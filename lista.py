
lista = ['Paulo', 32,'Casado', 'Manaus']
for i in range(len(lista)):
    print(lista[i])


lista.append('Amazonas')
print('Lista após append', lista)

lista.insert(1,'Senna')
print('Lista após insert', lista)

lista2 = [1,50,56,25]
lista.extend(lista2)
print('Lista após o extend', lista)

lista.pop()
print('Lista após o pop', lista)

lista.remove('Senna')
print('Lista após o remove', lista)

lista.append('Amazonas')
print("Quantidade de Amazonas dentro da lista: ", lista.count('Amazonas'))
lista.pop()

print('Indice do elemento 5 = ', lista.index('Paulo'))

print("O tamanho da sua lista é de: ", len(lista))

print('Antes do sort:', lista2)
lista2.sort()
lista2.sort(reverse=True)
print(lista2)
print("Somatório de lista:", sum(lista2))
print("Máximo da lista:", max(lista2))
print("Mínimo da lista:", min(lista2))


