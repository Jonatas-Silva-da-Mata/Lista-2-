tupla = ()

for i in range(5):
    numeros = int(input('Digite 5 numeros: '))
    tupla += (numeros,)

print(f'Primeiro elemento digitado: {tupla[0]}')