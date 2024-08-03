import asyncio
import os
import logging
import argparse
from dotenv import load_dotenv
from together import AsyncTogether, Together, error

# Configuración de registro (logging)
class CustomFormatter(logging.Formatter):
    """
    Esta clase formatea los mensajes de registro para mostrarlos en la consola con colores y un formato personalizado.
    Los colores hacen que sea más fácil distinguir los diferentes niveles de registro (depuración, información, advertencia, error, crítico).
    """

    # Códigos de colores ANSI para resaltar los diferentes niveles de registro
    blue = "\033[94m"   # Azul para DEBUG
    green = "\033[92m"  # Verde para INFO
    yellow = "\033[93m" # Amarillo para WARNING
    red = "\033[91m"    # Rojo para ERROR
    bold_red = "\033[1;91m" # Rojo negrita para CRITICAL
    reset = "\033[0m"    # Código para restablecer el color

    # Formato base para los mensajes de registro
    format = "%(asctime)s - %(levelname)s - %(message)s"

    # Diccionario que asigna cada nivel de registro a su formato con color correspondiente
    FORMATS = {
        logging.DEBUG: blue + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        """
        Formatea un registro de registro (log record) utilizando el formato correspondiente a su nivel.
        """
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt='%H:%M:%S')
        return formatter.format(record)


# Configuración inicial del registro
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Elimina cualquier handler de registro existente
logger.handlers = []

# Crea un manejador para mostrar los registros en la consola
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Establece el formateador personalizado en el manejador de consola
ch.setFormatter(CustomFormatter())

# Añade el manejador de consola al registrador
logger.addHandler(ch)

# Carga variables de entorno desde el archivo .env
_ = load_dotenv()

# Constantes del sistema
API_KEY = os.environ.get("TOGETHER_API_KEY")  # Obtiene la clave API desde las variables de entorno
TEMPERATURE = 0.7    # Controla la aleatoriedad de las respuestas de los modelos (0 = determinista, 1 = muy aleatorio)
MAX_TOKENS = 512     # Número máximo de tokens (palabras o subpalabras) que un modelo puede generar en una respuesta
RETRY_DELAYS = [1, 2, 4] # Tiempos de espera (en segundos) en caso de errores de límite de tasa (rate limit)

# Inicializa los clientes de la API Together
client = Together(api_key=API_KEY)         # Cliente para interacciones síncronas
async_client = AsyncTogether(api_key=API_KEY) # Cliente para interacciones asíncronas

# Listas de modelos
PROPOSAL_MODELS = [   # Modelos que generan propuestas de respuesta
    "Qwen/Qwen2-72B-Instruct",
    "google/gemma-2-27b-it",
    "zero-one-ai/Yi-34B-Chat",
    "deepseek-ai/deepseek-llm-67b-chat"
]

AGGREGATOR_MODEL = "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"
AGGREGATOR_SYSTEM_PROMPT = """\
You have been provided with a set of responses from various open-source models to the latest user query. \
Your task is to synthesize these responses into a single, high-quality response. \
It is crucial to critically evaluate the information provided in these responses, recognizing that some of it may be biased or incorrect. \
Your response should not simply replicate the given answers but should offer a refined, accurate, and comprehensive reply to the instruction. \
Ensure your response is well-structured, coherent, and adheres to the highest standards of accuracy and reliability.

Responses from models:""" # Instrucción para el modelo agregador (le dice qué hacer con las respuestas de los modelos de propuesta)

async def run_llm(model, user_prompt):
    """Ejecuta una llamada a un modelo de lenguaje grande (LLM) con reintentos en caso de errores de límite de tasa."""
    for sleep_time in RETRY_DELAYS:
        try:
            logger.info(f"Calling model {model} with prompt: {user_prompt}")
            response = await async_client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": user_prompt}],
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS,
            )
            logger.info(f"Received response from model {model}")
            return response.choices[0].message.content
        except error.RateLimitError as e:
            logger.warning(f"Rate limit exceeded for model {model}: {e}")
            await asyncio.sleep(sleep_time)
        except Exception as e:
            logger.error(f"Error running model {model}: {e}")
            return None
    return None

def __collect_responses(system_prompt, results):
    """Construye una instrucción para el modelo agregador que incluye las respuestas previas para sintetizar."""
    logger.info("Collecting responses from models")
    return (
        system_prompt
        + "\n"
        + "\n".join([f"{i+1}. {element}" for i, element in enumerate(results)])
    )

async def __gather_responses(models, user_prompt):
    """Recopila las respuestas de todos los modelos de propuesta de forma asíncrona."""
    logger.info("Gathering responses from proposal models")
    results = await asyncio.gather(*[run_llm(model, user_prompt) for model in models])  # Ejecuta las llamadas a los modelos asincrónicamente
    results = [result for result in results if result] # Filtra las respuestas que no son None (en caso de errores)
    logger.info(f"Collected {len(results)} responses from proposal models")
    return results

def __stream_final_response(finalStream):
    """Imprime la respuesta final del modelo agregador a medida que se recibe (en tiempo real)."""
    logger.info("Streaming final response from aggregator model")
    for chunk in finalStream: # Itera sobre los fragmentos de la respuesta a medida que se reciben
        print(chunk.choices[0].delta.content or "", end="", flush=True) # Imprime el contenido del fragmento (si hay alguno)

async def __run_aggregator_model(user_prompt, concatenated_results):
    """Ejecuta el modelo agregador con la instrucción y las respuestas concatenadas."""
    logger.info("Running aggregator model")
    finalStream = client.chat.completions.create(
        model=AGGREGATOR_MODEL,
        messages=[
            {"role": "system", "content": AGGREGATOR_SYSTEM_PROMPT + "\n" + concatenated_results},
            {"role": "user", "content": user_prompt},
        ],
        stream=True, # Habilita la transmisión en tiempo real de la respuesta
    )
    __stream_final_response(finalStream)

async def two_layer_moa(user_prompt):
    """Ejecuta el proceso MOA de dos capas."""
    results = await __gather_responses(PROPOSAL_MODELS, user_prompt)
    concatenated_results = "\n".join([f"{i+1}. {result}" for i, result in enumerate(results)]) # Concatena las respuestas en un formato legible
    await __run_aggregator_model(user_prompt, concatenated_results)

async def multi_layer_moa(user_prompt, layers):
    """Ejecuta el proceso MOA de múltiples capas."""
    results = await __gather_responses(PROPOSAL_MODELS, user_prompt)

    for layer in range(1, layers - 1): # Ejecuta las capas intermedias
        logger.info(f"Running layer {layer + 1} of {layers}")
        results = await __gather_responses(PROPOSAL_MODELS, user_prompt)

    concatenated_results = __collect_responses(AGGREGATOR_SYSTEM_PROMPT, results)
    await __run_aggregator_model(user_prompt, concatenated_results)

def main():
    parser = argparse.ArgumentParser(description="Run the MOA process.")
    parser.add_argument("--mode", type=str, choices=["two_layer", "multi_layer"], default="two_layer",
                        help="Choose the mode to run: 'two_layer' or 'multi_layer'.")
    parser.add_argument("--prompt", type=str, default="What is the meaning of life?",
                        help="The user prompt to provide to the models.")
    parser.add_argument("--layers", type=int, default=3, help="Number of layers for multi-layer MOA (default is 3).")
    
    args = parser.parse_args()

    user_prompt = args.prompt
    if args.mode == "two_layer":
        asyncio.run(two_layer_moa(user_prompt))
    elif args.mode == "multi_layer":
        asyncio.run(multi_layer_moa(user_prompt, args.layers))

if __name__ == "__main__":
    main()