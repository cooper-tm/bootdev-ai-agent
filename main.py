import argparse
import os

from dotenv import load_dotenv
from openai import OpenAI

from prompts import system_prompt


def main():
    print("Hello from test-agent!")

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key == None:
        raise RuntimeError("key not found")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    user_prompt = args.user_prompt

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0,
    )

    prompt_tokens = response.usage.prompt_tokens
    response_tokens = response.usage.completion_tokens

    if response.usage == None:
        raise RuntimeError("usage property is empty")

    if args.verbose:
        print(f"User prompt:\n{user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    print(f"Response:\n{response.choices[0].message.content}")


if __name__ == "__main__":
    main()
