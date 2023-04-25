conjunto = set()

for i in range(10):
    numeros = int(input('Digite 10 numeros: '))
    conjunto.add(numeros)

print(conjunto)

if numeros % 2 == 0:
    conjunto.remove(numeros)

print(conjunto)
