# -*- coding:utf-8 -*-

S=[]
key="abcdef"
keylength=len(key)
child_key=[]
plaintext="hello who are you"
ciphertext=[]

def KSA():
    for i in range(256):
        S.append(i)

    j=0
    for i in range(256):
        j=(j+S[i]+ord(key[i%keylength]))%256
        S[j],S[i]=S[i],S[j]

def PRGA():
    i=0
    j=0
    for m in plaintext:
        i=(i+1)%256
        j=(j+S[i])%256
        S[i],S[j]=S[j],S[i]
        t=(S[i]+S[j])%256
        k=S[t]
        child_key.append(k)

def encrypt():
    print("加密：",end="")
    for (m,n) in zip(plaintext,child_key):
        ciphertext.append(ord(m)^n)
    for i in ciphertext:
        print(i,end=",")
    print()

def decrypt():
    print("解密：",end="")
    for (m,n) in zip(ciphertext,child_key):
        print(chr(m^n),end="")
    print()

KSA()
PRGA()
print("子密钥流：",child_key)
encrypt()
decrypt()