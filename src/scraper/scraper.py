import json
import os
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
from src.utils import create_timestamped_filename, add_timestamp_to_json

# Get the root directory path of the project
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load environment variables
load_dotenv(os.path.join(PROJECT_ROOT, '.env'))


def scrape_products():
    url = os.getenv("SCRAPER_URL")
    if not url:
        raise ValueError("SCRAPER_URL is not defined in the .env file")

    HEADERS = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': os.getenv("USER_AGENT",
                                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'),
        'Cache-Control': 'no-cache',
    }

    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = soup.find('script', {'id': '__NEXT_DATA__'})
    data = json.loads(data.string)

    available_products = data['props']['pageProps']['dehydratedState']['queries'][0]['state']['data'][
        'availableProducts']

    # Add timestamp to the scraped data
    available_products = add_timestamp_to_json({'products': available_products})

    return available_products


def save_raw_data(data, filename=None):
    if filename is None:
        base_filename = os.getenv("RAW_DATA_FILENAME", 'available_products')
        filename = create_timestamped_filename(base_filename)

    data_dir = os.getenv("DATA_DIR", 'data')
    raw_dir = os.getenv("RAW_DATA_DIR", 'raw')

    # Create absolute paths
    full_dir = os.path.join(PROJECT_ROOT, data_dir, raw_dir)
    os.makedirs(full_dir, exist_ok=True)

    file_path = os.path.join(full_dir, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Data saved to {file_path}")


if __name__ == "__main__":
    try:
        products = scrape_products()
        save_raw_data(products)
        print(f"{len(products['products'])} products have been saved")
    except Exception as e:
        print(f"Error executing the scraper: {str(e)}")