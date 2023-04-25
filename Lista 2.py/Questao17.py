from tokenize import Triple


lista = []

for i in range(3):
    nomes = str(input('Digite tres nomes: '))
    lista.append(nomes)

tupla = tuple(lista)
print(f'Nomes digitados: {tupla}')
print(f"Quantidade de vezes que a palavra 'Maria' aparece: {tupla.count('Maria')}")