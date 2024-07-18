# Guía para Contribuir

¡Gracias por tu interés en contribuir al repositorio de CodingMindset! Aquí te explicamos cómo puedes colaborar de manera efectiva.

## Cómo Empezar

1. **Fork el Repositorio:**
   Haz un fork de este repositorio para crear una copia en tu cuenta de GitHub.

2. **Clona tu Fork:**
   Clona tu fork a tu máquina local.
   ```sh
   git clone https://github.com/tu-usuario/CodingMindset-YouTube.git
   ```

3. **Configura el Repositorio Remoto:**
   Añade el repositorio original como un remoto llamado `upstream`.
   ```sh
   cd CodingMindset-YouTube
   git remote add upstream https://github.com/CodingMindset/CodingMindset-YouTube.git
   ```

## Haciendo Contribuciones

1. **Sincroniza tu Fork:**
   Asegúrate de que tu fork esté actualizado con la rama `main` del repositorio original.
   ```sh
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Crea una Rama para tu Cambio:**
   Crea una rama nueva para trabajar en tu contribución.
   ```sh
   git checkout -b nombre-de-tu-rama
   ```

3. **Realiza tus Cambios:**
   Haz las modificaciones necesarias en tu rama.

4. **Añade y Commitea tus Cambios:**
   Añade tus cambios al índice y crea un commit descriptivo.
   ```sh
   git add .
   git commit -m "Descripción detallada de tus cambios"
   ```

5. **Sube tus Cambios a GitHub:**
   Sube tu rama a tu fork en GitHub.
   ```sh
   git push origin nombre-de-tu-rama
   ```

6. **Crea un Pull Request:**
   Desde tu repositorio fork en GitHub, abre un pull request hacia el repositorio original en la rama `main`.

## Recomendaciones para los Pull Requests

- Asegúrate de que tu código sigue las normas de estilo del proyecto.
- Añade pruebas si estás agregando nuevas características.
- Actualiza la documentación según sea necesario.
- Revisa tus cambios para evitar errores.

## Reportar Errores

Si encuentras un error, por favor abre un issue en GitHub e incluye la siguiente información:

- Descripción del error.
- Pasos para reproducirlo.
- Entorno en el que ocurre (sistema operativo, versiones de software, etc.).

## Solicitudes de Nuevas Características

Si tienes ideas para nuevas características, nos encantaría escucharlas. Por favor, abre un issue en GitHub describiendo la característica y cómo beneficiaría al proyecto.

## Código de Conducta

Para garantizar una comunidad acogedora y respetuosa, todos los contribuyentes deben seguir nuestro [Código de Conducta](CODE_OF_CONDUCT.md).

## Gracias

¡Gracias por tu interés en contribuir! Tu ayuda es muy valiosa para nosotros y para toda la comunidad de CodingMindset.
