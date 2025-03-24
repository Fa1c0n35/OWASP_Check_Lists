import requests

def check_cleartext_transmission(url):
    """
    This function checks if sensitive information is transmitted over cleartext (HTTP)
    instead of a secure connection (HTTPS).
    
    Args:
        url (str): The URL of the target website or API to test.
    
    Returns:
        None: Prints results based on whether the website uses HTTP or HTTPS.
    """
    try:
        # Check if the URL uses HTTPS
        if url.lower().startswith("https://"):
            print(f"Secure connection (HTTPS) detected for: {url}")
        elif url.lower().startswith("http://"):
            print(f"[WARNING] Cleartext connection (HTTP) detected for: {url}")
        else:
            print("[ERROR] Invalid URL format. Please use a valid URL with 'http://' or 'https://'.")
            return
        
        # Make a request to check for potential sensitive information in the response
        response = requests.get(url)
        
        if response.status_code == 200:
            print(f"Successfully connected to {url}. Now checking for sensitive data transmission.")
            # Check for sensitive data in the response headers or body (example: 'Authorization', 'password', 'token', etc.)
            sensitive_keywords = ['password', 'token', 'api_key', 'auth', 'authorization', 'secret']
            for keyword in sensitive_keywords:
                if keyword in response.text.lower():
                    print(f"[WARNING] Potential sensitive information found in the response from {url}.")
                    break
            else:
                print("No sensitive information found in the response.")
        else:
            print(f"Failed to connect to {url}. HTTP Status Code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Error accessing {url}: {e}")

# Input: Get the target URL from the user
target_url = input("Please enter the target URL (e.g., https://example.com): ")
check_cleartext_transmission(target_url)
