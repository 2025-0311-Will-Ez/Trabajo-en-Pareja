#Proyecto-Scraping
#Es la técnica de extraer información de páginas web de forma automática mediante programas o bots, para luego organizarla y utilizarla en bases de datos u otros anális. Es como "copiar y pegar" grandes cantidades de datos de un sitio web, pero de forma programada y eficiente, en lugar de hacerlo manualmente. Se utiliza comúnmente para comparar precios, analizar datos de mercado o monitorear la competencia. En este caso se utilizó para ver la disponibilidad de algunos libros, para ver el precio y si ya están agotados.
#Willyn Ezequiel Pérez Hernández #2025-0311

import requests
from bs4 import BeautifulSoup
import csv

#Página que voy a usar para hacerle el Scraping
url = "https://books.toscrape.com/"

#Hago la petición a la página
respuesta = requests.get(url)

#Paso el HTML al parser de BeautifulSoup
soup = BeautifulSoup(respuesta.text, "html.parser")

#Aquí busco todos los libros
libros = soup.find_all("article", class_="product_pod")

#Aquí voy guardando la info
datos = []

#Recorro los libros encontrados
for libro in libros: 
    titulo = libro.h3.a["title"]
    precio = libro.find("p", class_="price_color").text
    disponibilidad = libro.find("p", class_="instock availability").text.strip()

    datos.append([ titulo, precio, disponibilidad ])

#Guardo la muestra en un archivo CSV
with open("muestra_libros.csv", "w", newline = "", encoding = "utf-8") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Título", "Precio", "Disponibilidad"])
    writer.writerows(datos)

print("Scraping listo. Se creó el archivo: muestra_libros.csv.")
