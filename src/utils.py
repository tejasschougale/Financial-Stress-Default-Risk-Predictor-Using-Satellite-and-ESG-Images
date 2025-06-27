import os
import psycopg2
from urllib.parse import urlparse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_db_connection():
    """
    Returns a psycopg2 connection using DATABASE_URL from .env
    """
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise ValueError("DATABASE_URL not set in .env")

    parsed = urlparse(db_url)

    return psycopg2.connect(
        host=parsed.hostname,
        port=parsed.port,
        dbname=parsed.path.lstrip('/'),
        user=parsed.username,
        password=parsed.password
    )

def log(message):
    """
    Simple logger for notebook and CLI debugging.
    """
    print(f"[LOG] {message}")

