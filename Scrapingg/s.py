import requests
from bs4 import BeautifulSoup
import csv

# Página que voy a usar para el scraping
url = "https://books.toscrape.com/"

# Hago la petición a la página
respuesta = requests.get(url)

# Paso el HTML al parser de BeautifulSoup
soup = BeautifulSoup(respuesta.text, "html.parser")

# Aquí busco todos los libros
libros = soup.find_all("article", class_="product_pod")

# Aquí voy guardando la info
datos = []

# Recorro los libros encontrados
for libro in libros:
    titulo = libro.h3.a["title"]
    precio = libro.find("p", class_="price_color").text
    disponibilidad = libro.find("p", class_="instock availability").text.strip()

    datos.append([titulo, precio, disponibilidad])

# Guardo la muestra en un archivo CSV
with open("muestra_libros.csv", "w", newline="", encoding="utf-8") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Título", "Precio", "Disponibilidad"])
    writer.writerows(datos)

print("Scraping listo. Se creó el archivo muestra_libros.csv.")
