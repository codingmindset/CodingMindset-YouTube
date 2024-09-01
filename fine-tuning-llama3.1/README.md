# Fine-Tuning Llama 3.1 8B LoRA con Unsloth

Este repositorio contiene el código y las instrucciones para realizar fine-tuning del modelo Llama 3.1 8B utilizando LoRA (Low-Rank Adaptation) y la biblioteca Unsloth. Este tutorial está basado en un video de YouTube que muestra paso a paso cómo implementar estas técnicas avanzadas de ajuste de modelos de lenguaje.

## Descripción

Este proyecto demuestra cómo utilizar técnicas de fine-tuning eficientes en términos de recursos para mejorar el rendimiento de modelos de lenguaje de gran escala. Utilizamos LoRA para adaptar el modelo Llama 3.1 8B de manera eficiente, y aprovechamos las optimizaciones proporcionadas por Unsloth para acelerar el proceso de entrenamiento.

## Tutorial en Video

Puedes ver el tutorial completo y la explicación detallada del proceso de fine-tuning aquí 👇🏽👇🏽:

[![Watch this video on YouTube](https://img.youtube.com/vi/--l1HXN6gXc/0.jpg)](https://www.youtube.com/watch?v=--l1HXN6gXc)

## Requisitos

- Python 3.8 o superior
- CUDA compatible GPU (recomendado)
- Dependencias listadas en el notebook

## Instalación

1. **Clonar el repositorio:**
   ```bash
   gh repo clone codingmindset/CodingMindset-YouTube
   cd fine-tuning-llama3.1
   ```

2. **Instalar dependencias:**
Instala las dependencias siguiendo las instrucciones del notebook


## Uso

El notebook principal `CodingMindset_Fine_Tuning_con_Unsloth.ipynb` contiene todo el código necesario para realizar el fine-tuning. Sigue estos pasos:

1. Abre el notebook en Google Colab o en tu entorno local con Jupyter.
2. Ejecuta las celdas en orden, siguiendo las instrucciones y comentarios proporcionados.
3. Ajusta los hiperparámetros según tus necesidades específicas.

## Características Principales

- Fine-tuning de Llama 3.1 8B usando QLoRA
- Utilización de Unsloth para optimización de rendimiento
- Soporte para diferentes configuraciones de cuantización
- Guardado y carga de modelos en formatos eficientes (LoRA, merged_16bit, merged_4bit)
- Conversión a formato GGUF para compatibilidad con diversos motores de inferencia

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para sugerencias de mejoras o correcciones.

## Licencia

Este proyecto está bajo la licencia [insertar tipo de licencia].

---

## Redes Sociales

Sígueme en mis redes sociales para más contenido sobre IA y programación:

- Twitter: [@codingmindsetio](https://twitter.com/codingmindsetio)
- YouTube: [CodingMindset](https://www.youtube.com/@CodingMindsetIO?sub_confirmation=1)
- Instagram: [@codingmindset](https://www.instagram.com/codingmindset)

¡No olvides dejar tu like y comentario en el video si te ha sido útil! Tu apoyo me ayuda a seguir creando contenido educativo de calidad.