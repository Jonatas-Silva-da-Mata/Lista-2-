conjunto = set()

for i in range(5):
    numeros = int(input('Digite o 5 numeros: '))
    conjunto.add(numeros)

print(conjunto)

remocao = int(input('Escolha um número que voce digitou para ser removido: '))

if remocao in conjunto:
    conjunto.remove(remocao)
else:
    print('Esse numero nao foi digitado.')

print(conjunto)
