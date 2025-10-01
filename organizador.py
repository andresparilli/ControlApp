import os
import shutil
import time
from datetime import datetime, timedelta

# --- CONFIGURACIÓN ---
# Define la ruta a la carpeta que quieres organizar.
# La ~ es un atajo para tu carpeta de usuario.
carpeta_a_organizar = os.path.expanduser('~/Downloads')

# Define los directorios de destino.
# Se crearán automáticamente si no existen.
directorios_destino = {
    'Imágenes': ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.tiff', '.bmp', '.svg', '.raw'],
    'Documentos': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.ods'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm', '.avchd'],
    'Música': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma'],
    'Comprimidos': ['.zip', '.rar', '.7z', '.gz', '.tar', '.iso'],
    'Programas': ['.exe', '.sh', '.dmg', '.deb', '.rpm'],
    'CSV': ['.csv']
}

# Define la ruta para archivos sin categoría y el archivo a archivar
directorio_otros = os.path.join(carpeta_a_organizar, 'Otros')
directorio_archivo = os.path.join(carpeta_a_organizar, 'Archivo')

# Tiempo límite para el archivo (más de 1 año)
hace_un_anio = datetime.now() - timedelta(days=365)
# --- FIN DE LA CONFIGURACIÓN ---

import sys

def organizar_archivos():
    """Organiza los archivos de la carpeta de descargas."""
    print(f"Organizando la carpeta: {carpeta_a_organizar}")

    # Crear directorios de destino si no existen
    for carpeta in directorios_destino.keys():
        ruta_carpeta = os.path.join(carpeta_a_organizar, carpeta)
        os.makedirs(ruta_carpeta, exist_ok=True)
    os.makedirs(directorio_otros, exist_ok=True)
    os.makedirs(directorio_archivo, exist_ok=True)

    # Recorrer todos los archivos en la carpeta
    with os.scandir(carpeta_a_organizar) as entries:
        for entry in entries:
            if entry.is_file():
                # Obtener la fecha de modificación del archivo
                mod_time_stamp = os.path.getmtime(entry.path)
                mod_datetime = datetime.fromtimestamp(mod_time_stamp)

                # Si el archivo tiene más de 1 año, moverlo a Archivo
                if mod_datetime < hace_un_anio:
                    destino_path = os.path.join(directorio_archivo, entry.name)
                    shutil.move(entry.path, destino_path)
                    print(f"Archivado (más de 1 año): {entry.name}")
                    continue  # Pasa al siguiente archivo

                # Si no es un archivo antiguo, organizar por tipo
                nombre_archivo, extension = os.path.splitext(entry.name)
                extension_lower = extension.lower()
                
                encontrado = False
                for tipo, extensiones in directorios_destino.items():
                    if extension_lower in extensiones:
                        destino_path = os.path.join(carpeta_a_organizar, tipo, entry.name)
                        shutil.move(entry.path, destino_path)
                        print(f"Movido: {entry.name} -> {tipo}")
                        encontrado = True
                        break # Sal del bucle interno, ya encontramos la carpeta
                
                # Mover a la carpeta 'Otros' si no se encuentra un tipo coincidente
                if not encontrado and entry.name != 'organizador.py':
                    destino_path = os.path.join(directorio_otros, entry.name)
                    shutil.move(entry.path, destino_path)
                    print(f"Movido: {entry.name} -> Otros")

def eliminar_carpetas_vacias():
    """Elimina todas las carpetas vacías en el directorio de organización."""
    print(f"Buscando y eliminando carpetas vacías en: {carpeta_a_organizar}")
    carpetas_eliminadas = 0
    # Itera sobre todas las carpetas en el directorio
    for dirpath, dirnames, filenames in os.walk(carpeta_a_organizar, topdown=False):
        # No eliminar la carpeta raíz que estamos organizando
        if dirpath == carpeta_a_organizar:
            continue

        # Si la carpeta está vacía, la elimina
        if not dirnames and not filenames:
            try:
                os.rmdir(dirpath)
                print(f"Eliminada carpeta vacía: {dirpath}")
                carpetas_eliminadas += 1
            except OSError as e:
                print(f"Error al eliminar {dirpath}: {e}")

    if carpetas_eliminadas == 0:
        print("No se encontraron carpetas vacías.")
    else:
        print(f"Total de carpetas eliminadas: {carpetas_eliminadas}")

if __name__ == "__main__":
    # El primer argumento de la línea de comandos (sys.argv[1]) determina qué función ejecutar.
    if len(sys.argv) > 1:
        if sys.argv[1] == "organizar":
            organizar_archivos()
        elif sys.argv[1] == "limpiar":
            eliminar_carpetas_vacias()
        else:
            print(f"Argumento no reconocido: {sys.argv[1]}")
            print("Uso: python organizador.py [organizar|limpiar]")
    else:
        # Comportamiento predeterminado si no se proporcionan argumentos
        organizar_archivos()
