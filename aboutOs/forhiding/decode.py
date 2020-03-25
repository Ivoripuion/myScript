import zipfile
import sys
import os 
import rsa
import shutil
from shutil import copyfile

with open('private.pem','r') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())

#解压docx
def unzip():    
    copyfile(".\\sample.docx",".\\sample.zip")
    zFile = zipfile.ZipFile(".\\sample.zip", "r")
    for fileM in zFile.namelist(): 
        zFile.extract(fileM, ".\\sample")
    zFile.close()
    os.remove(".\\sample.zip")

#解密并打印message
def get_message():
    c = open('.\\sample\\message.txt','rb+').read()
    message = rsa.decrypt(c, privkey).decode()
    print(message)

unzip()
get_message()
shutil.rmtree(".\\sample")