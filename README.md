# Division de PDFs locales por página

Este proyecto consiste en una aplicación de escritorio desarrollada en Python para dividir archivos PDF en múltiples documentos, uno por cada página del original. La herramienta fue diseñada para funcionar completamente de forma local, sin necesidad de conexión a internet, con el objetivo de preservar la confidencialidad de los documentos procesados. Es especialmente útil en entornos clínicos o administrativos donde los archivos contienen información sensible y no deben subirse a servicios en la nube.

## Descripción general

El usuario selecciona un archivo PDF desde su equipo mediante una interfaz gráfica simple. La aplicación divide automáticamente el PDF en tantas páginas como contenga, generando un nuevo archivo PDF por cada página en una carpeta separada.

## Funcionalidades

- Interfaz gráfica de selección de archivo mediante tkinter
- División automática de PDFs multipágina
- Guardado de los archivos individuales en una carpeta local
- Manejo básico de errores si el archivo no existe

## Requisitos

El proyecto requiere las siguientes dependencias:

- PyPDF2
- tkinter (incluido por defecto en instalaciones estándar de Python)

Estas pueden instalarse con:

pip install PyPDF2

## Estructura del proyecto

La estructura básica del proyecto es la siguiente:

tu_proyecto/
  main.py              -> Código principal
  README.md            -> Descripción del proyecto

## Ejecución

1. Ejecutar el archivo main.py
2. Se abrirá una ventana para seleccionar un archivo PDF
3. El programa creará una carpeta llamada paginas_separadas junto al archivo original y guardará allí los nuevos PDFs divididos

## Autor

Desarrollado por Diego Vallina Álvarez, estudiante de cuarto curso del Grado en Ingeniería de la Salud en la Universidad de Burgos (UBU), durante su periodo de prácticas en el Hospital Universitario de Burgos. Fecha: 31/03/2025

Contacto: diego25codema@gmail.com
