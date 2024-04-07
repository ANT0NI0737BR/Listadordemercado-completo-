import PySimpleGUI as sg
import os


Frios = []

Produtos_de_limpeza = []

Carnes = []

Doces = []

Basicos = []

vegetais_frutas = []

Bebidas = []

Extra = []


todas = (Frios, Produtos_de_limpeza, Carnes, Doces, Basicos, vegetais_frutas, Bebidas, Extra)
todasequivalem = ('frios', 'produtos de limpeza', 'carnes', 'doces', 'basicos', 'planta', 'bebidas', 'extra')







def atualizar_lista(lista, como_o_que):

    Janela[(f'{lista}')].update(como_o_que[1:])


def apppend(contador, até, amudar, conteudo):

    while conteudo[contador] != (f'{até}'):

        amudar.append(conteudo[contador])

        contador = contador + 1

    return(contador)


def ler_arquivo(arq):
    lista = open(f'{arq}','r', encoding='utf8')

    conteudo = lista.readlines()

    contador1 = 0


    while contador1 != (len(conteudo)):

        if contador1 == len(conteudo)-1:

            print ('len==contador1')

            #print(len(conteudo))
            #print(f'{contador1}' + '\n')

        else:

            conteudo[contador1] = conteudo[contador1][:len(conteudo[contador1])-1]
        
            #print(len(conteudo))
            #print(f'{contador1}' + '\n')
        
        contador1 = contador1 + 1



    lista.close()

    contador1 = 0

    if conteudo[contador1] == 'Frios':

        contador1=apppend(contador1, 'Produtos de limpeza', Frios, conteudo)
        
    if conteudo[contador1] == 'Produtos de limpeza':

        contador1=apppend(contador1, 'Carnes', Produtos_de_limpeza, conteudo)
        
    if conteudo[contador1] == 'Carnes':

        contador1=apppend(contador1, 'Doces', Carnes, conteudo)

    if conteudo[contador1] == 'Doces':

        contador1=apppend(contador1, 'Basicos', Doces, conteudo)

    if conteudo[contador1] == 'Basicos':

        contador1=apppend(contador1, 'vegetais/frutas', Basicos, conteudo)

    if conteudo[contador1] == 'vegetais/frutas':

        contador1=apppend(contador1, 'Bebidas', vegetais_frutas, conteudo)

    if conteudo[contador1] == 'Bebidas':

        contador1=apppend(contador1, 'Extra', Bebidas, conteudo)

    if conteudo[contador1] == 'Extra':
        
        apppend(contador1, 'fim' , Extra, conteudo)
    
    
    

    return(Frios, Produtos_de_limpeza, Carnes, Doces, Basicos,  vegetais_frutas, Bebidas, Extra)





pesquisa = [

    [sg.FileBrowse('Pesquisar'),sg.Input('')],
    [sg.Submit('Aplicar')]

]

FRIOS = [

    [sg.Listbox((), size=(25, 20), key='frios')]
]

PRODUTOS_DE_LIMPEZA = [

    [sg.Listbox((), size=(25, 20), key='produtos de limpeza')]
]

CARNES = [

    [sg.Listbox((), size=(25, 20), key='carnes')]
]

DOCES = [

    [sg.Listbox((), size=(25, 20), key='doces')]
]

BASICOS = [

    [sg.Listbox((), size=(25, 20), key='basicos')]
]

PLANTAS = [

    [sg.Listbox((), size=(25, 20), key='planta')]
]

BEBIDAS = [

    [sg.Listbox((), size=(25, 20), key='bebidas')]
]

EXTRA = [

    [sg.Listbox((), size=(25, 20), key='extra')]
]

layout = [

    [sg.TabGroup( [ [ 
        sg.Tab('tipo', pesquisa),
        sg.Tab('FRIOS', FRIOS), 
        sg.Tab('LIMPEZA', PRODUTOS_DE_LIMPEZA),
        sg.Tab('CARNES', CARNES),
        sg.Tab('DOCES', DOCES),
        sg.Tab('BASICOS', BASICOS),
        sg.Tab('PLANTAS', PLANTAS),
        sg.Tab('BEBIDAS', BEBIDAS),
        sg.Tab('EXTRA', EXTRA),
        ] ] )]
    
]



Janela = sg.Window("lista compras",layout,finalize=True)
Janela.maximize()
while True:
    e,v = Janela.read()
    
    if e == sg.WINDOW_CLOSED:
        break

    if e == 'Aplicar':
        arquivo = v['Pesquisar'] or '.' 

        conteudo = ler_arquivo(arquivo)

        contagem = 0

        while contagem != len(todas):

            print(todasequivalem[contagem])

            atualizar_lista( (todasequivalem[contagem]) , (todas[contagem]) )

            print(todasequivalem[contagem])
        
            contagem = contagem + 1


#made by https://github.com/ANT0NI0737BR
