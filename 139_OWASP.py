import requests
import re

def check_password_in_config(url):
    try:
        # Check for the presence of web.config or appsettings.json files
        config_urls = [url + "/web.config", url + "/appsettings.json"]
        
        for config_url in config_urls:
            response = requests.get(config_url)
            if response.status_code == 200:
                print(f"Configuration file found: {config_url}")
                # Check for potential sensitive data like passwords
                if re.search(r'password\s*=\s*["\'](.*?)["\']', response.text, re.IGNORECASE):
                    print(f"Warning: Password found in configuration file at {config_url}.")
                if re.search(r'key\s*=\s*["\'](.*?)["\']', response.text, re.IGNORECASE):
                    print(f"Warning: API key or sensitive data found in configuration file at {config_url}.")
            else:
                print(f"No configuration file found at: {config_url}")
        
        # Check for any database connection string leaks in response or URL
        if 'connectionStrings' in response.text:
            print("Warning: Connection string found in the response.")
        
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")

# Get URL input from the user
target_url = input("Please enter the target URL (e.g., https://example.com): ")
check_password_in_config(target_url)
