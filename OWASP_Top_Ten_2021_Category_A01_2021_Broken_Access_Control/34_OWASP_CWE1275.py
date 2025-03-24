import requests

def check_sensitive_cookie_samesite(target_url):
    try:
        response = requests.get(target_url)

        # Retrieve all cookies from the response
        cookies = response.cookies

        print(f"[*] Checking cookies for SameSite attribute on {target_url}...\n")
        
        for cookie in cookies:
            # Check for SameSite attribute in the cookie
            if 'SameSite' not in cookie.__dict__:
                print(f"[!] Cookie '{cookie.name}' does not have SameSite attribute.")
            else:
                samesite_value = cookie.__dict__['SameSite']
                if samesite_value.lower() not in ['strict', 'lax']:
                    print(f"[!] Cookie '{cookie.name}' has an improper SameSite attribute value: {samesite_value}")
                else:
                    print(f"[+] Cookie '{cookie.name}' has a valid SameSite attribute: {samesite_value}")

        # Check if cookies have Secure and HttpOnly flags
        for cookie in cookies:
            if cookie.secure:
                print(f"[+] Cookie '{cookie.name}' has the Secure flag.")
            else:
                print(f"[!] Cookie '{cookie.name}' is missing the Secure flag.")

            if cookie.has_nonstandard_attr('HttpOnly'):
                print(f"[+] Cookie '{cookie.name}' has the HttpOnly flag.")
            else:
                print(f"[!] Cookie '{cookie.name}' is missing the HttpOnly flag.")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {target_url}: {e}")

# Get URL input from the user
target_url = input("Please enter the target URL (e.g., https://example.com): ")
check_sensitive_cookie_samesite(target_url)
