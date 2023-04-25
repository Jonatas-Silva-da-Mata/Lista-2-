grafo  = {}

vertice  =  int ( input ( 'Digite a quantidade de vértices: ' ))

for  i  in  range(vertice):
    vertice  =  input( f'{ i  +  1 } º vértice: ' )
    grafo [vertice] = []
    
quant_arestas  =  int ( input ( 'Quantidade de arestas: ' ))

for  i  in  range( quant_arestas ):
    valor_origem , valor_destino  =  input ( 'Arestas: ' ).split()
    grafo [valor_origem] =  valor_destino
    grafo [valor_origem] =  valor_destino

print(grafo)