# Proyecto 4: Prompting básico y control de salida

Este proyecto analiza cómo la estructura del prompt afecta la respuesta de un modelo de lenguaje (LLM) al realizar una tarea de clasificación de sentimientos. Se estudian variaciones con y sin ejemplos in-context y se comparan métricas de salida.

## Objetivo
Comparar precisión, coherencia y sesgos según el tipo de prompt.

## Estructura

- `notebooks/`: notebooks con prompts y ejecución
- `data/`: ejemplos usados
- `src/`: código para métricas
- `results/`: tabla final comparativa

## Términos clave tratados

- Transformer
- Modelado de lenguaje
- Tokenización
- Embeddings
- Fine-tuning
- Prompts e in-context learning
- Hallucinations y sesgos
- LangChain y RAG (referencial)
- Scaling laws y context size

## Instalación

```bash
git clone https://github.com/TutMosis22/nlp-proyecto4-susti.git
cd nlp-proyecto4-susti
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt