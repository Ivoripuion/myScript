still_1="225"
file = open('myDir.txt','w')
for i in range(1,1000):
    file.write(still_1+("%03d" % i)+'\n')
file.close()