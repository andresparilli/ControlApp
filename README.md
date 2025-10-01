# Gestor de Scripts Personalizados

Este proyecto proporciona un menú de terminal para ejecutar y gestionar una colección de scripts de utilidad. Actualmente, incluye un potente script para organizar archivos y funcionalidades para administrar tareas programadas con cron.

## Características

- **Menú Interactivo**: Una interfaz de línea de comandos fácil de usar para acceder a todas las funcionalidades.
- **Organizador de Archivos**: Un script de Python que organiza los archivos en tu carpeta de `Descargas` (o cualquier otra que configures) en subcarpetas según su tipo (Imágenes, Documentos, etc.). También archiva ficheros con más de un año de antigüedad.
- **Gestor de Cron**: Permite visualizar, editar y programar la ejecución automática del script organizador.
- **Limpieza de Carpetas**: Incluye una función para eliminar directorios vacíos en la carpeta gestionada.

## Instalación

1. **Clona o descarga el repositorio** en tu directorio de preferencia (ej. `~/ControlApp`).

2. **Otorga permisos de ejecución** al script del menú:
   ```bash
   chmod +x menu_scripts.sh
   ```

3. **Crea un lanzador de escritorio** (opcional pero recomendado):
   - Copia el archivo `gestor-scripts.desktop` a `~/.local/share/applications/`.
   - Asegúrate de que la ruta en la línea `Exec=` del archivo `.desktop` coincide con la ubicación de `menu_scripts.sh`.
   ```bash
   cp gestor-scripts.desktop ~/.local/share/applications/
   ```
   Ahora deberías poder encontrar "Control App" en el menú de aplicaciones de tu sistema.

## Uso

Para iniciar el gestor, puedes:
- Hacer clic en el lanzador "Control App" desde tu menú de aplicaciones.
- Ejecutar el script directamente en una terminal:
  ```bash
  ./menu_scripts.sh
  ```

### Opciones del Menú

- **Organizar Carpeta**: Ejecuta el script `organizador.py` para clasificar los archivos.
- **Limpiar Carpetas Vacías**: Elimina los subdirectorios que hayan quedado vacíos.
- **Gestionar Tarea Programada (Cron)**: Abre un submenú para:
    - **Ver Tarea Actual**: Muestra la configuración actual en `crontab` para el script.
    - **Editar Manualmente**: Abre `crontab -e` para una edición avanzada.
    - **Crear Tarea (Recomendado)**: Añade una entrada a `crontab` para que el organizador se ejecute diariamente a la medianoche.
    - **Eliminar Tarea**: Elimina la tarea programada del `crontab`.

## Configuración

### Script Organizador

Puedes personalizar el script `organizador.py` para adaptarlo a tus necesidades:
- `carpeta_a_organizar`: Cambia la ruta de la carpeta que quieres organizar.
- `directorios_destino`: Añade o modifica las categorías y las extensiones de archivo asociadas.
- `hace_un_anio`: Ajusta el tiempo límite para considerar un archivo como "antiguo".

### Script de Menú

Si cambias la ubicación de los scripts, asegúrate de actualizar la variable `RUTA_ORGANIZADOR` en `menu_scripts.sh`.