
import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_NAME = "Fluency Coach"

TAGLINE = "Understand your speech. Build your confidence."

DESCRIPTION = (
    "Speech disfluency detection system "
    "designed to support speech awareness and practice."
)

# The backend URL will be provided once the API is ready.
API_URL = os.getenv("API_URL", "http://localhost:8000")

# Change this to the actual endpoint agreed upon with your teammate.
PREDICT_ENDPOINT = f"{API_URL}/predict"

# Keep this False until the real model API is available.
USE_MOCK_MODE = False

ALLOWED_AUDIO_TYPES = ["wav", "mp3"]
