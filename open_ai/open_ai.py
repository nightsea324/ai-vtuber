import openai
import os

messenge = [
    {
        "role": "system",
        "content": "You are a gaming streamer, and you are playing game on twitch."
    },
    {
        "role": "system",
        "content": "You are playing Apex Legend."
    },
]


def openaiInit():
    openai.api_key = os.getenv('OPENAI_API_KEY')
    return


def chat(msg):
    msg = msg.strip()
    if not msg:
        return 'no msg'

    # record
    messenge.append({"role": "user", "content": msg})
    # open ai api
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messenge
    )
    # record
    messenge.append({"role": "assistant", "content": response.choices[0].message.content})

    return messenge
