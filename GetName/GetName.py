import json
x = input('Seu e-mail: ')
d = {}
with open('banco_dados_branco.json', 'r+') as f:
   data = json.load(f)

if x in data:
    print(data[x])

else:
    print('Este e-mail não está registrado')

username = data[x]
