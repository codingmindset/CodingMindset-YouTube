# LLama-Agents

Este repositorio contiene un sistema multi-agente utilizando agentes configurados con el nuevo framework de Llama-Index especial para la creación de agentes y por otro lado OpenAI como porveedor del servicio de LLMs, accesible a través de una interfaz de red.

## Descripción

Esta una aplicación diseñada para proporcionar información sobre el clima y titulares de noticias a través de un sistema multi-agente. Utiliza la API de OpenWeatherMap para obtener datos meteorológicos y se integra con el modelo de lenguaje de OpenAI para generar y gestionar las respuestas. El sistema de noticias NO está implementado.

## Requisitos

- Python 3.10 o superior
- Poetry para la gestión de dependencias

## Instalación

1. **Instala las dependencias:**

   ```bash
   poetry install
   ```

2. **Configura las variables de entorno:**

   - Renombra el archivo `template.env` a `.env`:
     ```bash
     cp template.env .env
     ```

   - Abre `.env` y añade tu API key de OpenWeatherMap y OpenAI:
     ```env
     OPENWEATHERMAP_API_KEY=your_api_key_here
     OPENAI_API_KEY=your_api_key_here
     ```

   Puedes obtener una clave API gratuita registrándote en [OpenWeatherMap](https://home.openweathermap.org/users/sign_up target="_blank").

## Uso

Para ejecutar la aplicación:

```bash
poetry run python llama_agents_ms.py
```

Para lanzar la GUI:

```bash
llama-agents monitor --control-plane-url http://127.0.0.1:8000
```

## Funcionalidades

- **Servicio Meteorológico:** Proporciona información actualizada del clima para cualquier ciudad utilizando la API de OpenWeatherMap.
- **Titulares de Noticias:** Genera titulares de noticias actuales utilizando el modelo de lenguaje de OpenAI.
- **Interacción Humana:** Configura un servicio que puede recibir y manejar consultas generales.

## Tutorial

Puedes ver el tutorial completo y el análisis de LLama-agents aquí 👉🏼 [Tutorial de LLama-agents](https://youtu.be/tk6bJaj3qV4 target="_blank").

## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para mejoras o correcciones.

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).

---

## Template `.env`

Asegúrate de crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
OPENWEATHERMAP_API_KEY=your_api_key_here
OPENAI_API_KEY=your_api_key_here
```

---

¡Disfruta usando LLama-agents! Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue.
