import os
import math
import random

m=[0,1,1,0]

def encode(m):
    s1=(int(m[0])+int(m[1])+int(m[3]))%2
    s2=(int(m[0])+int(m[2])+int(m[3]))%2
    s3=(int(m[1])+int(m[2])+int(m[3]))%2
    return [s1,s2,int(m[0]),s3,int(m[1]),int(m[2]),int(m[3])];
    

print(encode(m));


def canal(x,p):

    for i in range (len(x)):
        y=random.random()
        if(y<p):
            if(x[i]==0):
               x[i]=1
            else:
               x[i]=0
    return x;

print(canal([0,1,1,1,0],0.3))
def synfrome(y):
    s1=(y[2]+y[4]+y[6])%2
    s2=(y[2]+y[5]+y[6])%2
    s3=(y[4]+y[5]+y[6])%2
    return [s1,s2,s3]

y=[1,0,1,1,0,0,0]
x=[1,0,1,1,0,0,0]
o=[1,0,1,1,0,0,0]
s=[1,1,0]
def correction(y,s):
    x=0;
    if(s[0]!=y[0]):
        x=x+1
    if(s[1]!=y[1]):
        x=x+2
    if(s[2]!=y[3]):
        x=x+4
    if(x!=0):
        if(y[x-1]==0):
            y[x-1]=1
        else:
            y[x-1]=0
    return y;

print(correction(y,s));

n=1; bin(n)[2:]
print(bin(n))
print( [int(c) for c in bin(n)[2:]])

def dico_hamming():
    dico={}
    i=0
    while i!=16:
        x=0
        if((len(bin(i)[2:]))==1):
          x=[0,0,0,bin(i)[2:]]
        if((len(bin(i)[2:]))==2):
          x=[0,0,bin(i)[2],bin(i)[3]]
        if((len(bin(i)[2:]))==3):
          x=[0,bin(i)[2],bin(i)[3],bin(i)[4]]
        if((len(bin(i)[2:]))==4):
          x=bin(i)[2:]
        dico[bin(i)[2:]]=encode(x)
        i=i+1
    return dico;

print(dico_hamming())

def dist_hamming(x,y):
    dist=0
    for i in range(len(x)) :
        if(x[i]!=y[i]):
            dist=dist+1
    return dist

print(dist_hamming(x,o));

def dist_minimale(k):
   r=len(dico_hamming()[k[0]]);
   for i in range (len(k)):
       for j in range (len(k)):
          if (dist_hamming(dico_hamming()[k[i]],dico_hamming()[k[j]])!=0 and dist_hamming(dico_hamming()[k[i]],dico_hamming()[k[j]])<r):
             r=dist_hamming(dico_hamming()[k[i]],dico_hamming()[k[j]])
   return r;
Bo=["1001","1000"];
print(dist_minimale(Bo));


def factoriel(n):
    if (n==0):
        return 1
    else:
        return factoriel(n-1)*n

print(factoriel(3))


def binome(n,i):
    return (factoriel(n))/((factoriel(n-i))*(factoriel(i)))


print (binome(3,2))


def calcul_proba(n,p,e):
    if(e==0):
        return (binome(n,0))*(p**0)*((1-p)**(n-0))
    return (((binome(n,e))*(p**e)*((1-p)**(n-e)))+calcul_proba(n,p,e-1))
print(calcul_proba(7,0.25,1))
