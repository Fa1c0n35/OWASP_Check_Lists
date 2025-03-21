import os

# List of sensitive files & directories to check
sensitive_paths = [
    "/etc/passwd", "/etc/shadow", "/etc/sudoers",
    "/home/user/.ssh", "/var/www/html/config.php"
]

def check_permissions():
    print("Checking for weak file and directory permissions...")

    for path in sensitive_paths:
        if os.path.exists(path):
            permissions = oct(os.stat(path).st_mode)[-3:]
            if permissions in ["777", "666", "755"]:
                print(f"[!] Insecure permissions detected: {path} (Permissions: {permissions})")
            else:
                print(f"[-] Secure permissions: {path} (Permissions: {permissions})")
        else:
            print(f"[-] Path not found: {path}")

check_permissions()
