import numpy as np
file=open("idDir.txt","w")
random=np.random.RandomState(1)
for i in range(40000):
	a=random.uniform(1,57)
	file.write(str(int(a))+"\n")
file.close()
