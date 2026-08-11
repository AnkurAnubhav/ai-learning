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
        system="you are a professional financial analyst. Your job is to analyze a stock and provide " \
        "clear recommendations for buy/sell/hold and price prediction in 1 year and 5 years. Keep" \
        "the responses straight and consice",
        messages=messages
    )

    response = message.content[0].text
    print(f"Claude: {response}")

    messages.append({"role": "assistant", "content": response})

    question = input("You: ")

print("Goodbye!")