import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='Ścieżka do pliku wejściowego.')
parser.add_argument('--output', help='Ścieżka do pliku wyjściowego.')
args = parser.parse_args()

print('Input file:', args.input_file)
print('Output file:', args.output)
