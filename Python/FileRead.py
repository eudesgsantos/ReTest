import json
x = input('ID: ')
d = {}
with open('data_file.json', 'r+') as f:
   data = json.load(f)

if x in data:
    y = input('Gostaria de ver seu histórico?')
    if y == 'sim':
        print(data[x])

else:
    print('Nenhum report registrado')
