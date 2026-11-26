
import requests

from config import PREDICT_ENDPOINT


def analyze_audio(audio_file):

    try:
        audio_bytes = audio_file.getvalue()

        files = {
            "file": (
                audio_file.name,
                audio_bytes,
                audio_file.type or "audio/wav"
            )
        }

        response = requests.post(
            PREDICT_ENDPOINT,
            files=files,
            timeout=120
        )

        response.raise_for_status()

        result = response.json()

        if not isinstance(result, dict):
            return {
                "status": "error",
                "message": "The backend returned an unexpected response."
            }

        return result

    except requests.exceptions.ConnectionError:
        return {
            "status": "error",
            "message": "Backend is not running or is not connected."
        }

    except requests.exceptions.Timeout:
        return {
            "status": "error",
            "message": "Analysis took too long. Please try again."
        }

    except ValueError:
        return {
            "status": "error",
            "message": "The backend returned an invalid response."
        }

    except requests.exceptions.RequestException as error:
        return {
            "status": "error",
            "message": f"Could not analyze audio: {error}"
        }
