import codecs
import re
from collections import Counter

alphabet=['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
alp='абвгдежзийклмнопрстуфхцчшщъыьэюя'

def Open_file(file):
 file_o=codecs.open(file,"r","utf-8")
 text=file_o.read()
 text=text.lower()
 text=text.replace('ё','е')
 #.replace('ъ','ь')
 regular=re.compile('[^а-яА-Я]')
 text=regular.sub('',text)
 #print(text)
 return text;

def Keys(num):
    if num in range(2,6):
        if num==2:
            key='та'
        if num==3:
            key='род'
        if num==4:
            key='сова'
        if num==5:
            key='каноэ'
    else:
        key='абстракционизм'
    return key;

def Encr(text,alp,key):
    values=list()
    numbers=list()
    new_text=''
    for value in range(32):
            values.append(value)
    dictionary={}
    dictionary=dict(zip(alp,values))
    for item in range(len(text)):
            #print(i)
            a=(dictionary[text[item]]+dictionary[key[item]])%len(alp)
            #print(item)
            #print(key[item])
            numbers.append(a)
    for num in numbers:
       for key in dictionary:
            if num==dictionary[key]:
                new_text+=key
    #print(numbers)
    return new_text;

def BigKey(key,text):
    Big_key=''
    for i in range(len(text)):
            Big_key+=key[i%len(key)] 
    #print(Big_key)
    return Big_key;
def Print_encr(num,T):
    print()
    print('KEY:', Keys(num))
    print('r =',num)
    Big_key=BigKey(Keys(num),T)
    print("ENCRYPTED TEXT")
    encr_text=Encr(T,alp,Big_key)
    print(encr_text)
    
def Enc_value(num,T):
    Big_key=BigKey(Keys(num),T)
    encr_text=Encr(T,alp,Big_key)
    return encr_text
    
#COUNT
def Letter_counter(text):
    count=Counter(text)
    return count;

def Index(diction,n):
    i=0
    for key in diction:
        i+=diction[key]*(diction[key]-1)
    i=i*(1/(n*(n-1)))
    return i

def Index_check(diction,length):
    index=0
    for key in diction:
        diction[key]=diction[key]/length
        index+=diction[key]*diction[key]
    return index
def Print_index(text,n,num):
    dic=Letter_counter(text)
    index=Index(dic,len(text))
    print('INDEX FOR TEXT')
    if n==2:
        print('With key length ',num)
    print('I(Y) = ',index)
    if n==1:
        M=Open_file("text.txt")
        dic_M=Letter_counter(M)
        index_ch=Index_check(dic_M,len(M))
        print('MI(Y) = ',index_ch)
        
    print()
    
    

#main
print("TASK 1")
print()
print("TEXT")
T=Open_file("1.txt")
print(T)
print()
for i in range(2,7,1):
    if i==6:
        Print_encr(14,T)
    else:
        Print_encr(i,T)
    
print("TASK 2")
print()
for i in range(1,7):
    if i==1 or i==6:
        if i==1:
            Print_index(T,1,0)
        else:
            Print_index(Enc_value(14,T),2,14)
    else:
        Print_index(Enc_value(i,T),2,i)
        
    








    
