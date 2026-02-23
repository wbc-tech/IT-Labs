#!/usr/bin/env python3
"""
Active Directory User Report Generator
Queries Samba AD and generates a formatted report of all domain users
"""

import subprocess
import datetime

def get_users():
    result = subprocess.run(
        ["samba-tool", "user", "list"],
        capture_output=True, text=True
    )
    return [u for u in result.stdout.strip().split("\n") if u]

def get_user_details(username):
    result = subprocess.run(
        ["samba-tool", "user", "show", username],
        capture_output=True, text=True
    )
    details = {}
    for line in result.stdout.strip().split("\n"):
        if ": " in line:
            key, value = line.split(": ", 1)
            details[key.strip()] = value.strip()
    return details

def main():
    print("=" * 60)
    print("  ACTIVE DIRECTORY USER REPORT")
    print(f"  Domain: LAB.LOCAL")
    print(f"  Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print()

    users = get_users()
    # Skip built-in accounts
    skip = ["krbtgt", "Guest"]
    report_users = [u for u in users if u not in skip]

    print(f"Total accounts: {len(users)}")
    print(f"Active user accounts: {len(report_users)}")
    print()
    print(f"{'Username':<15} {'Display Name':<25} {'Account Status':<15}")
    print("-" * 55)

    for username in sorted(report_users):
        details = get_user_details(username)
        display = details.get("displayName", details.get("cn", username))
        acct_control = details.get("userAccountControl", "N/A")
        status = "Disabled" if acct_control == "514" else "Active"
        print(f"{username:<15} {display:<25} {status:<15}")

    print()
    print("=" * 60)
    print("  END OF REPORT")
    print("=" * 60)

if __name__ == "__main__":
    main()