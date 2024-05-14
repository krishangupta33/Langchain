import os
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Now retrieve the OPENAI_API_KEY
openai_api_key = os.getenv("OPENAI_API_KEY")

if openai_api_key is None:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

os.environ["OPENAI_API_KEY"] = openai_api_key

# Continue with the rest of your script
print(os.getenv("OPENAI_API_KEY"))
