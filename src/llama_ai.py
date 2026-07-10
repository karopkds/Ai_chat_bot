from dotenv import load_dotenv
load_dotenv()

from groq import Groq
from config import GROQ_API_KEY, LLM_MODEL

client = Groq(api_key=GROQ_API_KEY)



def ask_ask(question):
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content