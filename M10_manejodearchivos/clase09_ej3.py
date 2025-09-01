import csv
import os

# Diccionario provisto
montañas = {
    'nombre': ['Everest','K2','Kanchenjunga','Lhotse','Makalu',
               'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
    'orden': [1,2,3,4,5,6,7,8,9,10],
    'cordillera': ['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya',
                   'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
    'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
             'Pakistán','Nepal'],
    'altura': [8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]
}
# Abrimos el archivo en modo escritura
with open("clase09_ej3.csv",mode="w",newline="",encoding="utf-8")as archivo:
    writer =csv.writer(archivo)

# Escribimos la primera fila con los nombres de las claves
        # Encabezado con formato especial
    encabezado = [
        "🏔️ Nombre de la montaña",
        "🔢 Orden de altura",
        "🗻 Cordillera",
        "🌍 País",
        "📏 Altura (m)"
    ]

    writer.writerow(encabezado)

# Determinamos la cantidad de elementos (asumimos que todas las listas tienen el mismo largo)
    cantidad= len(montañas['nombre'])

# Escribimos cada fila con los valores i-ésimos
    for i in range(cantidad):
        fila = [
            montañas['nombre'][i],
            montañas['orden'][i],
            montañas['cordillera'][i],
            montañas['pais'][i],
            montañas['altura'][i]
        ]
        writer.writerow(fila)
    
#Confirmación en consola
print("✅ Archivo clase09_ej3.csv creado correctamente.")



