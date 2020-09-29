import codecs
import re
from itertools import cycle
alphabet=['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']

def Open_file(file):
 file_o=codecs.open(file,"r","utf-8")
 text=file_o.read()
 text=text.lower()
 text=text.replace('ё','е')
 #.replace('ъ','ь')
 regular=re.compile('[^а-яА-Я]')
 text=regular.sub('',text)
 print(text)
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


alp='абвгдежзийклмнопрстуфхцчшщъыьэюя'

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
def Menu(num,T):
    print()
    print('KEY: ', Keys(num))
    Big_key=BigKey(Keys(num),T)
    print("ENCRYPTED TEXT")
    print(Encr(T,alp,Big_key))

    



#main
print("ENCRYPTED TEXT")
T=Open_file("1.txt")
Menu(2,T)
Menu(3,T)
Menu(4,T)
Menu(5,T)
Menu(14,T)






    
