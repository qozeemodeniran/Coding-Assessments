import requests
import time

URLS = [
    "https://url1.com",
    "https://url2.com",
    "https:///www.google.com",
]

def monitor_urls():
    while True:
        for url in URLS:
            try:
                response = requests.get(url)
                if response.status_code != 200:
                    print(f"URL: {url} returned status code {response.status_code}.")
                else:
                    print(f"URL: {url} is up.")
            except requests.exceptions.RequestException as e:
                print(f"Error accessing URL: {url}. Error: {e}")
        time.sleep(5)

if __name__ == "__main__":
    monitor_urls()