import requests
import re

# List of weak cryptographic algorithms
WEAK_ALGORITHMS = ["md5", "sha1", "des", "rc4", "rsa-1024"]

def check_weak_encryption(target_url):
    try:
        print(f"[*] Checking for cryptographic issues at: {target_url}")
        response = requests.get(target_url)

        if response.status_code == 200:
            for algo in WEAK_ALGORITHMS:
                if re.search(algo, response.text, re.IGNORECASE):
                    print(f"[!] Possible vulnerability: Weak encryption detected ({algo}) in {target_url}")

        else:
            print(f"[-] Unable to access {target_url}. Status Code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"[-] Error accessing {target_url}: {e}")

# Get URL input from the user
target_url = input("Enter the target URL (e.g., https://example.com): ")
check_weak_encryption(target_url)
