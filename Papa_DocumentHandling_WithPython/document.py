import sys


fileread = open(sys.argv[1], "r") 
string = sys.argv[2]
memory=[]
for line in fileread:
    print(line)
    memory.append(line.replace(string, ""))

fileread.close()

filewrite = open(sys.argv[1], "w")
for line in memory:
    print(line)
    filewrite.write(line.replace(string, ""))
filewrite.close()