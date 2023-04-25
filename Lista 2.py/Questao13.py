tamanho = int(input('Digite o tamanho do vetor: '))
dicionario = {}

for i in range(tamanho):
    chave = input('Digite a chave que deseja: ')
    valor = input('Digite o valor dessa chave: 1')
    dicionario[chave] = valor

if 'Profissao' in dicionario:
    print(f'A chave Profissao está existente {dicionario["Profissao"]}.')
else: 
    print('A chave Profissao está inexistente.')