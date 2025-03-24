import requests

def check_sensitive_cookie_http_only(url):
    try:
        # Send a GET request to the target URL
        response = requests.get(url)
        
        # Check if there are cookies set in the response
        if 'Set-Cookie' in response.headers:
            cookies = response.cookies
            print(f"Cookies for {url}:")
            
            # Check each cookie for the 'HttpOnly' flag
            for cookie in cookies:
                cookie_name = cookie.name
                cookie_value = cookie.value
                cookie_flags = response.headers.get('Set-Cookie', '')
                
                if 'HttpOnly' in cookie_flags:
                    print(f"Cookie '{cookie_name}' is secure with HttpOnly flag.")
                else:
                    print(f"Cookie '{cookie_name}' is NOT secure! It lacks the HttpOnly flag.")
        else:
            print(f"No cookies set by {url}.")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")

# Get URL input from the user
target_url = input("Please enter the target URL (e.g., https://example.com): ")
check_asp_net_debug_misconfiguration(target_url)
