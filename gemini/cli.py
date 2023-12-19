from .gemini import Gemini

from prompt_toolkit import print_formatted_text, prompt, HTML
from prompt_toolkit.history import FileHistory
from prompt_toolkit.styles import Style

import os


def multiturn_generate_content():
    config = {"max_output_tokens": 8048, "temperature": 0.9}
    gemini = Gemini()

    # Define a custom style for the prompts and responses
    style = Style.from_dict(
        {
            "prompt": "#ff00ff bold",
            "response": "#00ff66 italic",
        }
    )

    history = FileHistory(".history")  # Store history in a file
    # user = system user. Idk how to get the system user in ptyhon to help me
    user = os.getlogin()

    while True:
        try:
            user_input = prompt(
                f"{user}> ", style=style, multiline=False, history=history
            )

            if user_input.lower() in ["exit", "quit", "q"]:
                break

            response_text = gemini.generate_response(user_input, config)

            # Print the user prompt and Gemini response with a line in between
            print_formatted_text(
                HTML(f"Gemini> <response>{response_text}</response>"),
                style=style,
                end="\n",
                style_transformation=None,
            )
        except KeyboardInterrupt:
            # Handle Ctrl+C to gracefully exit the loop
            print("Exiting.")
            break
        except Exception as e:
            print(f"Error: {e}")
            # Handle other exceptions as needed


def main():
    print("Gemini CLI - Type 'exit', 'quit', or 'q' to exit.")
    multiturn_generate_content()


if __name__ == "__main__":
    main()
