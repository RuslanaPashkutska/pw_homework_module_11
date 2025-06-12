import os
from dotenv import load_dotenv

# Build the absolute path to the .env file located two levels up
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../.env'))


print(f"DEBUG: main.py is trying to load .env from: {dotenv_path}")

# Load environment variables from the specified .env file
load_dotenv(dotenv_path)


# Attempt to get the DATABASE_URL environment variable
db_url_from_env = os.getenv("DATABASE_URL")
if db_url_from_env:
    print(f"DEBUG: DATABASE_URL successfully loaded from .env: {db_url_from_env}")
else:
    print("DEBUG: DATABASE_URL NOT FOUND when loading .env manually.")

from .routes import router
from fastapi import FastAPI

# Initialize the FastAPI application
app = FastAPI()

# Include the router under the /api prefix
app.include_router(router, prefix="/api")