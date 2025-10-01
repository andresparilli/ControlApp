#!/bin/bash

# Define la ruta completa a tu script organizador.
# Asegúrate de reemplazar "tu_usuario" con tu nombre de usuario real.
RUTA_ORGANIZADOR="/home/aparilli/organizador.py"

# --- FUNCIONES PARA GESTIONAR CRON ---

# Función para mostrar el submenú de Cron
mostrar_menu_cron() {
    while true; do
        clear
        echo "==================================="
        echo "  Gestionar Tarea Programada (Cron)"
        echo "==================================="
        echo "1. Ver Tarea Actual para Organizador"
        echo "2. Editar Crontab Manualmente"
        echo "3. Crear Tarea Predeterminada (Diaria a medianoche)"
        echo "4. Eliminar Tarea del Organizador"
        echo "5. Volver al Menú Principal"
        echo "==================================="
        read -p "Introduce tu opción: " opcion_cron

        case $opcion_cron in
            1)
                echo "Buscando tarea programada..."
                # Muestra las líneas de crontab que contienen la ruta del script
                crontab -l | grep "$RUTA_ORGANIZADOR" || echo "No se encontró ninguna tarea programada para este script."
                read -p "Presiona Enter para continuar."
                ;;
            2)
                echo "Abriendo el editor de crontab..."
                # Abre el editor de crontab. El usuario usará su editor predeterminado.
                crontab -e
                ;;
            3)
                echo "Creando tarea programada..."
                # Tarea: ejecutar el script todos los días a las 00:00
                TAREA_CRON="0 0 * * * /usr/bin/python3 $RUTA_ORGANIZADOR"
                # Añade la tarea sin duplicarla si ya existe
                (crontab -l 2>/dev/null | grep -Fv "$RUTA_ORGANIZADOR" ; echo "$TAREA_CRON") | crontab -
                echo "¡Tarea creada! El organizador se ejecutará todos los días a medianoche."
                read -p "Presiona Enter para continuar."
                ;;
            4)
                echo "Eliminando tarea programada..."
                # Elimina todas las tareas que ejecuten el script organizador
                crontab -l 2>/dev/null | grep -Fv "$RUTA_ORGANIZADOR" | crontab -
                echo "Tarea eliminada."
                read -p "Presiona Enter para continuar."
                ;;
            5)
                # Sale de este submenú y vuelve al bucle principal
                return
                ;;
            *)
                echo "Opción no válida. Presiona Enter para continuar."
                read -r
                ;;
        esac
    done
}

# --- BUCLE PRINCIPAL DEL MENÚ ---
while true; do
    clear
    echo "==================================="
    echo "      Gestor de Scripts Personalizados"
    echo "==================================="
    echo "1. Organizar Carpeta de Descargas"
    echo "2. Limpiar Carpetas Vacías"
    echo "3. Gestionar Tarea Programada (Cron)"
    echo "4. Salir"
    echo "==================================="

    read -p "Introduce tu opción: " opcion

    case $opcion in
        1)
            echo "Ejecutando el script de organización..."
            # Llama al script de Python con el argumento "organizar"
            python3 "$RUTA_ORGANIZADOR" organizar
            echo "Script de organización finalizado. Presiona Enter para continuar."
            read -r
            ;;
        2)
            echo "Ejecutando la limpieza de carpetas vacías..."
            # Llama al script de Python con el argumento "limpiar"
            python3 "$RUTA_ORGANIZADOR" limpiar
            echo "Limpieza finalizada. Presiona Enter para continuar."
            read -r
            ;;
        3)
            # Llama a la función que muestra el menú de cron
            mostrar_menu_cron
            ;;
        4)
            echo "Saliendo del Gestor de Scripts. ¡Adiós!"
            exit 0
            ;;
        *)
            echo "Opción no válida. Por favor, selecciona una opción del 1 al 4."
            echo "Presiona Enter para continuar."
            read -r
            ;;
    esac
done
