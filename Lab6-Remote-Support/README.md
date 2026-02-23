# Lab 6: Remote Support & Documentation

## Objective
Create professional IT support documentation including troubleshooting runbooks and a support ticket log based on real issues encountered during lab setup. Demonstrate the documentation and communication skills essential for help desk and IT support roles.

## Tools Used
- Markdown for documentation
- Git/GitHub for version control and publishing
- All tools from Labs 1-5 referenced in runbooks

## Documents Created

### IT Support Runbook
**File:** [runbooks/common-issues.md](runbooks/common-issues.md)

A comprehensive troubleshooting guide covering the 6 most common help desk scenarios:
1. **User Cannot Log In** — account verification, status checks, resolution steps
2. **User Cannot Access Internet** — systematic network diagnosis using ping, nslookup, ipconfig
3. **Password Reset Request** — identity verification, secure reset process, communication
4. **Account Lockout** — lockout verification, brute force detection, escalation criteria
5. **Cannot Connect to Network Drive** — SMB connectivity testing, permission checks, drive remapping
6. **New Employee Onboarding** — full account creation workflow from HR request to workstation setup

Each runbook entry includes severity level, estimated resolution time, step-by-step commands, and verification steps.

### Support Ticket Log
**File:** [tickets/ticket-log.md](tickets/ticket-log.md)

Documented 5 real support tickets based on actual issues encountered during lab setup:
- **Ticket #001:** Domain login format issue (forward slash vs backslash)
- **Ticket #002:** DNS forwarder misconfiguration causing external DNS failure
- **Ticket #003:** Failed login investigation from security event logs
- **Ticket #004:** Bulk user onboarding using automation scripts
- **Ticket #005:** Password reset following identity verification

Each ticket follows a standard format: date, submitter, category, priority, issue description, troubleshooting steps, resolution, and time to resolution.

## Real-World Application
- **Runbooks** are used by every IT team to ensure consistent troubleshooting across the team. When a new hire joins IT, they follow runbooks until they learn the environment.
- **Ticket documentation** is how IT teams track work, measure performance, and maintain an audit trail. Every action taken on a user account should be logged.
- Good documentation separates average IT workers from great ones. Managers notice who writes clear tickets and who doesn't.

## Skills Demonstrated
- Technical writing and documentation
- Troubleshooting methodology (systematic diagnosis)
- Ticket lifecycle management (open, investigate, resolve, close)
- Runbook creation for team knowledge sharing
- Incident categorization and prioritization
- Communication skills (explaining technical issues clearly)