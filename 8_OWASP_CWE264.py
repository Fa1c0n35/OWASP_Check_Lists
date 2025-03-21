import os

# List of sensitive files to check for weak permissions
sensitive_files = [
    "/etc/passwd", "/etc/shadow", "/etc/sudoers", 
    "/var/www/html/config.php", "/home/user/.ssh/id_rsa"
]

def check_file_permissions():
    print("Checking for weak file permissions...")

    for file in sensitive_files:
        if os.path.exists(file):
            permissions = oct(os.stat(file).st_mode)[-3:]
            if permissions in ["777", "666", "755"]:
                print(f"[!] Insecure permissions detected: {file} (Permissions: {permissions})")
            else:
                print(f"[-] Secure permissions: {file} (Permissions: {permissions})")
        else:
            print(f"[-] File not found: {file}")

check_file_permissions()
