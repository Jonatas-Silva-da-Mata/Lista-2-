lista = []

for i in range(10):
    numeros = int(input('Digite 10 numeros: '))
    lista.append(numeros)

for i in range(0, 10, 2):
    print(f'Numeros de posição de indices pares digitados: {lista[i]}')