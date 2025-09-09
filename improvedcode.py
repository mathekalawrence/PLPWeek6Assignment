import requests
import os
import hashlib
from urllib.parse import urlparse

def sanitize_filename(filename: str) -> str:
    """
    Ensure the filename is safe for saving on any OS.
    """
    return "".join(c for c in filename if c.isalnum() or c in (' ', '.', '_')).rstrip()

def fetch_images(urls):
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Creating storage directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    # Keeping track of downloaded hashes to prevent duplicates
    downloaded_hashes = set()

    for url in urls:
        try:
            print(f"Fetching: {url}")

            # Fetching image with safety precautions
            response = requests.get(url, timeout=10, headers={"User-Agent": "UbuntuFetcher/1.0"})
            response.raise_for_status()

            # Security: checking headers before saving
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print(f" Skipped!: {url} (not an image, Content-Type={content_type})")
                continue

            # Extracting filename from URL or even generating one
            parsed_url = urlparse(url)
            filename = sanitize_filename(os.path.basename(parsed_url.path))
            if not filename:
                filename = "downloaded_image.jpg"

            # Preventing duplicate downloads by hashing content
            file_hash = hashlib.sha256(response.content).hexdigest()
            if file_hash in downloaded_hashes:
                print(f"Alert!.. Duplicate skipped: {filename}")
                continue

            filepath = os.path.join("Fetched_Images", filename)

            # Save the image
            with open(filepath, "wb") as f:
                f.write(response.content)

            downloaded_hashes.add(file_hash)
            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}\n")

        except requests.exceptions.RequestException as e:
            print(f" Connection error: {e}")
        except Exception as e:
            print(f"✗ An error occurred: {e}")

    print("Connection strengthened. Community enriched.")


def main():
    # Asking the user for multiple URLs (comma separated)
    user_input = input("Please enter one or more image URLs (comma separated): ")
    urls = [url.strip() for url in user_input.split(",") if url.strip()]
    
    if urls:
        fetch_images(urls)
    else:
        print("No URLs provided. Exiting.")


if __name__ == "__main__":
    main()