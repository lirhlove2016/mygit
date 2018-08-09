import os
path=os.getcwd()

print(path)

file=path+'/data.txt'
print(file)

with open(file,encoding='UTF-8') as fr:
        lines2=fr.readlines()
        print(lines2)
