import json

data = {
    "imie": "Violetta",
    "nazwisko": "Volodina",
    "wiek": 18,
    "adres": {
        "ulica": "Kwiatkowa 16",
        "miasto": "Wroclaw",
    },
    "telefon": ["123456789"]
}

with open("mojeDane.json", "w") as json_file:
    json.dump(data, json_file)
