import openai
API_KEY = "xxxx-xxxx-xxxx" # enter your API key here
openai.api_key = API_KEY

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages=[
            {"role": "user", "content": "who are you?"}
        ]
)
print(response)
