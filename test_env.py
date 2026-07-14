import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Read the API key
api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    print("API Key Loaded Successfully!")
    print(f"First 10 characters: {api_key[:10]}...")
else:
    print("API Key NOT Found!")