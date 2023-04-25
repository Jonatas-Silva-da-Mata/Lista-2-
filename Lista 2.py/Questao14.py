conjunto = set()

for i in range(5):
    numeros = int(input('Digite 5 numeros: '))
    conjunto.add(numeros)

print(conjunto)

if 3 in conjunto:
    print('O numero 3 está presente.')
else:
    print('O numero 3 não está presente.')
