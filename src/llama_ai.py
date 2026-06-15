from groq import Groq
from config import GEMINI_API_KEY

client = Groq(api_key=GEMINI_API_KEY)  # Groq keys start with gsk_



def ask_ask(question):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages= [{"role": "user", "content" : question}]
    )

    return response.choices[0].message.content