import requests
from bs4 import BeautifulSoup

with open ("index.html", 'r', encoding="utf-8") as file:
    soup = BeautifulSoup(file, 'html.parser')

titre = soup.title.text
print(f"Titre de la page : {titre}\n")

titre_principale = soup.find(id="titre").text
print(f"Titre principale de la page : {titre_principale}\n")

produits = {}

products = soup.select("li.product")
for element in products:
    nom = element.find("h2").text
    prix_euro = element.find("p", class_= "price").text.split(" ")
    description = element.find("p",class_ = None).text.replace("Description : ", "")
    produits[nom]={"Prix" : prix_euro[1], "Description" : description}
print(f"Tous les produits en euro : {produits}\n")
for clé in produits:
    euro = produits[clé]["Prix"]
    prix = euro.strip("€")
    prix = float(prix)
    dollar = prix * 1.2
    produits[clé]["Prix"] = f"{dollar}$"

print(f"Tous les produits en dollar : {produits}")