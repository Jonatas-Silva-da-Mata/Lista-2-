lista = []

for i in range(5):
    numero = int(input('Digite 5 números que deseja fazer uma lista: '))
    lista.append(numero)

print(f'Lista de numeros digitados: {lista}')

numero2 = int(input('Digite mais um número: '))

print(f'Lista de numeros atualizadas: {lista, numero2}')
    
