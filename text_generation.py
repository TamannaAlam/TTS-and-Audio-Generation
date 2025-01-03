from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a short story about a cat and a robot"
        }
    ]
)

print(completion.choices[0].message)

with open("response.txt", "w") as file:
    file.write(str(completion.choices[0].message))

print("Response saved to response.txt")