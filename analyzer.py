from groq import Groq
from dotenv import load_dotenv
from prompts import SISTEMA
import os

load_dotenv()
cliente = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analizar_documento(texto):
    respuesta = cliente.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SISTEMA},
            {"role": "user", "content": texto}
        ]
    )
    return respuesta.choices[0].message.content