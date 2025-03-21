import os

# List of critical directories to check
directories_to_check = ["/etc", "/home", "/var/www", "/usr/local/bin"]

def check_default_permissions():
    print("Checking for incorrect default permissions...")

    for directory in directories_to_check:
        if os.path.exists(directory):
            permissions = oct(os.stat(directory).st_mode)[-3:]
            if permissions in ["777", "775", "666"]:
                print(f"[!] Insecure default permissions: {directory} (Permissions: {permissions})")
            else:
                print(f"[-] Secure permissions: {directory} (Permissions: {permissions})")
        else:
            print(f"[-] Directory not found: {directory}")

check_default_permissions()
