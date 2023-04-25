from pickle import DICT


tamanho = int(input('Digite o tamanho do vetor: '))
dicionario = {}

for i in range(tamanho):
    chave = input('Digite a chave que deseja: ')
    valor = input('Digite o valor que deseja: ')
    dicionario[chave] = valor

print(dicionario)