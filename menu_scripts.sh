#!/bin/bash

# Define la ruta completa a tu script organizador.
# Asegúrate de reemplazar "tu_usuario" con tu nombre de usuario real.
RUTA_ORGANIZADOR="/home/aparilli/organizador.py"

# Bucle principal para mostrar el menú
while true; do
    clear
    echo "==================================="
    echo "      Gestor de Scripts Personalizados"
    echo "==================================="
    echo "1. Organizar Carpeta de Descargas"
    echo "2. Otra Opción (ej. Limpiar Escritorio)"
    echo "3. Salir"
    echo "==================================="

    # Leer la opción del usuario
    read -p "Introduce tu opción: " opcion

    # Evaluar la opción seleccionada
    case $opcion in
        1)
            echo "Ejecutando el script de organización..."
            # Llama al script de Python con el intérprete python3
            python3 "$RUTA_ORGANIZADOR"
            echo "Script de organización finalizado. Presiona Enter para continuar."
            read -r
            ;;
        2)
            echo "Esta opción no está configurada. Presiona Enter para continuar."
            read -r
            ;;
        3)
            echo "Saliendo del Gestor de Scripts. ¡Adiós!"
            exit 0
            ;;
        *)
            echo "Opción no válida. Por favor, selecciona una opción del 1 al 3."
            echo "Presiona Enter para continuar."
            read -r
            ;;
    esac
done
