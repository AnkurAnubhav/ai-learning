import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

messages = []

question = input("You: ")
while question != "quit":
    messages.append({"role": "user", "content": question})

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=messages
    )

    response = message.content[0].text
    print(f"Claude: {response}")

    messages.append({"role": "assistant", "content": response})

    question = input("You: ")

print("Goodbye!")