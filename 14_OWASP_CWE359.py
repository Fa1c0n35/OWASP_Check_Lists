import requests
import re

# Target API endpoint that may expose personal data
target_url = input("Enter the target URL (e.g., https://example.com/api/userinfo): ")

def check_personal_data_exposure():
    try:
        print("Checking for personal data exposure...")

        # Send a request as an unauthenticated user
        response = requests.get(target_url)

        if response.status_code == 200:
            data = response.text

            # Search for sensitive patterns (PII, email, SSN, phone numbers)
            if re.search(r'\b\d{3}-\d{2}-\d{4}\b', data):  # SSN Format
                print(f"[!] Possible Personal Data Leak: Social Security Number found in response.")
            if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', data):
                print(f"[!] Possible Personal Data Leak: Email address found in response.")
            if re.search(r'\b\d{10}\b', data):  # Basic Phone Number Pattern
                print(f"[!] Possible Personal Data Leak: Phone number found in response.")

            print("[!] Check response manually for more details.")
        else:
            print(f"[-] No data exposure detected (Response Code: {response.status_code})")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {target_url}: {e}")

check_personal_data_exposure()
