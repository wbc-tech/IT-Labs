#!/bin/bash
# Bulk User Creation Script for Samba AD
# Reads from CSV and creates domain user accounts
# Usage: sudo bash bulk_create_users.sh

CSV_FILE="new_users.csv"
SUCCESS=0
FAILED=0

echo "========================================"
echo "  Bulk AD User Creation Script"
echo "  Domain: LAB.LOCAL"
echo "========================================"
echo ""

# Skip header line, read each row
tail -n +2 "$CSV_FILE" | while IFS=',' read -r first last username dept password; do
    echo "Creating user: $username ($first $last)"
    echo "  Department: $dept"
    
    if samba-tool user create "$username" "$password" \
        --given-name="$first" \
        --surname="$last" 2>/dev/null; then
        echo "  [SUCCESS] User $username created"
        ((SUCCESS++))
    else
        echo "  [SKIPPED] User $username already exists or failed"
        ((FAILED++))
    fi
    echo ""
done

echo "========================================"
echo "  Script Complete"
echo "========================================"
echo ""
echo "Current domain users:"
samba-tool user list