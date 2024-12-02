#!/bin/bash

TARGET_DIR="."

echo "Changing file permissions to 644..."
if sudo find "$TARGET_DIR" -type f -exec chmod 644 {} \;; then
    echo "File permissions changed successfully."
else
    echo "Failed to change file permissions." >&2
    exit 1
fi

echo "Changing directory permissions to 755..."
if sudo find "$TARGET_DIR" -type d -exec chmod 755 {} \;; then
    echo "Directory permissions changed successfully."
else
    echo "Failed to change directory permissions." >&2
    exit 1
fi

PRESTASHOP_DIR="prestashop"
echo "Changing ownership of $PRESTASHOP_DIR to www-data:root..."
if sudo chown -R www-data:root "$PRESTASHOP_DIR"; then
    echo "Ownership changed successfully."
else
    echo "Failed to change ownership." >&2
    exit 1
fi

echo "Script executed successfully."
