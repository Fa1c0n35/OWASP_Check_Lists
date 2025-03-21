import requests
import re

def check_external_control_of_config(url):
    try:
        print(f"Checking for CWE-15: External Control of System or Configuration Setting at {url}...\n")
        
        # Check for query parameters in the URL that could control configuration settings
        parsed_url = re.search(r"\?.*", url)
        if parsed_url:
            print(f"Warning: Query parameters found in URL. Potential risk of external control of configuration settings: {parsed_url.group()}")
        
        # Check for configuration settings in HTTP headers (e.g., X-Config)
        response = requests.get(url)
        headers = response.headers
        for header, value in headers.items():
            if re.search(r"config|setting|env|parameter", header, re.IGNORECASE):
                print(f"Warning: Configuration-related header found: {header}={value}. This could allow external control of settings.")
        
        # Check for sensitive configuration files accessible directly (e.g., web.config, appsettings.json)
        config_files = ["/web.config", "/appsettings.json", "/config/settings.json"]
        for config_file in config_files:
            config_url = url + config_file
            config_response = requests.get(config_url)
            if config_response.status_code == 200:
                print(f"Warning: Configuration file {config_file} found, exposing sensitive data.")
                
                # Check if configuration file contains any sensitive or insecure settings
                if re.search(r'password|apiKey|secret|token', config_response.text, re.IGNORECASE):
                    print(f"Warning: Sensitive data (e.g., password, API key) found in {config_file}.")
        
        # Check for possible manipulation of system environment variables via HTTP requests
        if 'X-Environment' in headers:
            print(f"Warning: Environment variable exposure found: {headers['X-Environment']}. External control of environment settings could be a risk.")
        
        # Check for URL patterns that could manipulate system settings
        if re.search(r"(\.\./|\.\.\\)", url):
            print(f"Warning: Path traversal detected in URL. This could allow external manipulation of system settings.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Get URL input from user
target_url = input("Please enter the target URL (e.g., https://example.com): ")
check_external_control_of_config(target_url)
