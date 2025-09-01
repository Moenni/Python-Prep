import sys
import csv
from datetime import datetime
# Verificamos que se hayan ingresado exactamente 3 argumentos

if len(sys.argv)!=4:
    print("Error: Se deben ingresar 3 parametros")
    sys.exit()
    
# Capturamos los argumentos
    
try:
    temperatura= float(sys.argv[1])
    humedad = int(sys.argv[2])
    llovio = sys.argv[3].lower()== "true"
except ValueError:
    print("Error: la temperatura debe ser float , humedad debe ser int, llovio debe ser true")
    sys.exit()

# Obtenemos la marca de tiempo actual
timestamp= datetime.now().strftime("%Y-%m-%d %H-%M-%S")

# Ruta del archivo CSV
archivo_csv = "clase09_ej2_1.csv"

# Escribimos en el archivo
with open(archivo_csv,mode="a",newline="")as archivo:
    writer=csv.writer(archivo)
    writer.writerow([timestamp, temperatura,humedad,llovio])
    

print("✅ Datos registrados correctamente:")
print(f"🕒 Tiempo: {timestamp}")
print(f"🌡️ Temperatura: {temperatura} °C")
print(f"💧 Humedad: {humedad} %")
print(f"🌧️ Llovió: {llovio}")


    