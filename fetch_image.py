import requests
import os
from urllib.parse import urlparse
import uuid

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get URL from user
    url = input("Please enter the image URL: ").strip()
    
    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)
        
        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        if not filename:  # If no filename, create one
            filename = f"image_{uuid.uuid4().hex}.jpg"
            
        # Save the image
        filepath = os.path.join("Fetched_Images", filename)
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
            
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")
        
    except requests.exceptions.MissingSchema:
        print("✗ Invalid URL format. Please include 'http://' or 'https://'")
    except requests.exceptions.HTTPError as e:
        print(f"✗ HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print("✗ Connection failed. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("✗ Request timed out.")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

if __name__ == "__main__":
    main()
