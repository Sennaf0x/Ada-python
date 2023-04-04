
dicionario = dict()

dicionario = {'nome':'Paulo', 'idade': 32, 'altura': 1.81}
print(dicionario)
print(dicionario['nome'])

dicionario['Sobrenome'] = 'Senna'
print(dicionario)

for variavel in dicionario:
    print(variavel, dicionario[variavel])

print('peso' in dicionario)
print('idade' in dicionario)

