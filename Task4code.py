import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print("Błąd wczytywania pliku YAML:", e)

file_path = 'C:/laboratoriumy Git Bash/lab6,7,8(projekt)/plik4.yml'
data = load_yaml(file_path)

if data is not None:
    print("Plik YAML jest poprawny")
else:
    print("Plik YAML ma niepoprawną składnię.")
