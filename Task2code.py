import json

def load_json_file(file_path):
    try:
        with open(file_path) as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Plik nie został znaleziony.")
    except json.JSONDecodeError as e:
        print("Błąd dekodowania pliku JSON:")
        print(e)

file_path = 'sciezka/do/pliku.json'
json_data = load_json_file(file_path)

if json_data is not None:
    print("Dane z pliku JSON zostały wczytane poprawnie.")
