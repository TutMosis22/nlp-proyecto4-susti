import openai
import os
from typing import List
from dotenv import load_dotenv

# SE CARGA LA API KEY DESDE .env

load_dotenv()  # Cargar variables de entorno
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key  # Configurar API key de OpenAI

# FUNCIÓN PARA GENERAR RESPUESTA CON UN PROMPT

def ejecutar_prompt(texto: str, prompt_plantilla: str, modelo: str = "gpt-3.5-turbo-instruct") -> str:
    """
    Aplica un prompt a un texto usando un modelo de OpenAI.

    Args:
        texto (str): Texto de entrada para clasificar.
        prompt_plantilla (str): Plantilla con {} para insertar el texto.
        modelo (str): Modelo de OpenAI a usar.

    Returns:
        str: Respuesta generada por el modelo.
    """
    try:
        prompt_formateado = prompt_plantilla.format(texto)

        respuesta = openai.Completion.create(
            engine=modelo,
            prompt=prompt_formateado,
            max_tokens=50,
            temperature=0.5,
            n=1
        )

        texto_generado = respuesta['choices'][0]['text'].strip()
        return texto_generado

    except Exception as e:
        print(f"[ERROR] Falló al ejecutar prompt: {e}")
        return "ERROR"

#FUNCIÓN PARA APLICAR UN PROMPT A UNA LISTA DE TEXTOS

def aplicar_prompt_a_lista(textos: List[str], prompt_plantilla: str, modelo: str = "gpt-3.5-turbo-instruct") -> List[str]:
    """
    Aplica un prompt a una lista de textos y devuelve las respuestas.

    Args:
        textos (List[str]): Lista de textos a procesar.
        prompt_plantilla (str): Plantilla del prompt con {}.
        modelo (str): Modelo de OpenAI.

    Returns:
        List[str]: Respuestas del modelo para cada texto.
    """
    resultados = []
    for texto in textos:
        respuesta = ejecutar_prompt(texto, prompt_plantilla, modelo)
        resultados.append(respuesta)
    return resultados
