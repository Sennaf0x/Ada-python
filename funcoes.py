"""def saudacao(nome, curso):
    print(f'Seja bem-vindo(a) {nome}!')
    print(f'Olá, é um prazer ter você conosco no curso de {curso}')
    
saudacao('Paulo', 'Python')"""

#Retorno

"""def soma(n1, n2):
    return n1 + n2

resultado = soma(5,7)

print(f'O resultado da soma é {resultado}.')"""

def calculadora(n1, n2, operacao='+'):
    if operacao == '+':
        return n1 + n2
    elif operacao == '-':
        return n1 - n2
    elif operacao == '*':
        return n1 * n2
    if operacao == '/':
        return n1 / n2
    else:
        print('Não e um operador (+, -, *, /)')

resultado = calculadora(5, 7, '*')

print(resultado)
