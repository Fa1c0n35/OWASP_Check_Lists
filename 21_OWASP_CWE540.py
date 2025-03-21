import requests
import re

# Common sensitive patterns
SENSITIVE_PATTERNS = [
    r"(?i)password\s*=\s*[\"'].*?[\"']",
    r"(?i)apikey\s*=\s*[\"'].*?[\"']",
    r"(?i)secret\s*=\s*[\"'].*?[\"']",
    r"(?i)aws_access_key_id\s*=\s*[\"'].*?[\"']",
    r"(?i)aws_secret_access_key\s*=\s*[\"'].*?[\"']",
    r"(?i)database_url\s*=\s*[\"'].*?[\"']"
]

def check_sensitive_info(target_url):
    print(f"[*] Scanning {target_url} for exposed source code with sensitive information...")

    try:
        response = requests.get(target_url, timeout=5)
        if response.status_code == 200:
            for pattern in SENSITIVE_PATTERNS:
                match = re.search(pattern, response.text)
                if match:
                    print(f"[!] Possible Vulnerability: Sensitive information found in {target_url} (Check manually)")
                    return
            print("[-] No sensitive information detected in the source code.")
        else:
            print(f"[-] Could not access {target_url}")
    except requests.exceptions.RequestException as e:
        print(f"[-] Error accessing {target_url}: {e}")

# Get user input
target_url = input("Enter the target URL (e.g., https://example.com/script.js): ")
check_sensitive_info(target_url)
