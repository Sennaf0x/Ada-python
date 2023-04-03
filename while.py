import random

print('Tente acertar o número sorteado em 5 tentativas!')

contador = 1
numero_sorteado = random.randint(1,20)

print('Tentativa n°', contador)
numero_escolhido = int(input('Digite um número entre 0 e 20: '))


if numero_escolhido > 20:
    print('Seu número é maior que 20, tente novamente!')
else:
    
    while numero_escolhido != numero_sorteado and contador <= 4:
        
        print('Você errou! Tente novamente!')
        contador = contador + 1
        print('Tentativa n°', contador)
        numero_escolhido = int(input('Digite outro número: '))
        

if contador >=4:
    print('Não lhe restam mais tentativas.')
else:
    print('Parabéns! O número sorteado era:', numero_sorteado) 
    print('Você acertou na tentativa n°', contador)
