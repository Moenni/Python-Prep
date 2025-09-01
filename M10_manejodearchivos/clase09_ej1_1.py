import sys
# Verificamos que se hayan ingresado exactamente 3 argumentos (sin contar el nombre del script)
if len(sys.argv)==4:
    print("Parametros recibidos:")
    print(f"Primer parametro: {sys.argv[1]}")
    print(f"Segundo parametro: {sys.argv[2]}")
    print(f"Tercer parametro: {sys.argv[3]}")
else:
    print("Error se deben ingresar 3 parametros")
    print("Ejemplo de uso: python clase09_ej1_1.py valor1,valor2,valor3")

    