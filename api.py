import os

import openai

MODEL = 'gpt-3.5-turbo'
openai.api_key = os.environ.get('OPENAI_API_KEY', '')
openai.organization = os.environ.get('OPENAI_ORGANIZATION', '')


def chat(content: list[dict[str, str]]):
    data = openai.ChatCompletion.create(
        model=MODEL,
        messages=content
    )
    response: str = data['choices'][0]['message']['content']
    return response
