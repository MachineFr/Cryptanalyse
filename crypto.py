# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 08:41:02 2019

@author: Antoine
"""
import numpy as np
from math import floor
from collections  import Counter
file= open("message1.txt",'r')
#print(Message.read())
Message=file.read()
#MAJ 65->90
longueur=len(Message)
print("longueur= "+str(longueur))
TableauMessage=[]
Decalage=1
Chaine=""
while Chaine[2:10]!="Fonction"and Decalage<10:
    Nmessage=[]
    TableauMessage=[]
    tableauI=floor(longueur/Decalage)
    CaseVide=longueur%Decalage
    for i in range(Decalage):
        LigneMessage=[]
        for j in range(tableauI):
            try :
                if longueur-(i*tableauI+j)>CaseVide:
                    LigneMessage.append(Message[i*tableauI+j])
            except:
                pass
        TableauMessage.append(LigneMessage) 
    for i in range(CaseVide):
        TableauMessage[i].append(Message[longueur+i-CaseVide])
    for i in range(len(TableauMessage[0])): #taille du message
        for j in range(len(TableauMessage)): #Nombre de ligne
            try :
                Nmessage.append(TableauMessage[j-CaseVide-1][i])
            except:
                pass
    Decalage+=1
    Chaine=""
    for i in range(len(Nmessage)):
        Chaine+=str(Nmessage[i])   
print("NbLigne= "+str(Decalage))
print("TailleLigne= "+str(tableauI))
print("CaseVide= "+str(longueur%Decalage))
print("n°tour :"+str(Decalage)+"resultat : ")
print(Chaine[CaseVide+1:])
print("")


#while decrypt==False:
#    for i in range(1,longueur):
#        if ord(Message[i])==46 and ord(Message[i+j])>=65 and ord(Message[i+j])<=90:
#            decrypt=True
#        else:
#            break
#    j+=1
#print(j)
""" -----message 2&3-----"""
#file= open("message3.txt",'r',encoding="utf8")
#Message=file.readline()
#print(ord(Message[0]))
#print(Message)
#occurence=[0]*65536
#Espace=32
#E=101
#for i in range(len(Message)):
#        print(Message[i])
#        occurence[ord(Message[i])]+=1     
#m = max(occurence)     
#l = [k for k, j in enumerate(occurence) if j == m]
#EspaceCesar=(l[0]-Espace)
#ECesar=(l[0]-E)
#for i in range(len(Message)):
#    print(chr(ord(Message[i])-EspaceCesar),end='')
""" -----message 4-----"""

#file= open("message4.txt",'r',encoding="utf8")
#Espace=32
#Message=file.readline()
#Dico=Counter(map(ord,Message))
#LongueurVig=2
#AsciiMostUse=Counter(Dico).most_common(LongueurVig)
#NCharMostUse=[0]*LongueurVig
#
#for i in range(LongueurVig):
#    print(AsciiMostUse[i][0])
#    NCharMostUse[i]=AsciiMostUse[i][0]-Espace
#print( NCharMostUse)
#
#for i in range(len(Message)):
#    Decal=(i+1)%LongueurVig
#    try:
#        print(chr(ord(Message[i])-NCharMostUse[Decal]),end='')
#    except:
#        pass
#    
from collections  import Counter
"""transforme le message en plusieur message découper caractere par caractere
(nombre de message correspondant la la longueur de la clé testé)"""
def MessageDecoupe(Message,clé):
    MsgDecoupe=[0]*clé
    for NbVig in range(clé):
        MessageTemp="";
        for i in range(int((len(Message)/clé))):
            MessageTemp+=Message[i*clé+NbVig]
        MsgDecoupe[NbVig]=MessageTemp
    return MsgDecoupe
"""transforme le message donné en un dictionnaire de repetition de caractere"""
def MsgIntoDico(Msg,clé):
    
    Dico=[0]*clé
    for i in range(clé):
        Dico[i]=Counter(map(ord,Msg[i]))
    return Dico
"""trouve les caracteres les plus utilisés, enleve la lettre la plus utilisée 
pour trouver le décalage entre les deux, correspondant à la clé de vigenere"""
def DicoToVig(Dico,TailleVig):
    AsciiMostUse=[Dico[0]]*TailleVig
    decalage=[0]*TailleVig
    for j in range(TailleVig):
        AsciiMostUse[j]=Counter(Dico[j]).most_common(TailleVig)# pour chaque décomposition retourne les caractere les plus présents
        decalage[j]=AsciiMostUse[j][0][0]-Espace
    return decalage
""" décode le message avec vigenere"""
def TransformMsg(lenMsg,MessageMorceau,clé):
    TailleVig=len(clé)
    for i in range(int(lenMsg/TailleVig)):
        for j in range(TailleVig):
            try:
                print(chr((ord(MessageMorceau[j][i])-clé[j])),end='')
            except:
                pass
""" -----message 6-----"""

#file= open("message6.txt",'r',encoding="utf8")
#Espace=ord(' ')
#Message=file.readline()
#LongueurMessage=len(Message)
#for LongueurVig in range (11 ,12):
#    MessageDecouper=MessageDecoupe(Message,LongueurVig)
#    Dico=MsgIntoDico(MessageDecouper,LongueurVig)
#    Vigenere=DicoToVig(Dico,LongueurVig) #[2, 9, 3, 1, 3, 5, 11, 10, 4, 3, 7]
#    TransformMsg(LongueurMessage,MessageDecouper,Vigenere)
