
# OpenAI/ChatGPT with Python

In this project we use the open_ai API to generate respones. We call openAI API using python3




## Install package 

First install openAI package , write the below command in your terminal 

```bash
  pip install openai
```
Explore further insights into this library/package by clicking [here.](https://pypi.org/project/openai/) 


## Code 
Import the OpenAI package 
```python
import openai
```

Assigning your API key in order to authenticate 
```python 
openai.api_key = "YOUR_API_KEY"
```
Getting our first response from that AI model
```python 
response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages=[
            {"role": "user", "content": "who are you?"}
        ]
)
```
Now to get the response 

```python 
print(response)

```
The response you will get will be in json or dictionary format with bunch of different extra information, to get the desired output 

```python
print(response["choices"][0]["message"]["content"])
```


## Complete code

```python 
import openai
API_KEY = "xxxx-xxxx-xxxx-xxxx"
openai.api_key = API_KEY

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages=[
            {"role": "user", "content": "who are you?"}
        ]
)
print(response)
```

## Reference

 - [Chat Competions API](https://platform.openai.com/docs/guides/gpt/chat-completions-api)

