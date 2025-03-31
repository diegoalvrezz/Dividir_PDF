# Busqueda_Hospital_HUBU

Este proyecto ha sido desarrollado en el contexto de un entorno hospitalario con el objetivo de automatizar la extracción de información clínica contenida en informes médicos en formato PDF. La herramienta permite aplicar filtros diagnósticos específicos y generar bases de datos estructuradas en Excel para su posterior análisis o integración con sistemas externos.

Por motivos de confidencialidad, no se incluyen archivos de entrada, salida ni ejemplos de ejecución, ya que el código fue utilizado con información sensible de pacientes.

## Descripción general

La aplicación permite procesar documentos PDF multipágina, identificar aquellos informes que cumplan determinados criterios clínicos y extraer campos relevantes como el número de historia clínica, el número de muestra o biopsia, la procedencia anatómica, el diagnóstico y el resultado. Posteriormente, los datos se combinan con una base de datos externa en Excel para enriquecer la información extraída.

Todo el procesamiento se realiza de forma local, garantizando la privacidad y seguridad de los datos clínicos.

## Funcionalidades principales

### 1. Extracción de informes válidos desde un PDF

La función extraer_informes_pdf(pdf_path) analiza los documentos en busca de informes que contengan:

- Número de historia clínica (NHC)
- Número de muestra o biopsia
- Procedencia anatómica válida (ej. colon, sigma, recto, intestino grueso)
- Diagnóstico
- La frase clave: "NO SE DETECTA pérdida"

Solo los informes que cumplen con todos estos requisitos son extraídos.

### 2. Exportación de resultados

La función guardar_en_excel(datos, output_path) permite guardar los informes válidos en un archivo Excel para facilitar su revisión o tratamiento posterior.

### 3. Combinación con una base de datos externa

La función combinar_resultados(base_resultados, base_biobancbdd, output_final) realiza la unión de los resultados obtenidos con una base de datos externa (biobancbdd.xlsx) utilizando el campo NHC como clave de enlace. El resultado es un nuevo archivo Excel enriquecido con la información adicional.

## Requisitos

El entorno de ejecución requiere las siguientes dependencias, especificadas en el archivo requirements.txt:

- pandas
- PyMuPDF
- openpyxl
- unidecode

Estas pueden instalarse mediante:


pip install -r requirements.txt


## Estructura esperada del proyecto

```
tu_proyecto/
  archivo.pdf              -> Informe PDF original
  biobancbdd.xlsx          -> Base de datos externa
  resultados.xlsx          -> Resultados extraídos del PDF
  resultadosfinal.xlsx     -> Resultados combinados
  main.py                  -> Código principal
  README.md                -> Descripción del proyecto
  requirements.txt         -> Requisitos del entorno
```

## Estructura esperada de los documentos PDF

Los documentos PDF deben contener texto seleccionable (no imágenes escaneadas) y presentar una estructura coherente que permita identificar claramente los elementos clave: número de historia clínica, número de muestra, procedencia anatómica, diagnóstico y resultado. La aplicación ha sido diseñada para tolerar pequeñas variaciones en el formato del texto.

## Ejecución

1. Colocar los archivos archivo.pdf y biobancbdd.xlsx en la carpeta del proyecto.
2. Ejecutar el archivo main.py.
3. Se generarán los archivos Excel resultados.xlsx y resultadosfinal.xlsx con los datos procesados.

## Autor

Desarrollado por Diego Vallina Álvarez, estudiante de cuarto curso del Grado en Ingeniería de la Salud en la Universidad de Burgos (UBU), durante su periodo de prácticas en el Hospital Universitario de Burgos (Área de Anatomía Patológica) a fecha de 31/03/2025.

Contacto: diego25codema@gmail.com
