import requests
import re

def check_weak_encoding_for_password(url):
    try:
        # Send a GET request to the target URL (replace with the actual login or password change page URL)
        response = requests.get(url)
        
        # Check if the URL contains password fields in GET requests (URL parameter)
        if 'password' in response.url or 'pwd' in response.url:
            print(f"Warning: Password is being sent through GET request in the URL: {response.url}")
        
        # If the site contains an HTTP form, check the form method and action
        if 'html' in response.headers['Content-Type']:
            print("Checking form for weak encoding...")
            form = re.findall(r'<form[^>]*action="([^"]*)"[^>]*>', response.text)
            if form:
                print(f"Form found with action: {form[0]}")
                # Look for weak hash or encoding techniques in the form data
                if re.search(r'(MD5|Base64|SHA1)', response.text, re.IGNORECASE):
                    print("Warning: Weak encoding or hash algorithm detected in form.")
                else:
                    print("Form does not appear to use weak encoding.")
            else:
                print("No form found.")
        
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")

# Get URL input from the user
target_url = input("Please enter the target URL (e.g., https://example.com/login): ")
check_weak_encoding_for_password(target_url)

