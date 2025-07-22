import openai
import os
import time
from typing import List
from dotenv import load_dotenv

# SE CARGA LA API KEY DESDE .env

load_dotenv()  # Cargar variables de entorno
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key  # Configurar API key de OpenAI

# FUNCIÓN PARA GENERAR RESPUESTA CON UN PROMPT

client = openai.OpenAI(api_key=api_key)

def aplicar_prompt(texto: str, prompt: str) -> str:
    """
    Aplica un prompt a un solo texto usando el modelo GPT-3.5-Turbo.
    """
    try:
        respuesta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente útil."},
                {"role": "user", "content": prompt + "\n" + texto}
            ],
            temperature=0.7,
            max_tokens=512
        )
        return respuesta.choices[0].message.content.strip()

    except Exception as e:
        print("[ERROR] Falló al ejecutar prompt:\n", e)
        return "ERROR"

#FUNCIÓN PARA APLICAR UN PROMPT A UNA LISTA DE TEXTOS

def aplicar_prompt_a_lista(lista_textos: List[str], prompt: str) -> List[str]:
    """
    Aplica el mismo prompt a una lista de textos, devolviendo una lista de respuestas.
    """
    respuestas = []
    for i, texto in enumerate(lista_textos):
        print(f"[{i+1}/{len(lista_textos)}] Procesando...")
        respuesta = aplicar_prompt(texto, prompt)
        respuestas.append(respuesta)
        time.sleep(1.5)  # Para evitar límites de tasa
    return respuestas
