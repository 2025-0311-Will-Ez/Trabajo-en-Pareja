import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

libros = soup.select(".product_pod")

data = []

for libro in libros:
    title = libro.h3.a["title"]
    price = libro.select_one(" .price_color ").text
    availability = libro.select_one(" .instock.availability ").text.strip()

    data.append([title, price, availability])

# Guardar muestra
with open("muestra_libros.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Título", "Precio", "Disponibilidad"])
    writer.writerows(data)

print("Scraping completado. Muestra guardada en 'muestra_libros.csv'")
