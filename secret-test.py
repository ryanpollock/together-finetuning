from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the secret value
#api_key = os.getenv('TOGETHER_API_KEY')
api_key = os.environ.get("TOGETHER_API_KEY")

# Print the secret value
print(f'TOGETHER_API_KEY: {api_key}')