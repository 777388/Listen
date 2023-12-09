import sys
G = []
for char in sys.argv[1]:
    for i in range(len(sys.argv[1])):
        b = i%4
        if (b == 0):
            G.append(i + i)
            G.append(ord(sys.argv[1][i]))
        elif (b == 1):
            G.append(i)
            G.append(ord(char))
        elif (b == 2):
            G.append(i-G[0])
            G.append(ord(sys.argv[1][i-G[0]]))
        elif (b == 3):
            G.append(i)
            G.append(ord(sys.argv[1][i^i]))
bin = lambda e: print(e, end="")
fin = lambda g: print(ord(sys.argv[1][g%(len(sys.argv[1]))])*g%(len(sys.argv[1])), end="")
(list(map(bin, G)))
(list(map(fin, G)))
print("")