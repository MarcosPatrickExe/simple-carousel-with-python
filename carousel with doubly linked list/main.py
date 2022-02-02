# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 23:47:52 2022
@author: Patrick
"""
import cv2 as opencv;
import numpy as num;

print("Tecla 'a' passa para a imagem anterior \n"+
     "Tecla 'b' passa para a imagem posterior \n"+
     "Tecla 'i' exibe detalhes do filme \n"+
     "Tecla 'q' encerra a execução do programa \n");

# LSTA DUPLAMENTE ENCADEADA:
class Node:
    def __init__(self, elem = None, prev = None, next = None):
        self._elem_ = elem;
        self._prev_ = prev;
        self._next_ = next;

elementoSelecionado = Node();

class DoubleLinkedList:
    def __init__(self):
        self._length_ = 0;
        self._header_ = Node();
        self._trailer_ = Node();

    def __str__(self):
        valores = "Exibindo todos os nos da lista: \n";
        elementoAtual = self._header_._next_;

        while (elementoAtual._elem_ != None):
            valores += str(elementoAtual._elem_[0])+"\n";
            elementoAtual = elementoAtual._next_;
           
        print(valores);

    def append(self, elem):
        novoElemento = Node(elem);
        global elementoSelecionado;

        if(self._length_==0):
            self._header_._next_= novoElemento;
            self._trailer_._prev_ = novoElemento;
            novoElemento._next_ = self._trailer_;
            novoElemento._prev_ = self._header_;
            self._length_ +=1;

        else:
            ultimoElemento = self._trailer_._prev_;
            ultimoElemento._next_= novoElemento;
            self._trailer_._prev_ = novoElemento;
            novoElemento._next_ = self._trailer_;
            novoElemento._prev_ = ultimoElemento;
            self._length_ +=1;
            elementoSelecionado = novoElemento;

    def delete(self, elem):
        if (self._length_==0):
            raise ValueError("Lista vazia!!!");

        elif (self._header_._next_._elem_ == elem): 
    
     #  CASO O ELEMENTO A SER APAGADO ESTEJA NA PRIMEIRA POSICAO
            if (self._length_==1):
                self._length_ = 0;
                self._header_ = Node();
                self._trailer_ = Node();
            else:
                self._header_._next_ = self._header_._next_._next_;

        elif (self._length_>1):
            elementoAtual = self._header_._next_;

            while (elementoAtual._elem_ != None):
                 if(elementoAtual._elem_ == elem):
                     elementoAnterior = elementoAtual._prev_;
                     proximoElemento = elementoAtual._next_;
                     elementoAnterior._next_ = proximoElemento;
                     proximoElemento._prev_ = elementoAnterior;
                     break;

                 elementoAtual = elementoAtual._next_;

    def toRight(self):
        global elementoSelecionado

        #SE ESTIVER NA ULTIMA POSICAO O ELEMENTO ATUAL APONTA PARA O PRIMEIRO
        if(elementoSelecionado._next_._elem_ == None):
            elementoSelecionado = self._header_._next_;
        else:
            elementoSelecionado = elementoSelecionado._next_;
            print("foi pra direita \n Valor do elemento: "+str(elementoSelecionado._elem_)+"\n")
    
    def toLeft(self):
        global elementoSelecionado

        #SE ESTIVER NA PRIMEIRA POSICAO O ELEMENTO ATUAL APONTA PARA O ULTIMO
        if(elementoSelecionado._prev_._elem_ == None): 
            elementoSelecionado = self._trailer_._prev_;
        else:
            elementoSelecionado = elementoSelecionado._prev_;
            print("foi pra esquerda \n Valor do elemento: "+str(elementoSelecionado._elem_)+"\n")        


# AS IMAGENS TEM DIMENSÕES PRÓXIMAS DE 1688x2500
def carregarImagem(caminhoFoto):
    fileImage = opencv.imread(caminhoFoto, opencv.IMREAD_COLOR);
    #print("dimensões originais da imagem: "+str(fileImage.shape));
    width = int(fileImage.shape[1] * 0.25);
    height = int(fileImage.shape[0] * 0.25);
    dimensions = (width, height); #criando uma tupla
    resizedImage = opencv.resize(fileImage, dimensions, interpolation = opencv.INTER_AREA);
    return resizedImage;


lista = DoubleLinkedList();
lista.append(['images/Ant-man.jpg', 2015]);
lista.append(['images/Aquaman.jpg', 2018]);
lista.append(['images/Matrix.jpg', 1999]);
lista.append(['images/King Kong.jpg', 2005]);
lista.append(['images/Black panther.jpg', 2018]);
lista.append(['images/Captain marvel.jpg', 2019]);
lista.append(['images/Captain america.jpg', 2011]);
lista.append(['images/Avengers endgame.jpg', 2019]);
lista.append(['images/Avengers infinity war.jpg', 2018]);
lista.append(['images/Spider-man no way home.jpg', 2021]);
lista.append(['images/Captain america civil war.jpg', 2016]);

lista.__str__();

exibeDetalhes = False;
while True:
        opencv.imshow("Posters", carregarImagem(elementoSelecionado._elem_[0]) );
#        key = chr(opencv.waitKey(0)); # ValueError: chr() arg not in range(0x110000)
        key = opencv.waitKey(0);

        if key==ord('a') and (exibeDetalhes==False):
            lista.toLeft();

        if key==ord('i'):    
            
            if(exibeDetalhes==False):
                       # altura de 100 x 400 de largura, usando 3 canais de cores
                janelaMensagem = num.zeros((100, 450, 3), dtype='uint8')
                janelaMensagem[:] = 38, 38, 38; # Atribuindo cor cinza para o fundo
             
                opencv.putText(janelaMensagem, "Nome do filme: ", (10, 30), opencv.QT_FONT_NORMAL , 0.7, (255, 255, 255), 1, opencv.LINE_AA);
                txt = elementoSelecionado._elem_[0];
                nomeFilme = txt[ txt.rindex("/")+1 : txt.rindex(".")];
                opencv.putText(janelaMensagem,  nomeFilme, (200, 30), opencv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, opencv.LINE_AA); # Exibindo janela vazia (cor de fundo preto)
                                                                                                                            #thickness=2
                opencv.putText(janelaMensagem, "Ano de lancamento: ", (10, 70), opencv.QT_FONT_NORMAL , 0.7, (255, 255, 255), 1, opencv.LINE_AA);
                opencv.putText(janelaMensagem, str(elementoSelecionado._elem_[1]), (250, 70), opencv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, opencv.LINE_AA);

                opencv.imshow("Detalhes sobre o filme", janelaMensagem);
                exibeDetalhes=True;
               # opencv.waitKey(0);
                
            else:
                opencv.destroyWindow("Detalhes sobre o filme");
                exibeDetalhes=False;

        if key==ord('d') and (exibeDetalhes==False):
            lista.toRight();
            
        if key==ord('q'): 
            print("Tecla 'Q' foi pressionada! \nSaindo do programa....");
            opencv.destroyAllWindows();
            break;

    







































































#https://stackoverflow.com/questions/22855475/python-opencv-refresh-images-when-a-key-is-pressed

#print("The sum of the two given numbers is {} ".format(addition))
#print("The name of the user is {0} and his/her age is {1}".format(name, age))

"""
# APLICANDO FIGURAS GEOMETRICAS NA IMAGEM:
import numpy as num;

# Criando janela vazia de tamanho 500x500 que irá 
# operar com 3 canais de cores
blank = num.zeros((500, 500, 3), dtype='uint8')
opencv.imshow('Blank', blank); # Exibindo janela vazia (cor de fundo preto)

blank[:] = 0,255,0; #Atribuindo a cor Verde para todo o fundo da janela
opencv.imshow('Green Window example', blank)

#Desenhando um pequeno quadrado na janela de fundo verde
blank[200:300, 200:300] = 0,0,255; 
opencv.imshow('Litte red square', blank)

opencv.rectangle(blank, (0,0), (250, 250), (255,0,255), thickness=opencv.FILLED); 
# "thickness" pode ter valor 2 que é a largura da borda da janela 
# ou FIILED que irá preencher o retangulo com a cor verde

opencv.imshow('Rectangle in blank', blank);
"""

#opencv.resize(200);
#opencv.namedWindow("Rectangle in blank", opencv.WINDOW_NORMAL);
#opencv.resizeWindow("images/Ant man.jpg", 300, 300);


#DOCUMENTATION:
#https://opencv-python.readthedocs.io/_/downloads/en/latest/pdf/  


# VIDEO AULA:
#https://www.bing.com/videos/search?q=using+opencv+in+python&&view=detail&mid=58C011626533C0E44B6158C011626533C0E44B61&&FORM=VRDGAR&ru=%2Fvideos%2Fsearch%3Fq%3Dusing%2Bopencv%2Bin%2Bpython%26FORM%3DHDRSC3