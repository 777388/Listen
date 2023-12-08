import sys
import os
b = []
for i in range(int(sys.argv[1])):
    b.append(i)
A = lambda AB: print(str(AB)+"-"+str(A)+" == "+str(A)+" "+str(sys.argv[2]), end="")
while True:
    print(list(map(A, b)), end="")

