# importar libreria CSV para manejar archivos CSV
import csv

#Leer los datos del archivo csv
with open('videos.csv', 'r') as file:
    reader = csv.DictReader(file)
    videos = list(reader)
    
# Encontrar el video más con la calificacion mas alta
mejor_video = max(videos, key=lambda x: float(x['Calificacion']))

#Imprimir el video con la calificacion mas alta
print("👌 Video Recomendado")
print(f"Nombre: {mejor_video['Video']}")
print(f"Calificacion: {mejor_video['Calificacion']}")