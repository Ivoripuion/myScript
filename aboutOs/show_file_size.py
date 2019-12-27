import os
from os.path import join, getsize

def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name)) for name in files])
    return size


if __name__ == '__main__':
    size_array={}

    all_dirs="C:\\Program Files (x86)"
    for dir in os.listdir(all_dirs):
        tar_dir=os.path.join(all_dirs,dir)
        filesize = getdirsize(tar_dir)

        size_array.update({tar_dir:filesize})

        #print('There are %.3f' % (filesize / 1024 / 1024 ), 'Mbytes in ',tar_dir)

    sorted_dirlist=sorted(size_array.items(),key=lambda x:x[1])
    #print(sorted_dirlist)
    for pair in sorted_dirlist:
        print(pair[0],"size\t%.3f"%(pair[1]/ 1024 / 1024),"MB")