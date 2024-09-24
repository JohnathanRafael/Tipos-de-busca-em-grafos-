import tkinter as tk
import grafo
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def exibirJanela():
    janela = tk.Tk()
    janela.title("Inteligencia Artifical - Grafo Rede")
    frameBuscaLargura(janela)
    frameBuscaProfundidade(janela)
    frameBuscaGulosa(janela)
    frameBuscaAEstrela(janela)
    gerarGrafo(janela)
    grafo.adicionarValores(grafo.G7)
    plotarGrafo(janela)

    janela.mainloop()

def frameBuscaLargura(janela):
    buscaLarguraFrame = tk.Frame(janela, borderwidth=4, relief="ridge")
    buscaLarguraFrame.grid(column=0, row=0, padx=10, pady=10)
    #adicona o texto
    titulo = tk.Label(buscaLarguraFrame, text="Busca em largura", font=("Arial", 12, "bold"), justify="center")
    titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
    verticeFonte = tk.Label(buscaLarguraFrame, text="Vértice fonte", font=("Arial", 10))
    verticeFonte.grid(column=0, row=1, padx=10, pady=10)
    verticeChegada = tk.Label(buscaLarguraFrame, text="Vértice a ser buscado", font=("Arial", 10))
    verticeChegada.grid(column=1, row=1, padx=10, pady=10)

    entradaFonte = tk.Entry(buscaLarguraFrame, width=20)
    entradaFonte.grid(column=0, row=2, padx=20, pady=5)

    entradaChegada = tk.Entry(buscaLarguraFrame, width=20)
    entradaChegada.grid(column=1, row=2, padx=20, pady=5)

    caixaDeTexto = tk.Text(buscaLarguraFrame, width=40, height=8)
    caixaDeTexto.grid(row=0, column=2, padx=10, pady=10, rowspan=4)

    botaoEnviar = tk.Button(buscaLarguraFrame, text="Buscar", command=lambda: botaoBuscaLarguraClicado(entradaFonte, entradaChegada, caixaDeTexto))
    botaoEnviar.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

    return buscaLarguraFrame
def frameBuscaProfundidade(janela):
    buscaProfundidadeFrame = tk.Frame(janela, borderwidth=4, relief="ridge")
    buscaProfundidadeFrame.grid(column=0, row=1, padx=10, pady=10)
    #adicona o texto
    titulo = tk.Label(buscaProfundidadeFrame, text="Busca em profundidade", font=("Arial", 12, "bold"), justify="center")
    titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
    verticeFonte = tk.Label(buscaProfundidadeFrame, text="Vértice fonte", font=("Arial", 10))
    verticeFonte.grid(column=0, row=1, padx=10, pady=10)
    verticeChegada = tk.Label(buscaProfundidadeFrame, text="Vértice a ser buscado", font=("Arial", 10))
    verticeChegada.grid(column=1, row=1, padx=10, pady=10)

    entradaFonte = tk.Entry(buscaProfundidadeFrame, width=20)
    entradaFonte.grid(column=0, row=2, padx=20, pady=5)

    entradaChegada = tk.Entry(buscaProfundidadeFrame, width=20)
    entradaChegada.grid(column=1, row=2, padx=20, pady=5)

    caixaDeTexto = tk.Text(buscaProfundidadeFrame, width=40, height=8)
    caixaDeTexto.grid(row=0, column=2, padx=10, pady=10, rowspan=4)

    botaoEnviar = tk.Button(buscaProfundidadeFrame, text="Buscar", command=lambda: botaoBuscaProfundidadeClicado(entradaFonte, entradaChegada, caixaDeTexto))
    botaoEnviar.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

    return buscaProfundidadeFrame

def frameBuscaAEstrela(janela):
    buscaAEstrelaFrame = tk.Frame(janela, borderwidth=4, relief="ridge")
    buscaAEstrelaFrame.grid(column=0, row=2, padx=10, pady=10)
    #adicona o texto
    titulo = tk.Label(buscaAEstrelaFrame, text="Busca A*", font=("Arial", 12, "bold"), justify="center")
    titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
    verticeFonte = tk.Label(buscaAEstrelaFrame, text="Vértice fonte", font=("Arial", 10))
    verticeFonte.grid(column=0, row=1, padx=10, pady=10, columnspan=2)

    entradaFonte = tk.Entry(buscaAEstrelaFrame, width=20)
    entradaFonte.grid(column=0, row=2, padx=20, pady=5, columnspan=2)

    caixaDeTexto = tk.Text(buscaAEstrelaFrame, width=40, height=8)
    caixaDeTexto.grid(row=0, column=2, padx=10, pady=10, rowspan=4)

    botaoEnviar = tk.Button(buscaAEstrelaFrame, text="Buscar", command=lambda: botaoBuscaAEstrelaClicado(entradaFonte, caixaDeTexto))
    botaoEnviar.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

    return buscaAEstrelaFrame
def frameBuscaGulosa(janela):
    buscaGulosaFrame = tk.Frame(janela, borderwidth=4, relief="ridge")
    buscaGulosaFrame.grid(column=0, row=3, padx=10, pady=10)
    # adicona o texto
    titulo = tk.Label(buscaGulosaFrame, text="Busca Gulosa", font=("Arial", 12, "bold"),justify="center")
    titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
    verticeFonte = tk.Label(buscaGulosaFrame, text="Vértice fonte", font=("Arial", 10))
    verticeFonte.grid(column=0, row=1, padx=10, pady=10, columnspan=2)

    entradaFonte = tk.Entry(buscaGulosaFrame, width=20)
    entradaFonte.grid(column=0, row=2, padx=20, pady=5, columnspan=2)

    caixaDeTexto = tk.Text(buscaGulosaFrame, width=40, height=8)
    caixaDeTexto.grid(row=0, column=2, padx=10, pady=10, rowspan=4)

    botaoEnviar = tk.Button(buscaGulosaFrame, text="Buscar", command=lambda: botaoBuscaGulosaClicado(entradaFonte, caixaDeTexto))
    botaoEnviar.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

    return buscaGulosaFrame
def botaoBuscaLarguraClicado(entradaFonte, entradaChegada, caixaDeTexto):
    verticeFonte = entradaFonte.get()  # Obter o texto do campo
    verticeChegada = entradaChegada.get()
    vertices, resultado = grafo.buscaLargura(verticeFonte, verticeChegada)
    # Limpar
    caixaDeTexto.delete(1.0, tk.END)
    for vertice in vertices:
        caixaDeTexto.insert(tk.END, vertice + '\n')
    caixaDeTexto.insert(tk.END, resultado)

def botaoBuscaProfundidadeClicado(entradaFonte, entradaChegada, caixaDeTexto):
    verticeFonte = entradaFonte.get()
    verticeChegada = entradaChegada.get()
    vertices, resultado = grafo.buscaProfundidade(verticeFonte, verticeChegada)
    caixaDeTexto.delete(1.0, tk.END)
    for vertice in vertices:
        caixaDeTexto.insert(tk.END, vertice + '\n')
    caixaDeTexto.insert(tk.END, resultado)

def botaoBuscaAEstrelaClicado(entradaFonte, caixaDeTexto):
    verticeFonte = entradaFonte.get()
    vertices, trajeto = grafo.buscaAEstrela(verticeFonte)
    caixaDeTexto.delete(1.0, tk.END)
    for vertice in vertices:
        caixaDeTexto.insert(tk.END, vertice + '\n')
    caixaDeTexto.insert(tk.END, 'Valor do Percurso:' + str(round(trajeto,4)))


def botaoBuscaGulosaClicado(entradaFonte, caixaDeTexto):
    verticeFonte = entradaFonte.get()
    vertices, trajeto = grafo.buscaGulosa(verticeFonte)
    caixaDeTexto.delete(1.0, tk.END)
    for vertice in vertices:
        caixaDeTexto.insert(tk.END, vertice + '\n')
    caixaDeTexto.insert(tk.END, 'Valor do Percurso:' + str(round(trajeto,4)))

def gerarGrafo(janela):
    gerarGRafoFrame = tk.Frame(janela, borderwidth=4, relief="ridge")
    gerarGRafoFrame.grid(column=1, row=0, padx=10, pady=10, columnspan=2)

    titulo = tk.Label(gerarGRafoFrame, text="Gerar Grafo", font=("Arial", 15, "bold"),justify="center")
    titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
    verticeGrafo = tk.Label(gerarGRafoFrame, text="Vértice de chegada para busca Heurística", font=("Arial", 12))
    verticeGrafo.grid(column=0, row=1, padx=10, pady=10, columnspan=2)

    entradaVerticeGrafo = tk.Entry(gerarGRafoFrame, width=20)
    entradaVerticeGrafo.grid(column=0, row=2, padx=20, pady=5, columnspan=2)

    botaoEnviar = tk.Button(gerarGRafoFrame, text="Gerar",command=lambda: botaoGerarGrafoClicado(entradaVerticeGrafo, janela))
    botaoEnviar.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

def botaoGerarGrafoClicado(verticeChegada, janelaPrincipal):
    verticeGrafo = verticeChegada.get()
    grafo.adicionarValores(verticeGrafo)
    plotarGrafo(janelaPrincipal)

def plotarGrafo(janela):
    gerarGRafoFrame = tk.Frame(janela, borderwidth=4, relief="ridge")
    gerarGRafoFrame.grid(column=2, row = 1,padx=10, pady=10, rowspan=4)

    # para plotagem de grafo na tela
    canvas = FigureCanvasTkAgg(grafo.plotarGrafo(), master=gerarGRafoFrame)
    canvas.get_tk_widget().pack()
