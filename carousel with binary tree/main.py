# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 22:02:13 2022
@author: Patrick
"""
#from tkinter import FALSE
import cv2 as opencv;
import numpy as num;
from abc import ABC, abstractmethod


#------------------------CLASSE ADT---------------------------
class TreeADT(ABC):

    @abstractmethod
    def insert(self, value):
        """Insere <value> na arvore"""
        pass

    @abstractmethod
    def empty(self):
        """Verifica se a arvore esta vazia"""
        pass

    @abstractmethod
    def root(self):
        """Retorna o no raiz da arvore"""
        pass
#-----------------------FIM CLASSE ADT------------------------------------





#-----------------------CLASSE DE NÓ-------------------------------------
class Node:

    def __init__(self, data=None, parent=None, left=None, right=None):
        self._data = data
        self._parent = parent
        self._left = left
        self._right = right

    def empty(self):
        return not self._data #Nota:  not None retorna True

    def __str__(self):
        return self._data.__str__()
#--------------------------------------------------------------------------




#------- CLASSE BinaryTree COM AS IMPLEMENTAÇÕES DOS MÉTODOS DA SUA SUPER CLASSE--------------------------------------
class BinaryTree(TreeADT):

    def __init__(self, data = None):
        self._root = Node(data)
    
    def empty(self):
        return not self._root._data

    def root(self):
        return self._root

    def insert(self, elem): # 18
        node = Node(elem) # node(18,_,_,_)
        if self.empty():
            self._root = node
        else:
            self.__insert_children(self._root, node)

    def __insert_children(self, root, node): # root(15,11,_,18) - node(18,15,_,_)

        if (node._data["valorRed"]) < (root._data["valorRed"]):
            if (not root._left):  # Caso base - condicao de parada da recursividade
                root._left = node
                node._parent = root
            else:
                self.__insert_children(root._left, node) 

        elif (node._data['valorRed']) > (root._data['valorRed']):
            if (not root._right): # caso (_right != None) entao retorna True e dps False;
                root._right = node;
                node._parent = root;
            else:
                self.__insert_children(root._right, node);
       
        """
            if (node._data <= root._data):
                if not root._left:  # Caso base - condiÃ§Ã£o de parada da recursividade
                    root._left = node
                    root._left._parent = root
                else:
                    self.__insert_children(root._left, node) # sub-ÃƒÂ¡rvore esquerda
        
            else:
                if not root._right: # caso (_right != None) entÃ£o retorna True e dps False;
                    root._right = node._data;
                    node._parent = node;
                else:
                    self.__insert_children(root._right, node);
        """

    def traversal(self, in_order=True, pre_order=False, post_order=False):
        result = list()
        if in_order:
            in_order_list = list()
            result.append(self.__in_order(self._root, in_order_list))
        else:
            result.append(None)

        if pre_order:
            pre_order_list = list()
            result.append(self.__pre_order(self._root, pre_order_list))
        else:
            result.append(None)

        if post_order:
            post_order_list = list()
            result.append(self.__post_order(self._root, post_order_list))
        else:
            result.append(None)

        return result

    def __in_order(self, root, listaValores): #PRIMEIRO RAIZ Ã‰ CONSULTADA, DEPOIS O RAMO ESQUERDO E DEPOIS O RAMO DIREITO
        
        if self.empty():
            print("Raiz da arvore vazia! Impossivel encontrar valores! ");
            return;
        else:
            if (root._left != None):
                self.__in_order(root._left, listaValores);

            listaValores.append(root._data);
            
            if (root._right != None):
                self.__in_order(root._right, listaValores);

        # QUANDO A FUNÃ‡ÃƒO VOLTAR AO SEU PRIMEIRO ESCOPO O "_parent" DE "root" valerÃ¡ None, pois ele estarÃ¡ na raiz da Ã¡rvore
        if (root._parent == None): 
            return listaValores;

        """
        if (self.empty()):
            return
        
        self.__in_order(root._left, lista)
        lista.append(root._data)  
        self.__in_order(root._right, lista)
        return lista
        """

    def __pre_order(self, root = None, valores = None):
       
        if self.empty():
            print("Raiz da arvore vazia! Impossivel encontrar valores! ");
            return;
        else:
            valores.append(root._data);

            if (root._left != None):
                self.__pre_order(root._left, valores);

            if (root._right != None):
                self.__pre_order(root._right, valores);

        if (root._parent == None): 
            return valores;
        """
            if not root:
                return
            lista.append(root._data) # modificar para o trabalho parte 2???
            self.__pre_order(root._left, lista)
            self.__pre_order(root._right, lista)
            return lista    
        """
    def __post_order(self, root, valores):
       
        if self.empty():
            print("Raiz da arvore vazia! Impossivel encontrar valores! ");
            return;
        else:
            if (root._left != None):
                self.__post_order(root._left, valores);

            if (root._right != None):
                self.__post_order(root._right, valores);

            valores.append(root._data);  
        
        if (root._parent == None): 
            return valores;
        """
        if not root:
            return
        self.__post_order(root._left, lista)
        self.__post_order(root._right, lista)
        lista.append(root._data) # modificar para o trabalho parte 2???
        return lista
        """

    def print_binary_tree(self):
        if self._root:
            print(self.traversal(False, True, False)[1])

#-------------------FIM DA CLASSE "Binary Tree" AQUI------------------------------------------------------------







#------------------------------------------------------------------------------------
#---------------------INICIO DA APLICACAO A PARTIR DAQUI--------------------------------------------------
#------------------------------------------------------------------------------------

imagens= [
    ['images/Ant-man.jpg', 2015],
    ['images/Aquaman.jpg', 2018],
    ['images/Matrix.jpg', 1999],
    ['images/King Kong.jpg', 2005],
    ['images/Black panther.jpg', 2018],
    ['images/Captain marvel.jpg', 2019],
    ['images/Captain america.jpg', 2011],
    ['images/Avengers endgame.jpg', 2019],
    ['images/Avengers infinity war.jpg', 2018],
    ['images/Spider-man no way home.jpg', 2021],
    ['images/Captain america civil war.jpg', 2016],
    ['images/The book of eli.jpg', 2010],
    ['images/Zombieland double tap.jpg', 2019],
    ['images/I robot.jpg', 2004],
    ['images/Real steel.jpg', 2011] 
];


redChannelImages = [None]*len(imagens) ;#Criando lista de tamanho 11

# LINK PARA PEGAR CORES RGB DA IMAGEM:
#https://www.pyimagesearch.com/2021/01/20/opencv-getting-and-setting-pixels/

def truncate(numero, digitos): #FUNCAO QUE REDUZ O NUMERO DE CASAS DECIMAIS
    nums = str(numero).split('.');
    decimais = nums[1];
    decimais = decimais[:digitos]
    return str(nums[0])+"."+str(decimais); 


print(" \n    Realizando a leitura das imagens, por favor aguarde..... \n \n");

for i in range(0, len(imagens)):
    fileImage = opencv.imread(imagens[i][0], opencv.IMREAD_COLOR);
    width = int( fileImage.shape[1] );
    height = int( fileImage.shape[0] );
    totalRed = 0;

    for pixelX in range(width):
        for pixelY in range(height):
            (b, g, r) = fileImage[pixelY, pixelX]
            totalRed += r; #somando todos os valores de red de cada pixel existente na imagem

   # nome_recortado = cortarNomeImagem(imagens[i]);

    redChannelImages[i] = {
        "nomeImagem" : imagens[i][0], #nome_recortado
        "dataLancamento" : imagens[i][1],
        "valorRed" : totalRed
    }

    i+=1;
    print(" "+truncate( i/len(imagens)*100, 2) +"% carregado....");





# INSERINDO OS VALORES NA ARVORE BINARIA
no = BinaryTree(redChannelImages[0]);

for index in range(1, len(redChannelImages)):
    no.insert(redChannelImages[index]);  
    # inserindo o dicionario que contem tanto seu nome como 
    # a soma total dos valores do canal RED de todos os pixel da imagem



exibirDetalhes = False;
indexAtual = 1;
cortarNomeImagem = lambda name : name[ name.rindex('/')+1 : name.rindex('.') ];
lista_order = None;

def pegarElemento(index, lista, dados):
    contador = 0;

    for elemento in lista:

        if contador == index:
            if dados =='nomeImagem':
                return elemento['nomeImagem']; 
          
            elif dados =='valorTotalRed':
                return elemento['valorRed'];

            elif dados =='data':
                return elemento['dataLancamento'];
        ## Retornando o nome da imagem ou a soma total dos valores seu canal RED 
        # que se encontra na posicao "index" 
        # da lista  que foi percorrida por um dos metodos apresentados abaixo
        contador+=1;


# AS IMAGENS TEM DIMENSOES PRÓXIMAS DE 1688x2500
def carregarImagem(caminhoFoto):
    fileImage = opencv.imread(caminhoFoto, opencv.IMREAD_COLOR);
    #print("dimensoes originais da imagem: "+str(fileImage.shape));
    width = int(fileImage.shape[1] * 0.25);
    height = int(fileImage.shape[0] * 0.25);
    dimensions = (width, height); #criando uma tupla
    resizedImage = opencv.resize(fileImage, dimensions, interpolation = opencv.INTER_AREA);
    return resizedImage;


#================= LOOP DE ACESSO AO MENU INICIAL ==================
print("\n Seja bem-vindo(a)! Escolha uma das opcoes abaixo para percorer\n as imagens das capas de filmes cadastradas no programa: \n");

while True:
     consultarLista = False;
    
     response = input("\n  In-order (digite 1)  \n  Pre-order (digite 2)  \n  Post-order (digite 3)  \n  Encerrar programa (digite 4)")  ;

     if (response == '1'):
         lista_order = no.traversal(True, False, False)[0];
         consultarLista = True;

     elif (response == '2'):
         lista_order = no.traversal(False, True, False)[1];
         consultarLista = True;

     elif (response == '3'):
         lista_order = no.traversal(False, False, True)[2];
         consultarLista = True;

     elif (response == '4'):
         print("\n Finalizando execucao.... \n");
         break;

     elif (type(response)=='str'):     
         raise ValueError("Caracteres do tipo String nao sao permitidos!!");
     
     else: 
         print("\n Entrada de valor invalido, por favor digite novamente! \n");
         
        
     if consultarLista == True:
         print("\n Tecla A -> imagem anterior ");
         print(" Tecla D -> imagem posterior ");
         print(" Tecla I -> ver/ocultar detalhes do filme ");
         print(" Tecla Q -> voltar ao menu... \n");

     while consultarLista:
             nome_da_imagem = pegarElemento(indexAtual, lista_order, "nomeImagem"); 
           # A FUNCAO "pegarElemento" BUSCA O ELEMENTO CORRESPONDENTE A IMAGEM NA LISTA QUE FOI 
           # CRIADA E RETORNADA PELO METODO "traversal()"


             opencv.imshow("Poster", carregarImagem(nome_da_imagem) );
             tecla = opencv.waitKey(0);


             if tecla == ord('a') and (exibirDetalhes==False):
                 if (indexAtual-1) < 0:
                     print("Nao existe elemento a esquerda !!");
                 else:
                     indexAtual-=1;

             if tecla == ord('d') and (exibirDetalhes==False):
                 if (indexAtual+1) == len(lista_order):
                     print("Nao existe elemento a direita !!");
                 else:
                     indexAtual+=1

                
             if tecla == ord('i'): #opencv.getWindowProperty('Detalhes sobre o filme', 0) == -1
                    
                    if exibirDetalhes == False:
                                # altura de 100 x 400 de largura, usando 3 canais de cores
                                janelaMensagem = num.zeros((100, 450, 3), dtype='uint8')
                                janelaMensagem[:] = 38, 38, 38; # Atribuindo cor cinza para o fundo
                            
                                opencv.putText(janelaMensagem, "Nome do filme: ", (10, 30), opencv.QT_FONT_NORMAL , 0.7, (255, 255, 255), 1, opencv.LINE_AA);
                            
                                txt = pegarElemento(indexAtual, lista_order, "nomeImagem");
                                nomeFilme = txt[ txt.rindex("/")+1 : txt.rindex(".")];
                            
                                opencv.putText(janelaMensagem,  nomeFilme, (200, 30), opencv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, opencv.LINE_AA); # Exibindo janela vazia (cor de fundo preto)
                                                                                                                    #thickness=2
                                opencv.putText(janelaMensagem, "Ano de lancamento: ", (10, 70), opencv.QT_FONT_NORMAL , 0.7, (255, 255, 255), 1, opencv.LINE_AA);
                                opencv.putText(janelaMensagem, str(pegarElemento(indexAtual, lista_order, "data")), (250, 70), opencv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, opencv.LINE_AA);

                                opencv.imshow("Detalhes sobre o filme", janelaMensagem);
                               # opencv.setMouseCallback("Detalhes sobre o filme", mouseClick);
                               # opencv.waitKey(0);
                               # print("WND_PROP_VISIBLE) == -1 retornou =>  "+str(opencv.WND_PROP_VISIBLE));   
                                exibirDetalhes = True;
                                

                    elif exibirDetalhes == True:
                                opencv.destroyWindow("Detalhes sobre o filme"); 
                                exibirDetalhes = False;

              
             if (tecla == ord('q')) and (exibirDetalhes==False):
                 opencv.destroyAllWindows();
                 consultarLista = False;
                 print("\n  Voltando para a tela de menu...... \n");
                 break;
            
##==================================== FIM CODIGO DA APLICACAO =================================================
            






















































"""
    print(  
           redChannelImages[i]["nomeImagem"] +" => "+
           str(redChannelImages[i]["valorRed"])+" // width: "+
           str(width)+" // height: "+
           str(height)
        );
"""



"""
listaPre_order = no.traversal(False, True, False)[1];  # pre-order
print("Lista de imagens no modo Pre-order: \n")
# USANDO A SINTAXE DE LISTA COMPRIMIDA PARA EXIBIR OS VALORES
[  print( image['nomeImagem']+": "+str(image['valorRed'])+"") for image in listaPre_order]; 


listaIn_order = no.traversal(True, False, False)[0];  # in-order
print("\n Lista de imagens no modo In-order: \n")
[  print( image['nomeImagem'] +": "+str(image['valorRed'])+"") for image in listaIn_order];


listaPost_order = no.traversal(False, False, True)[2]; # post-order
print("\n Lista de imagens no modo Post-order: \n")
[  print( image['nomeImagem']+": "+str(image['valorRed'])+"") for image in listaPost_order];
"""
# TypeError: list indices must be integers or slice, not dict (para resoler isso basta acessar o indice que contem o dict diretamente como: index["propriedade"] e nao assim:  vetor[index]  )








"""
nos = BinaryTree(11);
nos.insert(9);
nos.insert(15);
nos.insert(13);
nos.insert(3);
nos.insert(10);

valores = nos.traversal(None, True, False);# Executando o pre-order
print("Valores no modo de 'pre-order':");
print( str([ v for v in valores]) +" \n");

valores = nos.traversal(True, None, None); # Executando o In-order
print("Valores no modo de 'in-order':");
print( str([ v for v in valores]) +" \n");

valores = nos.traversal(None, None, True); # Executando o post-order
print("Valores no modo de 'post-order':");
print( str([ v for v in valores]) +" \n");
"""

# CRIANDO LISTAS DE FORMA MAIS FÃCIL:
#https://stackoverflow.com/questions/10712002/create-an-empty-list-in-python-with-certain-size

"""

if __name__ == '__main__':
    t = BinaryTree()
    t.insert(11)
    t.insert(9)
    t.insert(15)
    t.insert(13)
    t.insert(3)
    t.insert(10)
    t.print_binary_tree()
    l = t.traversal(True, True, True)
    print(l)

"""
