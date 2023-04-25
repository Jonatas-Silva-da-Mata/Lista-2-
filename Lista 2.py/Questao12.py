tupla = ()

for i in range(3):
    nomes = str(input('Digite tres nomes: '))
    tupla += (nomes,)

print(f'Nomes digitados: {tupla}')

if 'Maria' in tupla:
    print('O nome "Maria" foi digitado.')
else:
    print('O nome "Maria" não foi digitado.')