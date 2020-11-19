"""
Nom et prénom 1:
Nom et prénom 2:
"""

import os
import math


"""
Nom du fichier qui sera traité
"""
nomfic = "exemple.txt"


"""
Classe Noeud pour construire l'arbre de Huffman
"""

class Noeud:
    """
    Classe qui représente les noeuds internes et externes de l'arbre de
    codage de Huffman. Un noeud contient:
    - une lettre: si le noeud est une feuille, la lettre est un symbole du texte.
    Sinon, il s'agit d'un espace.
    - un fils gauche et droite
    - un champ nb_occur qui donne le nombre d'occurences de la lettre dans le texte
    - un champ freq qui donne la fréquence de la lettre dans le texte
    """

    def __init__(self,
                 lettre='.',
                 fils_gauche=None,
                 fils_droite=None,
                 nb_occur=0,
                 freq=0):
        self.lettre = lettre
        self.fils_gauche = fils_gauche
        self.fils_droite = fils_droite
        self.nb_occur = nb_occur
        self.freq = freq

    
    def __repr__(self):
        return "({},{},{},{},{})".format(
                self.lettre, self.fils_gauche, self.fils_droite,self.nb_occur,self.freq)



"""
Question 1: remplacer les None par les expressions qui conviennent
"""

noeudE=Noeud('E',None,None,8,0.0)
noeudA=Noeud('A',None,None,6,0.0)
noeudI=Noeud('I',None,None,5,0.0)
noeudO=Noeud('O',None,None,3,0.0)
noeudU=Noeud('U',None,None,2,0.0)

print("noeudE=", noeudE)
print("noeudA=", noeudA)
print("noeudI=", noeudI)
print("noeudO=", noeudO)
print("noeudU=", noeudU)
"""
print("noeudP2=", noeudP2)
print("noeudP3=", noeudP3)
print("noeudP4=", noeudP4)
print("noeudP5=", noeudP5)
"""


"""
  Question 2: Décrire la fonction lire_fichier, en particulier ce qu'elle calcule.
  Répondez à la question 2 ici ou juste après la fonction.
"""

def lire_fichier(nomfic):
    fichier = open(nomfic,"r")
    contenu  = fichier.read()
    fichier.close()
    dico = {}
    for lettre in contenu:
        if lettre in dico:
            dico[lettre]+=1
        else:
            dico[lettre]=1
    dico_sorted = sorted(dico.items(), key=lambda t: t[1],reverse=True)
    tab_noeud=[]
    for i in range(len(dico_sorted)):
        n=Noeud(dico_sorted[i][0],None,None,dico_sorted[i][1],0.)
        tab_noeud.append(n) 
    return tab_noeud

tab_noeud  = lire_fichier(nomfic)
print("tab_noeud=",tab_noeud)


"""
 Question 3: calcul des fréquences
"""

def frequence(tab_noeud):
    somme = 0
    for i in tab_noeud:
        somme+=i.nb_occur

    freq = dict()
    for i in tab_noeud:
        freq[i.lettre]=(i.nb_occur/somme)
    return freq

tab_freq = frequence(tab_noeud)
print("tab_freq=",tab_freq)


"""
Question 4: calcul de l'entropie
"""

def entropie(tab_noeud):
    e = 0.0
    freq = frequence(tab_noeud)
    for i in freq.values():
        e+=(-i*math.log(i,2))
    return e

h=entropie(tab_noeud)
print("entropie=",h)



"""
Question 5: Construction de l'arbre de Huffman
"""

def construit_arbre(tab_noeud):
    dio = dict()
    for i in range(len(tab_noeud)):
        
    return None


arbre=construit_arbre(tab_noeud)
print("arbre=",arbre)

"""
Question 6: Construction du dictionnaire de codage
"""

def construit_dico(noeud,prefixe,dico):
    return

dico_codage={}
construit_dico(arbre,"",dico_codage)
print(dico_codage)

"""
Question 7: longueur moyenne du code
"""

def longueur_moyenne(arbre,hauteur):
    return 0.

print("longueur moyenne=",longueur_moyenne(arbre,0))


"""
Question 8: Codage du fichier
"""

def codage(nomfic,dico_codage):
    return ""

c = codage(nomfic,dico_codage)
print("codage=",c)

