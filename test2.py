a = int(input())
d = []
e = []
for _ in range(a):
    d = []
    b = input()
    for _ in range(2):
        c = b.find(' ')
        d.append(' ')
        d.append(b[0:c])
        b = b[c + 1:]
    e.append(b + d[0] + d[1] + d[2] + d[3])
for i in range(0,a):
    print(e[i])