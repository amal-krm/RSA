from decimal import Decimal 
import random

# calculer pgcd
def pgcd(a,b) :  
   while a%b != 0 : 
      a, b = b, a%b 
   return b

def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
	    return False
    return True

#generer un nbre premier      
def generatePrime():
    while 1:
        i = random.randrange( 1000,2000)
        if is_prime_number(i):
            #print(i)
            return i

def finding_E(phi):
    e=2
    while 1:
        if(pgcd(e,phi) == 1) :
            print("e is :" + str(e))
            return e
        else :
            e=e+1

def Crypter(message , e , n) :
    mymsg = tuple(message)
    conversion=[]
    for x in mymsg:
        x=pow((ord(x)-96),e)%n
        conversion.append(x)
    print("Le message ' " + str(message) + " ' crypte est :")
    for x in conversion :
        print(str(x), end=' ')
    return (conversion)
def DeCrypter(conversion , d , n) :
    msg=[]
    for x in conversion:
        x=pow(x,d)%n
        x=x+96
        msg.append(chr(x))
    print("Le message est :")
    for x in msg :
        print(str(x), end='')
def generateD(e , phi):
    k=2
    d=0
    temp=0
    while 1 :
        temp =(k*phi)+1
        if temp % e == 0:
            d =int(temp/e)
            print("d is :" + str(d))
            return d
        else :
            k=k+1
p = generatePrime()
q = generatePrime()
while p==q :
    p = generatePrime()
    q = generatePrime()
print("p is "+ str(p))
print("q is " + str(q))
n = p*q
phi = (p-1)*(q-1)
e = finding_E(phi)
print("Votre cle public est ("+ str(n)+","+str(e)+ ").")
msgCrypter = Crypter("hello world" , e,n)
print("\ndecrypter ...")
d = generateD(e , phi)
DeCrypter(msgCrypter ,d ,n)

