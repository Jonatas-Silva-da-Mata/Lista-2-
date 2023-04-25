tamanho = int(input('Escolha o tamanho do vetor: '))
dicionario = {}

for i in range(tamanho):
    chave = input('Digite a chave que deseja: ')
    valor = input('Digita o valor que deseja: ')
    dicionario[chave] = valor

print(dicionario)
