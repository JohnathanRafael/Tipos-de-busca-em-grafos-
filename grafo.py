import networkx as grafo
import matplotlib.pyplot as plotar

rede = grafo.Graph()

PESO = 'Peso'
TRAJETO = 'Trajeto'
G1 = 'Serv 1'
G2 = 'Serv 2'
G3 = 'Serv 3'
G4 = 'Serv 4'
G5 = 'Serv 5'
G6 = 'Serv 6'
G7 = 'Serv 7'
G8 = 'Serv 8'
G9 = 'Serv 9'
G10 = 'Serv 10'

rede.add_node(G1)
rede.add_node(G2)
rede.add_node(G3)
rede.add_node(G4)
rede.add_node(G5)
rede.add_node(G6)
rede.add_node(G7)
rede.add_node(G8)
rede.add_node(G9)
rede.add_node(G10)

rede.add_edge(G1, G3, PESO = 500)
rede.add_edge(G1, G7, PESO = 400)
rede.add_edge(G1, G4, PESO = 600)

rede.add_edge(G2, G3, PESO = 900)
rede.add_edge(G2, G7, PESO = 1000)

rede.add_edge(G4, G8, PESO = 850)
rede.add_edge(G8, G5, PESO = 950)
rede.add_edge(G8, G10, PESO = 800)

rede.add_edge(G3, G8, PESO = 450)
rede.add_edge(G3, G10, PESO = 350)
rede.add_edge(G3, G9, PESO = 400)

rede.add_edge(G5, G6, PESO = 700)
rede.add_edge(G6, G10, PESO = 600)
rede.add_edge(G9, G10, PESO = 550)

#Busca em Largura
# A busca parte de um vertice fonte e procura um verticeBusca
def buscaLargura(verticeFonte, verticeBusca):
    retorno = []

    # uma tupla
    visitados = set()

    # uma lista
    fila = [verticeFonte]

    while fila:
        # remove o primeiro elemento da fila
        vertice = fila.pop(0)
        retorno.append(vertice)
        print(vertice)
        if vertice == verticeBusca:
            return retorno, 'VÉRTICE ENCONTRADO'

        # se ainda nao foi visitado
        if vertice not in visitados:
            visitados.add(vertice)

        # vizinhos do vertice
        for vizinho in rede[vertice]:

            # not in evita ir no mesmo lugar
            if vizinho not in visitados and vizinho not in fila:
                fila.append(vizinho)

        # mostra a busca funcionando corretamente

    return retorno, 'Vértice não encontrado'

#Busca em profundidade
# A busca parte de um vertice fonte e procura um verticeBusca
def buscaProfundidade(verticeFonte, verticeBusca):
    visitados = set()
    retorno = []

    def dfs_recursiva(vertice, verticePassado):
        visitados.add(vertice)
        retorno.append(vertice)
        print(vertice)
        if vertice == verticeBusca:
            return True

        for vizinho in rede[vertice]:
            if vizinho not in visitados:
                if dfs_recursiva(vizinho, verticePassado):# faz o teste para ver se o retorno e verdadeiro
                    return True

    if dfs_recursiva(verticeFonte, verticeBusca):
        return retorno, 'VÉRTICE ENCONTRADO'
    else:
        return retorno, 'Vértice não encontrado'


#adiciona Valores Baseado onde se quer chegar
def adicionarValores(nodeChegada):
    adicionar = 0

    visitados = set()
    fila = [nodeChegada]

    while fila:
        vertice = fila.pop(0)
        adicionar += 10
        rede.nodes[vertice][PESO] = adicionar
        if vertice not in visitados:
            visitados.add(vertice)

        for vizinho in rede[vertice]:
            if vizinho not in visitados and vizinho not in fila:
                fila.append(vizinho)

#busca Gulosa
# recebe um node de saida para chegada onde o node tiver peso 10
def buscaGulosa(nodeSaida):
    fila = [nodeSaida]
    retorno = []
    totalCaminho = 0
    while fila:
        menorPeso = float('inf')
        vertice = fila.pop(0)
        nodeMenor = None
        retorno.append(vertice)
        print(rede.nodes[vertice][PESO])
        for vizinho in rede[vertice]:
            peso = rede.nodes[vizinho][PESO]
            if peso < menorPeso:
                menorPeso = peso
                nodeMenor = vizinho
            if peso == 10:
                totalCaminho += (rede.nodes[vertice][PESO] - rede.nodes[nodeMenor][PESO]) / rede[vertice][nodeMenor]['PESO']
                retorno.append(vizinho)
                return retorno, totalCaminho
        totalCaminho += (rede.nodes[vertice][PESO] - rede.nodes[nodeMenor][PESO]) / rede[vertice][nodeMenor]['PESO']
        print(totalCaminho)
        fila.append(nodeMenor)
    return retorno, 0

#Faz uma relacao e vê qual caminho vai ser o mais rapido para trafegar a informacao

def buscaAEstrela(nodeSaida):
    fila = [nodeSaida]
    retorno = []
    pesoAcumulado = 0
    while fila:
        vertice = fila.pop(0)
        if rede.nodes[vertice][PESO] == 10:
            retorno.append(vertice)
            return retorno, pesoAcumulado
        menorRelacao = float('inf')
        nodeMenor = None
        retorno.append(vertice)
        print(rede.nodes[vertice][PESO])
        for vizinho in rede[vertice]:
            if rede.nodes[vizinho][PESO] < rede.nodes[vertice][PESO]:
                peso = (rede.nodes[vertice][PESO] - rede.nodes[vizinho][PESO]) / rede[vertice][vizinho]['PESO']
                print(peso)
                if peso < menorRelacao:
                    menorRelacao = peso
                    nodeMenor = vizinho
        pesoAcumulado += menorRelacao
        fila.append(nodeMenor)
    return retorno, 0

def plotarGrafo():
    pos = grafo.kamada_kawai_layout(rede)
    fig, ax = plotar.subplots()
    # Obter Arestas e Nodes com os pesos
    labelsArestas = {(u, v): d['PESO'] for u, v, d in rede.edges(data=True)}
    labelsNodes = {n: f"{n}\n{d[PESO]}" for n, d in rede.nodes(data=True)}

    grafo.draw_networkx_nodes(rede, pos, node_size=300, node_color='lightblue')
    grafo.draw_networkx_labels(rede, pos, labelsNodes, font_size=10, font_color='black')

    grafo.draw_networkx_edges(rede, pos)
    grafo.draw_networkx_edge_labels(rede, pos, edge_labels=labelsArestas)

    # Desativar os eixos
    ax.axis('off')

    # Mostrar o gráfico
    return fig