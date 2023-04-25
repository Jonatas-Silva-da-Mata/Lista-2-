grafo = {}
num_vertices = int(input('Digite o numero de vertices: '))

for i in range(num_vertices):
    vertice = input('Digite o nome do vertice: ')
    grafo[vertice] = []

num_arestas = int(input('Digite o numero de arestas: '))

for i in range(num_arestas):
    valor_origem, valor_final = input('Digite dois valores: ').split()
    grafo[valor_origem] = valor_final
    grafo[valor_final] = valor_origem

remocao = input('Escolha quem deseja remover: ')
valor_origem, valor_final = remocao.split()

if valor_origem in grafo and valor_final in grafo:
    if valor_final in grafo[valor_origem]:
        grafo[valor_origem].remove(valor_final)
        grafo[valor_final].remove(valor_origem)
        print(grafo)
    else:
         print('Nao existe essa aresta.')
else:
    print('Esse vertice nao existe.')
   


