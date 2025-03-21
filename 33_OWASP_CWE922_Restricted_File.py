import os
import re

# Define locations to scan (Modify these paths as needed)
sensitive_files = [
    "/etc/passwd",
    "/etc/shadow",  # This will likely cause a permission error
    "/var/log/syslog",
    "/var/log/auth.log",
    "./config.json",
    "./database.db",
]

# Regular expressions for sensitive data patterns
patterns = {
    "password": r"(password\s*=\s*['\"].+?['\"])",  
    "api_key": r"(api[_-]?key\s*=\s*['\"].+?['\"])",
    "token": r"(token\s*=\s*['\"].+?['\"])",
    "credit_card": r"(\d{4}-\d{4}-\d{4}-\d{4})",  
    "private_key": r"(-{5}BEGIN.*?KEY-{5})"  
}

def check_insecure_storage():
    print("[*] Checking for insecure storage of sensitive information...\n")

    for file in sensitive_files:
        if os.path.exists(file):
            try:
                with open(file, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    for key, pattern in patterns.items():
                        if re.search(pattern, content, re.IGNORECASE):
                            print(f"[!] Possible Insecure Storage Found: {key} in {file}")
            except PermissionError:
                print(f"[!] Permission denied: Cannot access {file}")
    
    print("\n[+] Scan completed.")

# Run the check
check_insecure_storage()
