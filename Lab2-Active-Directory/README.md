# Lab 2: Active Directory & User Management

## Objective
Configure a fully functional Active Directory domain controller using Samba on Ubuntu Linux, and join a Windows 11 client to the domain. Practice user account management, group management, and domain authentication.

## Tools Used
- Ubuntu 22.04 LTS ARM (Samba AD Domain Controller)
- Windows 11 Pro ARM (Domain-joined client)
- Samba AD, Kerberos, DNS

## Environment
- Domain: LAB.LOCAL
- Domain Controller: ubuntu.lab.local (192.168.64.4)
- Windows Client: Windows 11 Pro joined to LAB.LOCAL

## Labs Completed

### 2.1 - Install and Configure Samba Active Directory
- Installed Samba, Kerberos, and Winbind packages
- Provisioned AD domain: LAB.LOCAL with Samba internal DNS
- Resolved DNS port conflict: systemd-resolved was occupying port 53, preventing Samba DNS from starting. Identified conflict using `ss -tlnp | grep 53`, disabled systemd-resolved, and configured /etc/resolv.conf to point to localhost
- Verified domain with `samba-tool domain level show` (Forest/Domain level: Windows 2008 R2)
- Confirmed DNS working with `host -t SRV _ldap._tcp.lab.local localhost`

### 2.2 - Create Organizational Units
- Created IT Department OU: `samba-tool ou create "OU=IT Department,DC=lab,DC=local"`
- Created HR Department OU: `samba-tool ou create "OU=HR Department,DC=lab,DC=local"`
- Verified with `samba-tool ou list`

### 2.3 - Create and Manage User Accounts
- Created domain users:
  - jsmith (John Smith)
  - bwilson (Brian Wilson)
  - amartin (Alice Martin)
- Verified with `samba-tool user list`

### 2.4 - Security Group Management
- Created IT Support security group
- Added jsmith and bwilson as members
- Verified membership with `samba-tool group listmembers "IT-Support"`

### 2.5 - Domain Join Windows 11 Client
- Configured Windows 11 DNS to point to domain controller (192.168.64.4)
- Disabled IPv6 to resolve DNS resolution issues with domain controller
- Joined domain using `Add-Computer -DomainName "lab.local" -Credential LAB\Administrator`
- Successfully logged in as domain user LAB\jsmith on Windows 11 client

## Troubleshooting
- **RSAT tools unavailable on ARM:** Windows 11 ARM has limited RSAT support. Pivoted to Samba AD on Linux as domain controller instead.
- **DNS port conflict:** systemd resolved was blocking Samba DNS on port 53. Resolved by disabling systemd resolved and manually configuring /etc/resolv.conf.
- **Windows DNS not resolving domain:** IPv6 DNS was taking priority over IPv4. Disabled IPv6 on the network adapter to force DNS queries to the Samba DC.
- **Windows Server ARM unavailable:** Microsoft removed ARM64 UUP files from update servers. Used Samba AD as a cross platform alternative that provides identical AD functionality.

## Skills Demonstrated
- Active Directory domain controller setup and configuration
- Samba AD provisioning and management
- DNS configuration and troubleshooting
- Organizational Unit (OU) creation
- User and group account management
- Domain join process for Windows clients
- Cross platform administration (Linux DC + Windows client)
- Port conflict diagnosis and resolution