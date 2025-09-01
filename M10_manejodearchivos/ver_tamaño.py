import os

# Ruta del archivo
archivo= "clase09_ej3.csv"

# Obtener el tamaño en bytes
tamaño_bytes= os.path.getsize(archivo)

# Convertir a megabytes (1 MB = 1024 * 1024 bytes)
tamaño_mb= tamaño_bytes/(1024*1024)

# Mostrar el resultado con 4 decimales
print(f"📦 Tamaño del archivo '{archivo}': {tamaño_mb:.4f} MB")


