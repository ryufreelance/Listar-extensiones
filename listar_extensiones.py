import os

def encontrar_extensiones(ruta):
    extensiones = set()  # Usamos un conjunto para evitar duplicados

    for carpeta_actual, subcarpetas, archivos in os.walk(ruta):
        for archivo in archivos:
            # Usamos guion bajo como una variable temporal que no será utilizada posteriormente
            # Obtenemos la extensión del archivo
            _, extension = os.path.splitext(archivo)
            if extension:  # Nos aseguramos de que tiene extensión
                extensiones.add(extension.lower())  # Convertimos a minúsculas para evitar duplicados por mayúsculas/minúsculas

    return extensiones

# Ejemplo de uso
ruta_carpeta = r'C:\Users\TuUsuario\Carpeta'
extensiones_encontradas = encontrar_extensiones(ruta_carpeta)

# Mostramos las extensiones en pantalla
print("Extensiones de archivo encontradas:")
for extension in sorted(extensiones_encontradas):  # Ordenamos alfabéticamente
    print(extension)
