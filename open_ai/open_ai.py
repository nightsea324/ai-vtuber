import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

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
