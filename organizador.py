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

if __name__ == "__main__":
    organizar_archivos()
