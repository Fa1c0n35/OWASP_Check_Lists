import requests
import re

def check_resource_leak(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            print(f"[+] Successfully accessed {url}")

            # Check for private resources in response
            sensitive_patterns = [
                r'api_key\s*=\s*["\'](.*?)["\']',      # API keys
                r'access_token\s*=\s*["\'](.*?)["\']', # Access tokens
                r'secret\s*=\s*["\'](.*?)["\']',       # Secrets
                r'private_url\s*=\s*["\'](.*?)["\']'   # Private URLs
            ]

            for pattern in sensitive_patterns:
                match = re.search(pattern, response.text, re.IGNORECASE)
                if match:
                    print(f"[!] Possible resource leak detected: {match.group()}")

        else:
            print(f"[!] Unable to access {url} (Status Code: {response.status_code})")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")

# Get URL input from the user
target_url = input("Enter the target URL to check for resource leaks: ")
check_resource_leak(target_url)
