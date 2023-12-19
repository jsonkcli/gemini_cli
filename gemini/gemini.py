from vertexai.preview.generative_models import GenerativeModel
from vertexai.generative_models._generative_models import ResponseBlockedError
from html import escape


def get_model_response(user_input, model, generation_config):
    try:
        response = model.send_message(user_input, generation_config=generation_config)
        response_text = response.candidates[0].content.parts[0].text
        return escape(response_text)  # Escape HTML characters in response_text
    except ResponseBlockedError as e:
        print(f"Error: {e}")
        raise
    except UnicodeDecodeError as e:
        # Handle the case where the response is not valid UTF-8
        print(f"Error decoding response: {e}")
        return response.content  # Use raw bytes as a fallback
    except Exception as e:
        print(f"Error: {e}")
        # Print the raw response when encountering "not well-formed" errors
        print("Raw Response:", response.content.decode(errors="replace"))
        return "Invalid response"


class Gemini:
    def __init__(self):
        self.model = GenerativeModel("gemini-pro")
        self.chat = self.model.start_chat()

    def generate_response(self, user_input, generation_config):
        return get_model_response(user_input, self.chat, generation_config)
