import os
import shutil 
def cp_test(filename):
	shutil.copy(filename,'E:\Python_work\cp_test')#将要复制或者剪切的目标路径，剪切时目标文件夹不能存在一样的文件
def gci(filepath):
	files=os.listdir(filepath)
	for fi in files:
		fi_d=os.path.join(filepath,fi)
		if os.path.isdir(fi_d):
			gci(fi_d)
		else:
			cp_test(fi_d)
def main():
	gci('E:\Python_work\cp_test_1')#将要复制或者剪切的源路径
if __name__=='__main__':
	main()