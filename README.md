# Listar-extensiones

Este script de Python permite encontrar y listar todas las extensiones de archivos en un directorio dado, sin duplicados. Es especialmente útil para analizar el contenido de carpetas y entender qué tipos de archivos contiene.

## Cómo funciona

El script utiliza el módulo `os` para recorrer recursivamente un directorio y sus subdirectorios, identificando las extensiones de los archivos. Para evitar duplicados, las extensiones se almacenan en un conjunto (`set`). Además, las extensiones se convierten a minúsculas para manejar posibles inconsistencias entre mayúsculas y minúsculas.

## Requisitos

- Python 3.6 o superior.

## Uso

1. Clona o descarga este repositorio.
2. Abre el archivo `script.py` en tu editor de texto o entorno de desarrollo integrado (IDE) favorito.
3. Modifica la variable `ruta_carpeta` para que apunte al directorio que deseas analizar.
   ```python
   ruta_carpeta = r'C:\Users\TuUsuario\Carpeta'
4. Ejecuta el script desde la línea de comandos o el IDE.
5. Verás en pantalla una lista de todas las extensiones encontradas ordenadas alfabéticamente.