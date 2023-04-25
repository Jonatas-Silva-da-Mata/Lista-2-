lista = []
lista_mult = []

for i in range(10):
    numeros = int(input('Digite 10 números: '))
    lista.append(numeros)

print(f'Numeros digitados: {lista}')

for numeros in lista:
    lista_mult.append(numeros*2)

print(f'Numeros digitados anteriomente multiplicado por 2: {lista_mult}')