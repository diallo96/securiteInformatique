"""
Nom et prénom 1: KONE Idriss Apollin
Nom et prénom 2: LIPARO Collin
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

noeudP2=Noeud('.',noeudO,noeudU,noeudO.nb_occur+noeudU.nb_occur,0.0)
noeudP3=Noeud('.',noeudI,noeudP2,noeudI.nb_occur+noeudP2.nb_occur,0.0)
noeudP4=Noeud('.',noeudE,noeudA,noeudE.nb_occur+noeudA.nb_occur,0.0)
noeudP5=Noeud('.',noeudP4,noeudP3,noeudP4.nb_occur+noeudP3.nb_occur,0.0)

print("noeudE=", noeudE)
print("noeudA=", noeudA)
print("noeudI=", noeudI)
print("noeudO=", noeudO)
print("noeudU=", noeudU)
print("noeudP2=", noeudP2)
print("noeudP3=", noeudP3)
print("noeudP4=", noeudP4)
print("noeudP5=", noeudP5)



"""
  Question 2: Décrire la fonction lire_fichier, en particulier ce qu'elle calcule.
  Répondez à la question 2 ici ou juste après la fonction.

  la fonction lire_fichier permet de lire un fichier texte passé en paramètre. ensuite
  elle affiche un tableau effectue un tri dans l'ordre décroissant 
  
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
    sommeTotale =0
    for i in range (len(tab_noeud)):
        sommeTotale +=(tab_noeud[i].nb_occur)
    Freq ={};
    for i in range (len(tab_noeud)):
         F=tab_noeud[i].nb_occur/sommeTotale
         Freq[tab_noeud[i].lettre]=F
    
    return Freq

a=frequence(tab_noeud)
print("frequence= ", a)



"""
Question 4: calcul de l'entropie
"""

def entropie(tab_noeud):
    e = 0.0
    freq=frequence(tab_noeud)
    """for i in range (len(freq)):"""
    for valeur in freq.values():
        e =e-valeur*math.log(valeur,2)
    return e

h=entropie(tab_noeud)
print("entropie=",h)



"""
Question 5: Construction de l'arbre de Huffman
"""

def construit_arbre(tab_noeud):
    
    while(len(tab_noeud)!=1):
           lastnoeud=Noeud('.',tab_noeud[len(tab_noeud)-2],tab_noeud[len(tab_noeud)-1],tab_noeud[len(tab_noeud)-2].nb_occur+tab_noeud[len(tab_noeud)-1].nb_occur,0.0);
           del tab_noeud[len(tab_noeud)-1];
           tab_noeud[len(tab_noeud)-1]=lastnoeud;
           tab_noeud = sorted(tab_noeud, key=lambda Noeud: Noeud.nb_occur ,reverse=True);
    return tab_noeud[0];


arbre=construit_arbre(tab_noeud)
print("arbre=",arbre)

"""
Question 6: Construction du dictionnaire de codage
"""

def construit_dico(noeud,prefixe,dico):
    if(noeud.fils_gauche==None):
        dico[noeud.lettre]=prefixe;
    else:
        construit_dico(noeud.fils_gauche,(prefixe+"0"),dico);
        construit_dico(noeud.fils_droite,(prefixe+"1"),dico);
        
    return dico

dico_codage={}
construit_dico(arbre,"",dico_codage)
print(dico_codage)

"""
Question 7: longueur moyenne du code
"""

def longueur_moyenne(arbre,hauteur):
    if(arbre.fils_gauche==None):
        return (hauteur)
    else:
        return (longueur_moyenne(arbre.fils_gauche,hauteur+1)*arbre.fils_gauche.nb_occur+longueur_moyenne(arbre.fils_droite,hauteur+1)*arbre.fils_droite.nb_occur)/(arbre.nb_occur)
    

print("longueur moyenne=",longueur_moyenne(arbre,0))


"""
Question 8: Codage du fichier
"""

def codage(nomfic,dico_codage):
    fichier = open(nomfic,"r")
    contenu  = fichier.read()
    fichier.close()
    code=""
    for lettre in contenu:
            code=code+dico_codage[lettre]    
    return code

c = codage(nomfic,dico_codage)
print("codage=",c)

