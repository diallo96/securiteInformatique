import random
import math


def median(S):
    R = []
    k = 3/4
    n = len(S)
    for i in range(1,int(pow(n,k))):
        ran = random.randint(0,int((n**k)-1))
        R.append(S[ran])

    R.sort()
    rgA = max(1, int(((n**k)/-math.sqrt(n))))
    rgB = min(int(((n**k)/2)+math.sqrt(n)), int(n**k)-1)
    P = []
    #a = R[rgA-1]
    #b = R[rgB-1]
    print(rgA-1," ",rgB-1," ",n)
    rA = 1
    rB = 1
    for i in range(0,n-1):
        if((R[rgA-1]<=S[i]) and (R[rgB-1]>=S[i])):
            P.append(S[i])
        if((S[i]<R[rgA-1])):
           rA = rA+1
        if((S[i]<R[rgB-1])):
           rB = rB+1

    if((rA>(n/2))):
        return "A"
    if(rB<(n/2)):
       return "B"
    if((len(P)>=(4*n**k))):
       return "P"
    P.sort()

    if (n%2==0):
       c = P[int(n/2)-(rA)]
       return c
    else:
       c = P[int(n/2)-(rA)+1]
       return c


tab = [1,0,5,-8,3,-1,4,10,5,7,8,-2,-5,-16]
for i in range(10):
    res = median(tab)
    print("mediane : ",res)
    

def partition(tab, g, d, pivot):
    val_pivot = tab[pivot]
    tmp = tab[pivot]
    tab[pivot]=tab[d]
    tab[d]=tmp
    pos_insert = g
    print("pivot = ",val_pivot)
    print(tab)
    for i in range(g, d):
        if(tab[i]<val_pivot):
            tmp2 = tab[pos_insert]
            tab[pos_insert] = tab[i]
            tab[i] = tmp2
            pos_insert+=1
    tmp3 = tab[d]
    tab[d] = tab[pos_insert]
    tab[pos_insert] = tmp3
    return pos_insert

def quickSelect(tab, g, d):
    if(g==d):
        return tab[g]
    pivot = g
    n = len(tab)
    pivot = partition(tab, g, d, pivot)
    if(pivot == math.ceil(n/2)):
        return tab[pivot]
    if(pivot<math.ceil(n/2)):
        return quickSelect(tab, pivot+1, d)
    else:
        return quickSelect(tab, g, pivot-1)
        

res = quickSelect(tab, 0, len(tab)-1)
print("QuickSelect :", res)
print("median", sorted(tab)[int(math.ceil(len(tab))/2)])
