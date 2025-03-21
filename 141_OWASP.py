import requests
import re

def check_configuration_vulnerabilities(url):
    try:
        print(f"Checking for CWE-16: Configuration Issues at {url}...\n")
        
        # Check for the presence of configuration files
        config_files = ['/config.php', '/settings.json', '/config.xml']
        for config_file in config_files:
            config_url = url + config_file
            response = requests.get(config_url)
            if response.status_code == 200:
                print(f"Warning: Configuration file {config_file} found. This could expose sensitive information.")
                
                # Check for potential sensitive data in the configuration file
                if re.search(r'password|apiKey|secret|token', response.text, re.IGNORECASE):
                    print(f"Warning: Sensitive data (e.g., password, API key) found in {config_file}.")
        
        # Check for debug or development mode exposure (e.g., debug=true in query parameters or headers)
        if '?debug=true' in url:
            print("Warning: Debug mode is enabled in the URL query parameter. This could expose sensitive data.")
        
        # Check for insecure HTTP headers that might indicate misconfigured security settings
        response = requests.get(url)
        headers = response.headers
        for header, value in headers.items():
            if re.search(r'config|setting|debug|env', header, re.IGNORECASE):
                print(f"Warning: Potentially insecure header found: {header}={value}. This could reveal configuration details.")
        
        # Check for configuration-related environment variables in HTTP headers (e.g., X-Env)
        if 'X-Env' in headers:
            print(f"Warning: Environment variable exposure found: {headers['X-Env']}. Configuration may be exposed.")

        # Check for insecure authentication or weak config settings (e.g., weak passwords in headers)
        if 'Authorization' in headers and 'Basic' in headers['Authorization']:
            print(f"Warning: Basic Authentication detected in the header. This could be insecure if not encrypted over HTTPS.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Get URL input from user
target_url = input("Please enter the target URL (e.g., https://example.com): ")
check_configuration_vulnerabilities(target_url)

