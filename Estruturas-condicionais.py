"""
    
idade = int(input('Digite a sua idade: '))

if idade >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')
    
"""

media = float(input('Digite a sua média final: '))
presenca = float(input('Digite a sua presença: '))

if media >= 7 and presenca >= 75 :
    print('Você foi aprovado(a)! ')
elif media >=5 and presenca >=50 :
    print('Você está de recuperação!')
elif media < 5 or presenca < 50 :
    print('Você foi reprovado!')