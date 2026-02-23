# IT Support Runbook — Common Issues

## Table of Contents
1. User Cannot Log In
2. User Cannot Access the Internet
3. Password Reset Request
4. Account Lockout
5. User Cannot Connect to Network Drive
6. New Employee Onboarding

---

## 1. User Cannot Log In

**Severity:** High
**Estimated Time:** 5-15 minutes

### Step 1: Verify the Error Message
- Ask the user: "What exactly does the error say?"
- Common messages:
  - "The username or password is incorrect" → wrong credentials
  - "Your account has been disabled" → account disabled in AD
  - "Your account has been locked out" → too many failed attempts
  - "The trust relationship between this workstation and the primary domain failed" → machine needs to be re-joined to the domain

### Step 2: Check Account Status
```bash
# On the domain controller
sudo samba-tool user show <username> | grep userAccountControl
# 512 = Active, 514 = Disabled
```

### Step 3: Check if Account is Locked
```bash
sudo samba-tool user show <username> | grep lockoutTime
# If lockoutTime is not 0, the account is locked
```

### Step 4: Resolution
- **Wrong password:** Reset the password (see Runbook #3)
- **Disabled account:** Re-enable: `sudo samba-tool user enable <username>`
- **Locked out:** Unlock: `sudo samba-tool user setexpiry <username> --noexpiry` or wait for lockout duration (30 min)
- **Domain trust issue:** Re-join the computer to the domain

### Step 5: Verify and Close
- Have the user try logging in again
- Confirm the issue is resolved before closing the ticket

---

## 2. User Cannot Access the Internet

**Severity:** Medium
**Estimated Time:** 10-20 minutes

### Step 1: Determine Scope
- Ask: "Can you access any websites or is it all of them?"
- Ask: "Can your coworkers access the internet?"
- If multiple users affected → likely a server/network issue, escalate
- If single user → workstation issue, continue below

### Step 2: Check Network Connectivity
```powershell
# On the user's machine
ipconfig /all          # Verify IP, gateway, DNS
ping 192.168.64.1      # Can we reach the gateway?
ping 8.8.8.8           # Can we reach the internet by IP?
ping google.com        # Can we resolve DNS names?
```

### Step 3: Diagnose Based on Results
- **No IP address:** DHCP issue → `ipconfig /release` then `ipconfig /renew`
- **Can ping gateway but not 8.8.8.8:** Router/ISP issue → escalate to network team
- **Can ping 8.8.8.8 but not google.com:** DNS issue → check DNS settings, flush DNS: `ipconfig /flushdns`
- **Can't ping anything:** Check if cable is plugged in, check if WiFi is connected, check if adapter is enabled

### Step 4: Verify and Close
- Have user try loading a website
- Confirm resolution before closing ticket

---

## 3. Password Reset Request

**Severity:** Low
**Estimated Time:** 5 minutes

### Step 1: Verify Identity
- NEVER reset a password without verifying the user's identity
- Acceptable verification: employee ID, manager confirmation, security questions
- Do NOT reset based on email or phone call alone without verification

### Step 2: Reset the Password
```bash
# On the domain controller
sudo samba-tool user setpassword <username> --newpassword="TempPass123!"
```

### Step 3: Communicate to User
- Give the temporary password to the user securely (in person or encrypted message)
- Instruct them to change it immediately upon login
- Remind them of password requirements: 12+ characters, uppercase, lowercase, numbers, special characters

### Step 4: Document and Close
- Log which account was reset and when
- Never document the actual password in the ticket

---

## 4. Account Lockout

**Severity:** Medium
**Estimated Time:** 5-10 minutes

### Step 1: Verify the Lockout
```bash
sudo samba-tool user show <username> | grep lockoutTime
```

### Step 2: Determine Cause
- Check security event logs for Event ID 4625 (failed login attempts)
```powershell
Get-EventLog -LogName Security -InstanceId 4625 -Newest 20
```
- **A few failed attempts:** User probably forgot their password
- **Dozens of attempts from one IP:** Possible brute force attack → escalate to security team
- **Attempts from multiple IPs:** Possible credential stuffing → escalate immediately

### Step 3: Resolution
- If legitimate user: unlock the account and reset password if needed
- If suspicious activity: do NOT unlock, escalate to security team

### Step 4: Document and Close
- Record the cause of lockout
- If attack-related, create a security incident ticket

---

## 5. User Cannot Connect to Network Drive

**Severity:** Medium
**Estimated Time:** 10-15 minutes

### Step 1: Gather Information
- Ask: "What drive letter? What error message?"
- Ask: "Were you able to access it before?"
- Ask: "Can your coworkers access it?"

### Step 2: Check Connectivity
```powershell
# Test connection to the file server
ping <fileserver-ip>
Test-NetConnection -ComputerName <fileserver-ip> -Port 445
```
- Port 445 is SMB (file sharing). If this fails, it's a network or firewall issue.

### Step 3: Check Permissions
- Verify the user is in the correct security group for that share
```bash
sudo samba-tool group listmembers "<group-name>"
```

### Step 4: Try Remapping
```powershell
# Remove and remap the drive
net use Z: /delete
net use Z: \\server\share
```

### Step 5: Verify and Close
- Confirm user can access their files

---

## 6. New Employee Onboarding

**Severity:** Low
**Estimated Time:** 30-60 minutes

### Step 1: Receive Request
- HR provides: employee name, department, start date, manager, role
- Verify all information before proceeding

### Step 2: Create AD Account
```bash
sudo samba-tool user create <username> <temp-password> \
    --given-name="<first>" --surname="<last>"
```

### Step 3: Add to Groups
```bash
# Add to department group
sudo samba-tool group addmembers "<department-group>" <username>
# Add to any role-specific groups
sudo samba-tool group addmembers "<role-group>" <username>
```

### Step 4: Prepare Workstation
- Join computer to domain if not already joined
- Install required software
- Map network drives
- Set up email and other accounts

### Step 5: Document and Communicate
- Send credentials to new employee's manager (not directly to employee)
- Create a welcome document with:
  - Username and temporary password
  - How to change password
  - Key contacts in IT
  - How to submit support tickets