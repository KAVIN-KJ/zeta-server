from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_KEY")

prompt = input("Enter your prompt : ")

client = Groq(api_key=API_KEY)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a helpful assistant. who will help newbie Programmers to understand and solve errors in their programs. Always make sure to give links to any relevant web-articles for the user to learn, Give High preference to Youtube video links"
        },
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="llama3-70b-8192",
    temperature=0.5,
    max_completion_tokens=1024,
    top_p=1,
    stop=None,
    stream=False,
)

print(chat_completion.choices[0].message.content)
