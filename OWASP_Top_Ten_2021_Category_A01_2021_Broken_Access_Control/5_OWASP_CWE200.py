import requests

def check_sensitive_data_exposure(url):
    print(f"Checking for Exposure of Sensitive Information on: {url}")

    # Check for common headers that might reveal sensitive information
    headers_to_check = ['X-Powered-By', 'Server', 'X-AspNet-Version']
    response = requests.get(url)

    # Check if any sensitive information is exposed in headers
    for header in headers_to_check:
        if header in response.headers:
            print(f"[!] Sensitive information exposed in header: {header}: {response.headers[header]}")

    # Triggering error by invalidating common inputs (e.g., invalid login, bad API request)
    error_url = url + "/login"  # Example login page (change as needed)
    invalid_data = {'username': 'invalid', 'password': 'invalid'}
    error_response = requests.post(error_url, data=invalid_data)

    # Checking for detailed error messages that expose sensitive information
    if 'error' in error_response.text or 'exception' in error_response.text:
        print(f"[!] Sensitive error message found on {error_url} (Check response manually)")

    # Check for sensitive data in URLs or parameters
    if 'token' in response.text or 'password' in response.text:
        print("[!] Sensitive data found in URL or query parameters")

# Get the target URL input from the user
target_url = input("Please enter the target URL (e.g., https://example.com): ")
check_sensitive_data_exposure(target_url)
