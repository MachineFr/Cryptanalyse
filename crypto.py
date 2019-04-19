# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 08:41:02 2019

@author: Antoine
"""
import numpy as np
from math import floor
from collections  import Counter
""" -------------------------message 1--------------------------------------"""
print("---------------------message 1---------------------")
file= open("message1.txt",'r')
#print(Message.read())
Message=file.read()
longueur=len(Message)
print("longueur= "+str(longueur))
TableauMessage=[]
Decalage=1
Chaine=""
""" ici on met le texte dans un tableau qu'on inverse en prenant en compte
 la difference de taille entre le tableau et le texte (casevide) """

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

""" --------------------------message 2&3-----------------------------------"""
print("\n---------------------message 2|3---------------------\n")
"""ici on trouve juste la lettre la plus utilisé qu'on remplace par l'espace"""
file= open("message3.txt",'r',encoding="utf8")
Message=file.readline()
occurence=[0]*65536
Espace=ord(' ')
E=ord('e')
for i in range(len(Message)):
        occurence[ord(Message[i])]+=1     
m = max(occurence)     
l = [k for k, j in enumerate(occurence) if j == m]
EspaceCesar=(l[0]-Espace)
for i in range(len(Message)):
    print(chr(ord(Message[i])-EspaceCesar),end='')

""" ---------------------------message 4-------------------------------------"""
"""ajout du décalage et d'un tableau de caracteres par rapport au message 2&3 """
print("\n---------------------message 4---------------------\n")
file= open("message4.txt",'r',encoding="utf8")
Message=file.readline()
Dico=Counter(map(ord,Message))
LongueurVig=2
AsciiMostUse=Counter(Dico).most_common(LongueurVig)
NCharMostUse=[0]*LongueurVig

for i in range(LongueurVig):
    NCharMostUse[i]=AsciiMostUse[i][0]-Espace

for i in range(len(Message)):
    Decal=(i+1)%LongueurVig
    try:
        print(chr(ord(Message[i])-NCharMostUse[Decal]),end='')
    except:
        pass
    
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
def DicoToVig(MsgDec,Dico,TailleVig):
    AsciiMostUse=[Dico[0]]*TailleVig
    decalage=[0]*TailleVig
    for j in range(TailleVig):
        AsciiMostUse[j]=Counter(Dico[j]).most_common(TailleVig)# pour chaque décomposition retourne les caractere les plus présents
        decalage[j]=AsciiMostUse[j][0][0]-ord(' ')
    decalage[1]=AsciiMostUse[1][0][0]-ord('e')# à décommenter pour le message 5
#    decalage[1]=AsciiMostUse[1][0][0]-ord('c') à décommenter pour le message 6
#    decalage[3]=AsciiMostUse[3][0][0]-ord('i') à décommenter pour le message 6
#    decalage[4]=AsciiMostUse[4][0][0]-ord('e') à décommenter pour le message 6
#    decalage[7]=AsciiMostUse[7][0][0]-ord('e') à décommenter pour le message 6
     
    return decalage  

""" décode le message avec vigenere"""
def TransformMsg(lenMsg,MessageMorceau,clé):
    TailleVig=len(clé)
    MessageDecrypt=[]
    for i in range(int(lenMsg/TailleVig)):#int(lenMsg/TailleVig)
        for j in range(TailleVig):
            try:
                MessageDecrypt.append(chr((ord(MessageMorceau[j][i])-clé[j])))
            except:
                pass
    return MessageDecrypt


""" ------------------------------message 5&6-------------------------------"""
print("\n---------------------message 5|6---------------------\n")
file= open("message5.txt",'r',encoding="utf8")
Message=file.readline()
LongueurMessage=len(Message)
for LongueurVig in range (3,4): # 11,12 pour le 6
    print("Longueur: "+str(LongueurVig))
    MessageDecouper=MessageDecoupe(Message,LongueurVig)
    Dico=MsgIntoDico(MessageDecouper,LongueurVig)
    Vigenere=DicoToVig(MessageDecouper,Dico,LongueurVig) 
    print(Vigenere)
    MessageDecrypter=TransformMsg(LongueurMessage,MessageDecouper,Vigenere)
    for i in range(len(MessageDecrypter)):
        print(MessageDecrypter[i],end='')
        
"""/////////////////////////////____________\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"""
"""-----------------------------message final-------------------------------"""
"""\\\\\\\\\\\\\\\\\\\\\\\\\\\\\____________////////////////////////////////"""
print("\n---------------------message final---------------------\n")

file= open("antoine.txt",'r',encoding="utf8")
Message=file.readline()
LongueurMessage=len(Message)
for LongueurVig in range (3,4):
    print("Longueur: "+str(LongueurVig))
    MessageDecouper=MessageDecoupe(Message,LongueurVig)
    Dico=MsgIntoDico(MessageDecouper,LongueurVig)
    Vigenere=DicoToVig(MessageDecouper,Dico,LongueurVig) 
    print(Vigenere)
    MessageDecrypter=TransformMsg(LongueurMessage,MessageDecouper,Vigenere)
    file2=open("trantoine.txt",'w',encoding="utf8")
    Saut=False
    """ sert juste a enlever les caractères bizarre"""
    for i in range(len(MessageDecrypter)): 
        if Saut==False:
            if (ord(MessageDecrypter[i])>8350 and ord(MessageDecrypter[i])<10000):
                file2.write(chr(ord(MessageDecrypter[i])-8236))
            elif(MessageDecrypter[i]=='Ã'):
                file2.write(chr(ord(MessageDecrypter[i+1])+64))
                Saut=True
            else:
                file2.write(MessageDecrypter[i])
        else:
            Saut=False
    file.close()
    file2.close()
     