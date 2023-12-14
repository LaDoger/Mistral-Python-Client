import os
from dotenv import load_dotenv
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage


def main():
    load_dotenv()

    api_key = os.getenv("MISTRAL_API_KEY")
    model = "mistral-medium"

    client = MistralClient(api_key=api_key)

    while True:
        user_message = input("Question: ")

        messages = [
            ChatMessage(role="system", content="You are an AI that replies in an extremely concise manner."),
            ChatMessage(role="user", content=user_message)
        ]

        chat_response = client.chat(
            model=model,
            messages=messages,
        )

        print("Answer: ", end="")
        print(chat_response.choices[0].message.content)
        print("--------")


if __name__ == "__main__":
    main()