lista = []

for i in range(3):
    nomes = str(input('Digite os tres nomes que deseja: '))
    lista.append(nomes)

print(f'Nomes digitados: {lista}')
substituta = input('Digite a palavra que voce deseja substituir: ')

if substituta in lista:
    novo_nome = input('Digite o nome que voce deseja que substitua o antigo: ')
    lista.remove(substituta)
    lista.append(novo_nome)
else:
    print('Nome inexistente!')

tupla = tuple(lista)
print(f'Atualização: {tupla}')