
# Mistral Coding Assistant

Este repositorio contiene un asistente de codificación utilizando el modelo Codestral Mamba de Mistral, accesible a través de una interfaz de Gradio.

## Descripción

El Mistral Coding Assistant permite obtener ayuda y consejos de programación del modelo Codestral Mamba. Puedes hacer preguntas sobre programación o enviar fragmentos de código y recibir asistencia.

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

   - Abre `.env` y añade tu API key de Mistral:
     ```env
     MISTRAL_API_KEY=your_api_key_here
     ```

## Uso

Para ejecutar la aplicación:

```bash
poetry run python codestral.py
```

## Funcionalidades

- **Interfaz de Usuario:** Utiliza Gradio para interactuar con el modelo Codestral Mamba.
- **Asistente de Codificación:** Pregunta sobre problemas de programación y recibe respuestas generadas por el modelo.

## Tutorial

Puedes ver el tutorial completo y el análisis de Codestral aquí 👉🏼 [🤯 REVOLUCIÓN en la Programación! Conoce Codestral Mamba 🔥🐍 el Nuevo modelo Open Source](https://youtu.be/e9-6NUOiY5E).

## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para mejoras o correcciones.

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).

---

## Template `.env`

Asegúrate de crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
MISTRAL_API_KEY=your_api_key_here
```

---

¡Disfruta usando el Mistral Coding Assistant! Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue.

