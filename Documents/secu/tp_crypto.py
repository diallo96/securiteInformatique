# -*-coding:Latin-1 -*

from random import randint
from math import log

#********************
#
# fonctions arithmï¿½tiques
#
#********************

def euclid_it(a,b):
    a = abs(a)
    b = abs(b)
    if(b==0):
        return a
    else:
        rest = a%b
        return euclid(b,rest)

def euclid(a,b):
    a = abs(a)
    b = abs(b)
    while b!=0:
        a, b = b, a%b
    return a

print("****** euclid ******")
print(euclid(0,15) == 15)
print(euclid(15,0) == 15)
print(euclid(15,9) == 3)
print(euclid(9,15) == 3)
print(euclid(-9,15) == 3)
print(euclid(9,-15) == 3)
print(euclid(-9,-15) == 3)
print(euclid(1000,1) == 1)

print("****** euclid Itï¿½ratif ******")
print(euclid_it(0,15) == 15)
print(euclid_it(15,0) == 15)
print(euclid_it(15,9) == 3)
print(euclid_it(9,15) == 3)
print(euclid_it(-9,15) == 3)
print(euclid_it(9,-15) == 3)
print(euclid_it(-9,-15) == 3)
print(euclid_it(1000,1) == 1)


def extended_euclid(a,b):
    u = 1; uu = 0
    v = 0; vv = 1
    while b!=0:
    	q = a//b
    	a, b = b, a%b
    	uu, u = u - q*uu, uu
    	vv, v = v - q*vv, vv
    if(a<0):
        a = -a
        u = -u
        v = -v
    return a,u,v


print("****** extencded_euclid ******")
a=0
b=15
d,u,v = extended_euclid(a,b)
print( d>=0 and a*u+b*v==d)
a=15
b=0
d,u,v = extended_euclid(a,b)
print( d>=0 and a*u+b*v==d)
a=15
b=9
d,u,v = extended_euclid(a,b)
print( d>=0 and a*u+b*v==d)
a=9
b=15
d,u,v = extended_euclid(a,b)
print( d>=0 and a*u+b*v==d)
a=-15
b=9
d,u,v = extended_euclid(a,b)
print( d>=0 and a*u+b*v==d)
a=-9
b=-15
d,u,v = extended_euclid(a,b)

print( d>=0 and a*u+b*v==d)
a=1000
b=1
d,u,v = extended_euclid(a,b)
print( d>=0 and a*u+b*v==d)


def modular_inverse(a,n):
    x, y, z = extended_euclid(a,n)
    if(x!=1):
        return 0
    elif(y<0):
        return y+(abs(n))
    else:
        return y

print("****** modular_inverse ******")
print(modular_inverse(7,13)==2)
print(modular_inverse(7,-13)==2)
print(modular_inverse(-7,13)==11)
print(modular_inverse(-7,-13)==11)
print(modular_inverse(0,13)==0)
print(modular_inverse(8,14)==0)


def naive_euler_function(n):
	if(n==1):
		return 1
	else:
		j=0
		for i in range(1,n):
			if(euclid(n,i)==1):
				j+=1
	return j

print("****** naive_euler_function ******")
print(naive_euler_function(2)==1)
print(naive_euler_function(3)==2)
print(naive_euler_function(4)==2)
print(naive_euler_function(5)==4)
print(naive_euler_function(6)==2)
print(naive_euler_function(7)==6)
print(naive_euler_function(8)==4)
print(naive_euler_function(9)==6)
print(naive_euler_function(10)==4)
print(naive_euler_function(11)==10)
print(naive_euler_function(12)==4)


def euler_function(L1,L2):
	prod = 1
	for i in range(len(L1)):
		prod*=(L1[i]**L2[i])
	return naive_euler_function(prod)

print("****** euler_function ******")
L1 = [2,3,5,7]
L2 = [1,2,3,1]
n= 1
for i in range(len(L1)):
    n*=L1[i]**L2[i]
print(euler_function(L1,L2)==naive_euler_function(n))


def inversibles(n):
    L=[]
    for i in range(1,(n)):
    	if(euclid(n,i)==1):
    		L.append(i)
    return L

print("****** inversibles ******")
n=30
L = inversibles(n)
L=list(set(L))
test = True
for i in L:
    test= test and (euclid(i,n)==1)
test = test and (len(L)==naive_euler_function(n))
print(test)


def ordre(a,n):
    if(euclid(a,n)==1):
        k=1
        while(((a**k)%n)!=1):
            k+=1
        return k

print("****** ordre ******")
a=3
n=17
o=ordre(a,n)
r=a
k=1
test= (o>0) and (o<n)
while(k<o and test):
    test = test and (r!=1)
    k+=1
    r= (r*a)%n
test = test and (r==1)
print(ordre(3,17))
print(test)


def generateur(n):
    phi = naive_euler_function(n)
    res = 0
    for i in range(1,n-1):
        if(ordre(i,n)==phi):
            res = i
    if(res!=0):
        return res
    else:
        return 0

"""
print("****** generateur ******")
print (" (Z/nZ)* est cyclique si et seulement si n = 4, ou une puissance d'un premier impair, ou le double d'une telle puissance")
L=[8,12,15,16]
test=True
for n in range(2,20):
    a = generateur(n)
    if (n in L):
        if(a!=0):
            test=False
    else:
        if(a==0):
            test=False
        else:
            if(euclid(a,n)!=1):
                test=False
            else:
                phi=naive_euler_function(n)
                o = ordre(a,n)
                test=test and (o==phi)

print(test)
"""

def naive_exponentiation(a,k,n):
    res = 1
    for i in range(k):
        res = (res*a)%(abs(n))
    return res


print("****** naive_exponentiation ******")
print(naive_exponentiation(2,0,10)== 2**0 %10,' ',naive_exponentiation(2,0,10))
print(naive_exponentiation(2,1,10)== 2**1 %10,' ',naive_exponentiation(2,1,10))
print(naive_exponentiation(2,6,10)== 2**6 %10,' ',naive_exponentiation(2,6,10))
print(naive_exponentiation(-2,6,10)== (-2)**6 %10,' ',naive_exponentiation(-2,6,10))
print(naive_exponentiation(2,6,-10)== 2**6 % 10,' ',naive_exponentiation(2,6,-10))


def square_and_multiply(a,k,n):
    
    return 0

"""
print("****** square_and_multiply ******")
print(square_and_multiply(2,0,10)== 2**0 %10)
print(square_and_multiply(2,1,10)== 2**1 %10)
print(square_and_multiply(2,30,10)== 2**30 %10)
print(square_and_multiply(-2,30,10)== (-2)**30 %10)
print(square_and_multiply(2,30,-10)== 2**30 % 10)
"""


# Cette fonction retourne (x^y)%p
def exponentiel(x, y, p):
    res = 1
    x = x%p # si x>=p on calcule son modulo avant de l'élever à ^y 
    while(y>0):
        if(y & 1): # Si y est impair
            res = (res * x) % p
        y = y>>1 # y/2 (comme y est pair), qui est une division entière
        x = (x * x) % p
    return res

#Cette fonction retourne False si n est composite
# (n est divisible par au moins un entier autre que 1 et lui-même)
# ou si n est probablement premier
# d est impair

def testMillerRabin(d, n):
    #choix du nombre aléatoire entre [2..n-2]
    #il faut que n soit supérieur à 4
    a = 2 + randint(1, n-4)
    # x = a^d % n
    x = exponentiel(a, d, n)

    if(x==1 or x == n-1):   
        return True
    #on fait la boucle tant qu'aucune des conditions suivantes n'est
    #respectée:
    # 1) d n'atteint pas n-1
    # 2) x^2 % n est différent de 1
    # 3) x^2 % n est # de n-1
    while(d != n-1):
        x = (x * x) % n
        d*=2

        if(x==1):
            return False
        if(x == n-1):
            return True
    #retourne composite
    return False

def miller_rabin(n,k):
    if(n<= 1 or n==4):
        return False
    if(n<=3):
        return True

    d = n-1
    while(d%2==0):
        d//=2

    for i in range(k):
        if(testMillerRabin(d,n)==False):
            return False
    return True
"""
print("****** miller_rabin ******")
p=40
for n in range(2,50):
    print ("miller_rabin(",n,",",p,")=",miller_rabin(n,p))
"""

def generate_prime(k,d):
    n = randint(2**(k-1), (2**k))
    while(miller_rabin(n,d)==False):
        n = randint(2**(k-1), (2**k))
    return n
"""
print("****** generate_prime ******")
L=[2,3,4,5,10,20,30,40,50,100,200,500,1000]
for k in L:
    n = generate_prime(k,40)
    print(miller_rabin(n,40) and n>=2**(k-1) and n<2**k)
    print(n)
"""




#********************
#
# fonctions liï¿½es au RSA
#
#********************

def generate_key(k):
    p,q,n,phin,d,e=0,0,0,0,0,0
    p=generate_prime(k/2,40)
    q=generate_prime(k/2,40)
    n=p*q
    phin=(p-1)*(q-1)
    e=randint(1,phin)
    while(euclid(e,phin)!=1):
        e=randint(1,phin)
    d=modular_inverse(e,phin)
    return p,q,n,phin,d,e

print("****** generate_key ******")
k=1000
k2 = k//2
p,q,n,phin,d,e=  generate_key(k)
print("p premier:", miller_rabin(p,80))
print("q premier:", miller_rabin(q,80))
print("p!=q:", p!=q)
print("p et q ont ",k2," bits:", p<2**k2 and p>=2**(k2-1) and q<2**k2 and q>=2**(k2-1))
print("pq == n : ", p*q==n)
print("n a ",k," bits:", n<2**k and n>=2**(k-1))
print("(p-1)*(q-1) == phin : ", (p-1)*(q-1) == phin)
print("PGCD(e,phin)==1: ", euclid(e,phin) == 1)
print("ed =1 mod phin", (e*d) % phin  == 1)


def encipher(m,n,e):
    return pow(m, e)%n

def decipher(c,n,d):
    return exponentiel(c, d)%n

print("****** cipher and decipher ******")
m=12
c = encipher(m,n,e)
print("chiffrement de ",m,":", c)
print("dï¿½chiffrement de ",c,":", decipher(c,n,d))



#********************
#
# fonctions sur les courbes elliptiques
#
#********************



"""
ATTENTION: toutes les fonctions qui suivent n'ont pas
de fonction de test ï¿½ la fin du fichier
"""


def verifie_point(A,B,p,P):
    return False

def addition_points(A, B, p, P, Q):
    return (0,0,0)

def groupe_des_points(A, B, p):
    return []

def generateurs_EC(A, B, p):
    return []

def double_and_add(A, B, p, P, k):
    return (0,0,0)

"""
rï¿½pondre ici aux items 1,2,3 pour la courbe P256
"""

#item 1

#item 2

#item 3


def diffie_hellman_P256(p,n,B,Gx,Gy):
    return None

def ECDSA_P256(p,n,B,Gx,Gy):
    return None



#********************
#
# fonction de factorisation lorsque l'exposant secret est petit
#
#********************

def small_exponent(N,e):
    return 0




"""
print("****** CRT ******")
L1=[5,9,17,16]
L2=[1,2,3,4]
R= CRT(L1,L2)
test=True
for i in range(len(L1)):
    test = test and (R%L1[i] == L2[i])
print(test)
"""



"""
print("****** generate_key_CRT ******")
k=1000
k2 = k//2

p,q,n,phin,d,dp,dq,invp,invq,e=  generate_key_CRT(k)
print("p premier:", miller_rabin(p,40))
print("q premier:", miller_rabin(q,40))
print("p et q ont ",k2," bits:", p<2**k2 and p>=2**(k2-1) and q<2**k2 and q>=2**(k2-1))
print("pq == n : ", p*q==n)
print("n a ",k," bits:", n<2**k and n>=2**(k-1))
print("(p-1)*(q-1) == phin : ", (p-1)*(q-1) == phin)
print("PGCD(e,phin)==1: ", euclid(e,phin) == 1)
print("ed =1 mod phin", (e*d) % phin  == 1)
print("dp = d mod p-1 : ", dp == (d % (p-1)))
print("dq = d mod q-1 : ", dq == (d % (q-1)))
print("p * invp = 1 mod q: ", p*invp % q ==1)
print("q * invq = 1 mod p: ", q*invq % p ==1)
"""

"""
print("****** cipher and decipher_CRT ******")

m=12
c = encipher(m,n,e)
print("chiffrement de ",m,":", c)
print("dï¿½chiffrement de ",c,":", decipher_CRT(c,n,p,q,dp,dq,invp,invq))
"""



"""
print("****** small_exponent ******")
print("Gï¿½nï¿½ration d'une mauvaise bi-clï¿½")
k=2048
n= 16747165677462056268129145673947726240459167554525390427207159395993453000412183817298102860527898142910980701588445020644941145805116775073182765201051830658288067723342446665847168294157719004570163135739276668828351930479547412612594135619543858901369062191314795450495428380522108074218794060535536356592138121107663286013519189114238869709616935920389316831813468517260484298689301155973125504906656085030120148402632309215701203906133026921718504369385331652360593110141946503363972583239132180748669819595559600472615134122497474549146510790007668803843600381198681082882364826755976582516613910936975979013871
e=11128373102609799542544441302828906185353756638043397894550913960194075754391596859914258000621295742150055322916626918812199599007226691503109252865552440406874266822913138293576453618640005259030355795466109735043635474571938327025321393788952398379938372959756973855938843546304843025021648701455601779381263630943136784777192178949701863346353125979113684616665675341188420144284801542794261168962580808715631317706540116396413898324366850057883144232844701629915163397237632971224152403270060682881415062296916011400455119942247206772358262213758789471499399657187276847642522521737818722671274821976773800747647
d= 113012046295998254056212353895685804770209460690814597059625630226095001152430229979116178525589683080297406306375886790863

print("Nombre de bits:",k)
print("Nombre de bits de la clï¿½ secrï¿½te:", int(log(d,2))+1)

dprime=small_exponent(n,e)
print("small exponent:", dprime)
print("test ï¿½galitï¿½:", d==dprime)
"""
