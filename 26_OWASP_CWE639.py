import requests

def check_auth_bypass(target_url, test_ids):
    print(f"[*] Checking for authorization bypass at {target_url}...")

    for test_id in test_ids:
        test_url = target_url.replace("{{ID}}", str(test_id))  # Replace placeholder with test ID
        try:
            response = requests.get(test_url, timeout=5)
            
            if response.status_code == 200 and "Unauthorized" not in response.text:
                print(f"[!] Possible Vulnerability: Access granted to ID {test_id} -> {test_url}")
            else:
                print(f"[-] Access denied for ID {test_id} (Expected behavior)")

        except requests.exceptions.RequestException as e:
            print(f"[-] Error accessing {test_url}: {e}")

# Get user input
target_url = input("Enter the target URL with {{ID}} placeholder (e.g., https://example.com/profile?id={{ID}}): ")
test_ids = [1001, 1002, 1003, 9999]  # Example IDs to test

check_auth_bypass(target_url, test_ids)
