import json

data = {
    "Imie": "Violetta",
    "Nazwisko": "Volodina",
    "Wiek": 18,
    "Adres": {
        "Ulica": "Kwiatkowa 16",
        "Miasto": "Wroclaw",
    },
    "Telefon": ["123456789"]
}

with open("mojeDane.json", "w") as json_file:
    json.dump(data, json_file)
