import math
import random
import binascii
def GCD(p,x): 
   while(x): 
       p,x = x,p % x 
   return p
def GenerateP(n):
    p=2**(n-1)
    k=0
    for i in xrange(n-2,0,-1):
        k=random.randint(0,1)
        p+=((2**i)*k)
    p+=1
    return math.trunc(p)

def FindDS(p):
    p=p-1
    i=0
    while(p%2==0):
        p=p/2
        i+=1
    return p,i

def TESTMillerRabin(p,k):
    if p==2:
        return True
    for i in  (2,3,5,7):
        if p%i==0:
            return False
    s=FindDS(p)[1]
    d=FindDS(p)[0]
    
    for one in xrange(k):
        x = random.randrange(10, p - 1)
        gcd=GCD(p,x)
        if gcd==1:
            continue
        else:
            return False
            break
        a = pow(x, d, p)
        if a == 1 or a == p - 1:
            continue
        for two in xrange(s - 1):
            a = pow(x, 2, p)
            if a == p - 1:
                break
        else:
            return False
    return True

def GenPQ(n):
    L=[]
    for i in xrange(4):
        a=False
        while(a==False):
            p=GenerateP(n)
            a=TESTMillerRabin(p,50)
        L.append(p)
    L.sort()
    return L

def ReverseE(e,fn):
    if fn==0:
        return e,1,0
    else:
        gcd,x,y=ReverseE(fn,e%fn)
        return gcd,y,x-y*(e//fn)

def GenerateKeyPair(p,q):
    n=p*q
    fn=(p-1)*(q-1)
    e=pow(2,16)+1
    if GCD(e,fn)==1:
        d=ReverseE(fn,e)[1]
    if d<0:
        d=fn+d
    return (d,p,q),(n,e)

def HEX(text):
    t=[]
    t1=''
    for sym in text:
        t1=hex(ord(sym))
        t1=int(t1,16)
        t.append(t1)
    return t


def Encrypt(msg,pkey):
    n=pkey[1][0]
    e=pkey[1][1]
    print(" TEXT NUM: ",msg)
    print()
    C=pow(msg,e,n)
    print ("C",C)
    print
    return C

def Decrypt(cmsg,key):
    n=key[1][0]
    d=key[0][0]
    M=pow(cmsg,d,n)
    print ("M",M)
    return M

def Sign(msg,key):
    d=key[0][0]
    n=key[1][0]
    S=pow(msg,d,n)
    return (msg,S)

def Verify(sign,key):
    n=key[1][0]
    e=key[1][1]
    M=pow(sign,e,n)
    return (M,S)

def SendKey(Akey,Bkey):
    e,n=Akey[1][1],Akey[1][0]
    d=Akey[0][0]
    e1,n1=Bkey[1][1],Bkey[1][0]
    k=random.randrange(1,n-1)
    k1=Encrypt(k,Bkey)
    S=Sign(k,Akey)[1]
    S1=Encrypt(S,Bkey)
    return (k1,S1)


def ReciveKey(smsg,Bkey,Akey):
    k=Decrypt(smsg[0],Bkey)
    S=Decrypt(smssg[1],Bkey)
    ka=Encrypt(S,Akey)
    return()






PQ=GenPQ(256)
p=PQ[0]
q=PQ[2]
p1=PQ[1]
q1=PQ[3]
Akey=GenerateKeyPair(p,q)
Bkey=GenerateKeyPair(p1,q1)
print(Akey)
text=random.randrange(1,500)

txt=Encrypt(text,Akey)
aaa=Decrypt(txt,Akey)
txt1=Encrypt(aaa,Akey)

e=122
fn=277
d=ReverseE(e,fn)[1]
d=fn+d
print("D---",d)
print("E---",ReverseE(d,fn)[1])

k=SendKey(Akey,Bkey)
print(k)







