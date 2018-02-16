# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script qui permet de faire un peu
de web scraping.
"""

import bs4
import requests

# Récupérer la page web
url = 'http://www.boursorama.com/taux-de-change-euro-dollar-eur-usd'
maRequete = requests.get(url)

if( maRequete.status_code != 200 ):
    print("Erreur lors de la récupération. Code d'erreur :", maRequete.status_code)
    exit(1)

print(maRequete.url)
# Le contenu de la page est dans maRequete.text

# Analyser la page web avec BS4
soupe = bs4.BeautifulSoup(maRequete.text, "lxml")

soupe2 = soupe.find('div', attrs={'id': 'fiche_cours_details'})
conversion = soupe2.find('table').find('tr').findAll('td')[1].find('b').find('span').text

# Afficher la valeur de la conversion Euro/Dollar
print(conversion)
