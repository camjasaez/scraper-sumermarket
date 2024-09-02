import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Database configuration
    DATABASE_PATH = os.path.join('data', 'products.db')

    # Scraper configuration
    SCRAPER_URL = os.getenv('URL')
    SCRAPER_INTERVAL = int(os.getenv('SCRAPER_INTERVAL', '3600'))  # Interval in seconds, default 1 hour

    # API configuration
    API_HOST = os.getenv('API_HOST', '0.0.0.0')
    API_PORT = int(os.getenv('API_PORT', '8000'))

    # File paths
    RAW_DATA_PATH = os.path.join('data', 'raw', 'available_products.json')
    PROCESSED_DATA_PATH = os.path.join('data', 'processed', 'processed_products.json')

    # Other configurations
    DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')

config = Config()