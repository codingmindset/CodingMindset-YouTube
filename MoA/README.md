# Mixture of Agents (MoA)

Este repositorio contiene una implementación demostrativa del concepto Mixture of Agents (MoA), utilizando múltiples modelos de lenguaje de gran escala (LLMs) a través de la API de Together para mejorar la calidad de las respuestas en tareas de procesamiento de lenguaje natural.

## Descripción

Esta aplicación demuestra cómo la metodología MoA puede mejorar significativamente la calidad de las respuestas generadas por LLMs. Utiliza una arquitectura en capas con múltiples agentes LLM, donde cada agente refina y mejora las respuestas generadas por los agentes en la capa anterior.

## Tutorial

Puedes ver el tutorial completo y el análisis de Mixture of Agents aquí 👇🏽👇🏽

[![Watch this video on YouTube](https://img.youtube.com/vi/jqHUdrxqlPQ/0.jpg)](https://www.youtube.com/watch?v=jqHUdrxqlPQ)

## Requisitos

- Python 3.10 o superior
- Poetry para la gestión de dependencias

## Instalación

1. **Clona el repositorio:**

   ```bash
   gh repo clone codingmindset/CodingMindset-YouTube
   cd MoA
   ```

2. **Instala las dependencias:**

   ```bash
   poetry install
   ```

3. **Configura la variable de entorno:**

   - Renombra el archivo `template.env` a `.env`:
     ```bash
     cp template.env .env
     ```

   - Abre `.env` y añade tu API key de Together:
     ```env
     TOGETHER_API_KEY=your_api_key_here
     ```

   Puedes obtener una API key registrándote en [Together](https://www.together.ai/).

## Uso

El script principal admite dos modos de ejecución: `two_layer` y `multi_layer`. Puedes ejecutar la demostración de MoA con los siguientes comandos:

```bash
# Modo de dos capas (por defecto)
poetry run python moa_demo.py --mode two_layer --prompt "Tu pregunta aquí"

# Modo de múltiples capas
poetry run python moa_demo.py --mode multi_layer --layers 3 --prompt "Tu pregunta aquí"
```

### Argumentos

- `--mode`: Elige el modo de ejecución (`two_layer` o `multi_layer`). Por defecto es `two_layer`.
- `--prompt`: La pregunta o instrucción que quieres que los modelos procesen.
- `--layers`: Número de capas para el modo `multi_layer`. Por defecto es 3.

## Funcionalidades

- **Múltiples Agentes LLM:** Utiliza varios modelos de lenguaje disponibles a través de la API de Together como agentes en diferentes capas.
- **Refinamiento Iterativo:** Cada capa de agentes refina y mejora las respuestas generadas por la capa anterior.
- **Agregación Final:** Un modelo agregador sintetiza la mejor respuesta basándose en las salidas de todos los agentes anteriores.
- **Modos de Ejecución:** Soporta un modo de dos capas y un modo de múltiples capas configurable.
- **Manejo de Errores:** Implementa reintentos en caso de errores de límite de tasa (rate limit).
- **Logging Personalizado:** Utiliza un sistema de logging con formato colorido para mejor legibilidad.

### Modelos Utilizados

- **Modelos de Propuesta:**
  - Qwen/Qwen2-72B-Instruct
  - google/gemma-2-27b-it
  - zero-one-ai/Yi-34B-Chat
  - deepseek-ai/deepseek-llm-67b-chat

- **Modelo Agregador:**
  - meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo


## Obtención de la API Key de Together

Para utilizar este demo, necesitarás una API key de Together. Sigue estos pasos para obtenerla:

1. Visita la página de registro de Together: [https://api.together.ai/](https://api.together.ai/)
2. Crea una cuenta o inicia sesión si ya tienes una.
3. Una vez en tu dashboard, busca la sección para generar una nueva API key.
4. Copia la API key generada y pégala en tu archivo `.env` como se indica en la sección de instalación.

Recuerda mantener tu API key segura y no compartirla públicamente.


## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para mejoras o correcciones.


## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).

---


¡Disfruta explorando Mixture of Agents! Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue.
