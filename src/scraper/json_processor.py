import json
import os
from dotenv import load_dotenv

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
    input_filename = os.getenv("RAW_DATA_FILENAME", 'available_products.json')
    output_filename = os.getenv("PROCESSED_DATA_FILENAME", 'processed_products.json')

    # Create absolute paths
    input_dir = os.path.join(PROJECT_ROOT, data_dir, raw_dir)
    output_dir = os.path.join(PROJECT_ROOT, data_dir, processed_dir)

    # Ensure directories exist
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    input_path = os.path.join(input_dir, input_filename)
    output_path = os.path.join(output_dir, output_filename)

    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"The file {input_path} does not exist. Please run the scraper first.")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        available_products = json.load(f)

    processed_products = [extract_relevant_info(product) for product in available_products]

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(processed_products, f, ensure_ascii=False, indent=4)

    print(f"{len(processed_products)} products have been processed and saved to {output_path}")


if __name__ == "__main__":
    process_products()