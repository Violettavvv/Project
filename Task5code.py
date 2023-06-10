import yaml

produkty = {
    'nazwa': 'Produkt 1',
    'cena': 7.99,
    'kategoria': ['słodycze', 'pieczywo']
}

with open('plik.yml', 'w') as file:
    yaml.dump(data, file)
