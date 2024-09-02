import json
import os
from dotenv import load_dotenv
from src.utils import create_timestamped_filename, get_latest_file

# Get the root directory path of the project
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load environment variables
load_dotenv(os.path.join(PROJECT_ROOT, '.env'))


def extract_relevant_info(product):
    return {
        "name": product["name"],
        "id": product["productId"],
        "sku": product["sku"],
        "ean": product["ean"],
        "brand": product["brand"],
        "category": product["categories"][0] if product["categories"] else "",
        "net_content": product["netContent"],
        "regular_price": product["sellers"][0]["listPrice"] if product["sellers"] else None,
        "discount_price": product["sellers"][0]["price"] if product["sellers"] else None,
        "savings": product["sellers"][0]["saving"] if product["sellers"] else None,
        "discount_percentage": product["priceDetail"]["discountPercentage"] if "priceDetail" in product else None,
        "price_per_liter": product["sellers"][0]["ppum"] if product["sellers"] else None,
        "main_image": product["images"][0] if product["images"] else None,
        "description": product["description"],
        "url": product["detailUrl"]
    }


def process_products():
    data_dir = os.getenv("DATA_DIR", 'data')
    raw_dir = os.getenv("RAW_DATA_DIR", 'raw')
    processed_dir = os.getenv("PROCESSED_DATA_DIR", 'processed')

    # Get the latest raw data file
    input_filename = get_latest_file(os.path.join(PROJECT_ROOT, data_dir, raw_dir), 'available_products')
    if not input_filename:
        print("No raw data files found. Please run the scraper first.")
        return

    output_filename = create_timestamped_filename('processed_products')

    # Create absolute paths
    input_dir = os.path.join(PROJECT_ROOT, data_dir, raw_dir)
    output_dir = os.path.join(PROJECT_ROOT, data_dir, processed_dir)

    # Ensure directories exist
    os.makedirs(output_dir, exist_ok=True)

    input_path = os.path.join(input_dir, input_filename)
    output_path = os.path.join(output_dir, output_filename)

    with open(input_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    raw_timestamp = raw_data.get('timestamp')
    available_products = raw_data.get('products', [])
    processed_products = [extract_relevant_info(product) for product in available_products]

    # Create processed data structure with timestamp
    processed_data = {
        'timestamp': raw_timestamp,
        'processing_timestamp': create_timestamped_filename('')[:-5],  # Remove '.json' from the end
        'products': processed_products
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=4)

    print(f"{len(processed_products)} products have been processed and saved to {output_path}")


if __name__ == "__main__":
    process_products()