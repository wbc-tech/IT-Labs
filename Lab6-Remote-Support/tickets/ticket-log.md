# IT Support Ticket Log — LAB.LOCAL Environment

## Ticket #001
**Date:** 2026-02-21
**Submitted By:** John Smith (jsmith)
**Category:** Login Issue
**Priority:** High
**Status:** Resolved

**Issue:** User reports "cannot log in" to domain-joined Windows 11 workstation. Error message states credentials are incorrect.

**Troubleshooting Steps:**
1. Verified account exists in Active Directory: `sudo samba-tool user list`
2. Checked account status: `sudo samba-tool user show jsmith | grep userAccountControl` — returned 512 (active)
3. Discovered user was typing `LAB/jsmith` instead of `LAB\jsmith` — forward slash vs backslash
4. Tested login with correct format — successful

**Resolution:** Educated user on correct domain login format (LAB\jsmith or jsmith@lab.local). No account changes needed.

**Time to Resolution:** 10 minutes

---

## Ticket #002
**Date:** 2026-02-22
**Submitted By:** Multiple Users
**Category:** Network / Internet Access
**Priority:** High
**Status:** Resolved

**Issue:** Users report they can access internal resources (shared drives, intranet) but cannot reach any external websites. Affects all domain-joined machines.

**Troubleshooting Steps:**
1. Ran `ping 192.168.64.4` from client — success (internal connectivity works)
2. Ran `ping google.com` — failed ("could not find host")
3. Ran `nslookup google.com` — DNS query failed for external names
4. Ran `nslookup lab.local` — internal DNS working correctly
5. Checked DNS forwarder on domain controller: `cat /etc/samba/smb.conf`
6. Found `dns forwarder = 127.0.0.53` pointing to disabled systemd-resolved service
7. Updated forwarder to `dns forwarder = 8.8.8.8` (Google Public DNS)
8. Restarted Samba AD service: `sudo systemctl restart samba-ad-dc`
9. Flushed DNS on client: `ipconfig /flushdns`
10. Tested: `ping google.com` — success

**Resolution:** DNS forwarder was pointing to a disabled local DNS resolver. Updated to Google Public DNS (8.8.8.8) and restarted the DNS service. All users regained internet access.

**Time to Resolution:** 25 minutes

---

## Ticket #003
**Date:** 2026-02-22
**Submitted By:** Brandon (local admin)
**Category:** Account Lockout / Failed Login
**Priority:** Medium
**Status:** Resolved

**Issue:** 4 failed login attempts detected in Security Event Log (Event ID 4625) for account "Brandon" on domain LAB.

**Troubleshooting Steps:**
1. Queried security logs: `Get-EventLog -LogName Security -InstanceId 4625 -Newest 10`
2. Identified 4 failed attempts for account "Brandon" — account does not exist on domain
3. Failure code 0xc0000064 confirmed: "account does not exist"
4. Source was local machine (127.0.0.1) — not an external attack
5. Determined this was an admin attempting to log in with a local account name on the domain login screen

**Resolution:** False alarm. Failed attempts were from administrator using incorrect account name on domain login screen. No security threat. Documented for audit trail.

**Time to Resolution:** 10 minutes

---

## Ticket #004
**Date:** 2026-02-23
**Submitted By:** HR Department
**Category:** New Employee Onboarding
**Priority:** Low
**Status:** Resolved

**Issue:** HR submitted request to create accounts for 5 new employees starting across IT and HR departments.

**Troubleshooting Steps:**
1. Received CSV file from HR with employee details
2. Verified all required fields present: first name, last name, username, department, password
3. Ran bulk user creation script: `sudo bash bulk_create_users.sh`
4. All 5 accounts created successfully: sjohnson, mdavis, lchen, tbaker, jwilson
5. Verified accounts with: `sudo samba-tool user list`
6. Generated user report with: `sudo python3 ad_user_report.py`

**Resolution:** All 5 accounts created and verified. Credentials sent to department managers for distribution to new employees. Report generated for HR records.

**Time to Resolution:** 15 minutes

---

## Ticket #005
**Date:** 2026-02-23
**Submitted By:** John Smith (jsmith)
**Category:** Password Reset
**Priority:** Low
**Status:** Resolved

**Issue:** User reports they forgot their password and cannot log in.

**Troubleshooting Steps:**
1. Verified user identity through manager confirmation
2. Checked account status: `sudo samba-tool user show jsmith | grep userAccountControl` — 512 (active, not locked)
3. Reset password: `sudo samba-tool user setpassword jsmith --newpassword="Welcome2Lab!23"`
4. Informed user of temporary password through secure channel
5. Instructed user to change password at next login

**Resolution:** Password reset completed. User able to log in with new credentials.

**Time to Resolution:** 5 minutes