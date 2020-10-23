import codecs
import re
from collections import Counter

alphabet='абвгдежзийклмнопрстуфхцчшщыьэюя'

def OpenF(file):
 file_o=codecs.open(file,"r","utf-8")
 text=file_o.read()
 return text;

def Index(text):
    diction=Letter_counter(text)
    n=len(text)
    i=0
    for key in diction:
        i+=diction[key]*(diction[key]-1)
    i=i*(1/(n*(n-1)))
    return i

def Couple(text): 
    length=len(text)-1
    couples=[]
    for item in range(0,length,2):
        couples.append(text[item:item+2])    
    return couples
def Letter_counter(text):
    count=Counter(text)
    return count;

def makeXY(lst):
    x=0
    m=31
    newLst=[]
    for i in range (len(lst)):
        x=lst[i][0]*m+lst[i][1]
        newLst.append(x)
    return newLst
def Lst(lst):
    List=[]
    for i in range(5):
        for key in alp:
            if lst[i][0]==key:
                a=alp[key]
            if lst[i][1]==key:
                b=alp[key]
        List.append(tuple((a,b)))
    return List
    
#main
lst1=['ст','но','то','на','ен']
#open + mc
F=OpenF("V7.txt")
couples=Couple(F)
a=Letter_counter(couples)
b=a.most_common(5)
lst2=[]
for i in range(5):
    lst2.append(b[i][0])
print(lst2)
##
values=list()
for value in range(31):
    values.append(value)
alp={}
alp=dict(zip(alphabet,values))
##
#L1-mova L2-text
L1=Lst(lst1)
L2=Lst(lst2)
print(L1)
print(L2)
#
X=makeXY(L1)
Y=makeXY(L2)
print(Y)
print(X)



