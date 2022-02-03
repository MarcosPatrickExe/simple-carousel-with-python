# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 22:02:13 2022
@author: Patrick
"""
from tkinter import FALSE
import cv2 as opencv;
import numpy as num;
from abc import ABC, abstractmethod


class TreeADT(ABC):

    @abstractmethod
    def insert(self, value):
        """Insere <value> na Ã¡rvore"""
        pass

    @abstractmethod
    def empty(self):
        """Verifica se a árvore está vazia"""
        pass

    @abstractmethod
    def root(self):
        """Retorna o não raiz da árvore"""
        pass


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
            if (not root._left):  # Caso base - condição de parada da recursividade
                root._left = node
                node._parent = root
            else:
                self.__insert_children(root._left, node) 

        elif (node._data['valorRed']) > (root._data['valorRed']):
            if (not root._right): # caso (_right != None) então retorna True e dps False;
                root._right = node;
                node._parent = root;
            else:
                self.__insert_children(root._right, node);
       
        """
            if (node._data <= root._data):
                if not root._left:  # Caso base - condição de parada da recursividade
                    root._left = node
                    root._left._parent = root
                else:
                    self.__insert_children(root._left, node) # sub-Ã¡rvore esquerda
        
            else:
                if not root._right: # caso (_right != None) então retorna True e dps False;
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

    def __in_order(self, root, listaValores): #PRIMEIRO RAIZ É CONSULTADA, DEPOIS O RAMO ESQUERDO E DEPOIS O RAMO DIREITO
        
        if self.empty():
            print("Raíz da árvore está vazia! Impossível de cunsultar seus valores! ");
            return;
        else:
            if (root._left != None):
                self.__in_order(root._left, listaValores);

            listaValores.append(root._data);
            
            if (root._right != None):
                self.__in_order(root._right, listaValores);

        # QUANDO A FUNÇÃO VOLTAR AO SEU PRIMEIRO ESCOPO O "_parent" DE "root" valerá None, pois ele estará na raiz da árvore
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
            print("Raíz da árvore está vazia! Impossível de cunsultar seus valores! ");
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
            print("Raíz da árvore está vazia! Impossível de cunsultar seus valores! ");
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


imagens= ['images/Ant-man.jpg',
'images/Aquaman.jpg',
'images/Matrix.jpg',
'images/King Kong.jpg', 
'images/Black panther.jpg', 
'images/Captain marvel.jpg', 
'images/Captain america.jpg', 
'images/Avengers endgame.jpg',
'images/Avengers infinity war.jpg',
'images/Spider-man no way home.jpg', 
'images/Captain america civil war.jpg']

redChannelImages = [None]*11;#Criando lista de tamanho 11

# LINK PARA PEGAR CORES RGB DA IMAGEM:
#https://www.pyimagesearch.com/2021/01/20/opencv-getting-and-setting-pixels/

for i in range(0, len(imagens)):
    fileImage = opencv.imread(imagens[i], opencv.IMREAD_COLOR);
    width = int(fileImage.shape[1]);
    height = int(fileImage.shape[0]);
    totalRed = 0;

    for pixelX in range(width):
        for pixelY in range(height):
            (b, g, r) = fileImage[pixelY, pixelX]
            totalRed += r; #somando todos os valores de red de cada pixel existente na imagem

    redChannelImages[i] = {"nomeImagem" : imagens[i], "valorRed" : totalRed}
    print(redChannelImages[i]["nomeImagem"] +" => "+str(redChannelImages[i]["valorRed"])+" // width: "+str(width)+" // height: "+str(height));

#print("length: "+str(len(redChannelImages)))


nomeImagem = lambda name : name[ name.rindex('/')+1 : name.rindex('.') ];

no = BinaryTree(redChannelImages[0]);

for index in range(1, len(redChannelImages)):
    no.insert(redChannelImages[index]);  # in-order, pre-order, post-order

listaPre_order = no.traversal(False, True, False)[1];  # in-order, pre-order, post-order
print("Lista de imagens no modo Pre-order: \n")
[  print(nomeImagem(image['nomeImagem'])+": "+str(image['valorRed'])+"") for image in listaPre_order];

listaIn_order = no.traversal(True, False, False)[0];  # in-order, pre-order, post-order
print("\n Lista de imagens no modo In-order: \n")
[  print(nomeImagem(image['nomeImagem'])+": "+str(image['valorRed'])+"") for image in listaIn_order];

listaPost_order = no.traversal(False, False, True)[2]; # in-order, pre-order, post-order
print("\n Lista de imagens no modo Post-order: \n")
[  print(nomeImagem(image['nomeImagem'])+": "+str(image['valorRed'])+"") for image in listaPost_order];



# TypeError: list indices must be integers or slice, not dict (para resoler isso basta acessar o indice que contem o dict diretamente como: index["propriedade"] e não assim:  vetor[index]  )














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

# CRIANDO LISTAS DE FORMA MAIS FÁCIL:
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
