# Product Scraper and API

This project consists of a web scraper that collects product information, processes it, and stores it in a SQLite database. It also includes an API built with FastAPI to access the collected data.

## Project Structure

```
scraper-supermarket/
│
├── src/
│   ├── scraper/
│   │   ├── __init__.py
│   │   ├── scraper.py
│   │   └── json_processor.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── routes/
│   │   └── models/
│   └── database/
│       ├── __init__.py
│       └── db.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── tests/
├── config/
│   └── config.py
├── requirements.txt
├── README.md
├── .env
└── .env.example
```

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd scraper-supermarket
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - Copy the `.env.example` file and rename it to `.env`
   - Open the `.env` file and adjust the values according to your environment

## Usage

1. Run the scraper:
   ```
   python src/scraper/scraper.py
   ```

2. Process the data:
   ```
   python src/scraper/json_processor.py
   ```

3. Initialize the database:
   ```
   python src/database/db.py
   ```

4. Run the API:
   ```
   uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload
   ```

The API will be available at `http://localhost:8000`. You can access the API documentation at `http://localhost:8000/docs`.

## Data Structure

The data is stored in two formats:

1. Raw data: `data/raw/available_products.json`
2. Processed data: `data/processed/processed_products.json`

The SQLite database is created as `data/products.db`.

## Environment Variables

The main environment variables you can configure are:

- `SCRAPER_URL`: URL of the website to scrape
- `DATA_DIR`: Directory to store the data
- `API_HOST` and `API_PORT`: API server configuration
- `DATABASE_NAME`: Name of the database file
- `DEBUG`: Debug mode (True/False)
- `SCRAPER_INTERVAL`: Scraper execution interval in seconds

Refer to the `.env.example` file to see all available variables.

## Testing

To run the tests:

```
pytest tests/
```

## Contributing

If you'd like to contribute to the project, please:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - your@email.com

Project Link: [https://github.com/your-username/scraper-supermarket](https://github.com/your-username/scraper-supermarket)