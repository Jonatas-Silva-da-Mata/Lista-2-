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

print(grafo[vertice])
