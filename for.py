soma = 0

for i in range(1,4):
    nota = int(input(f'Digite sua nota n° {i}: '))
    soma = soma + nota
    
media = soma/i
print('Sua média final é de:', media)