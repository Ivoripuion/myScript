import zipfile
import sys
import os 
import rsa
import shutil
from shutil import copyfile

#加密
def encrypt(m):
    (pubkey, privkey) = rsa.newkeys(1024)
    
    with open('public.pem','w+') as f:
        f.write(pubkey.save_pkcs1().decode())
    with open('private.pem','w+') as f:
        f.write(privkey.save_pkcs1().decode())

    c = rsa.encrypt(m.encode(), pubkey)

    return c


#创建txt
def mktxt():
    en_file=open(".\\sample\\message.txt","wb+")
    en_file.write(encrypt("wrsndm"))#隐藏的数据
    en_file.close()

#解压docx
def unzip():    
    copyfile(".\\test.docx",".\\sample.zip")
    zFile = zipfile.ZipFile(".\\sample.zip", "r")
    for fileM in zFile.namelist(): 
        zFile.extract(fileM, ".\\sample")
    zFile.close()
    os.remove(".\\sample.zip")

# 压缩docx 
def zip_docx(startdir, file_news):
    mktxt()
    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath+filename)
    z.close()

unzip()
zip_docx(".\\sample", "sample.docx")
shutil.rmtree(".\\sample")