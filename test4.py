a = int(input())
c = 0
d = []
b = list(map(int,input().split()))
for i in range(0,a):
    d.append(b[i])
for i in range(a-1,-1,-1):
    c += b[i]
    for j in range(0,i):
        c += b[j]
        d.append(c)
        for l in range(j + 1, i):
            c -= b[l]
            d.append(c)
            c = b[i] + b[j]
        c = b[i]
        c -= b[j]
        d.append(c)
        c = b[i]
c = 0
f = 0
for i in range(a):
    c += b[i]
for i in range(1,c + 1):
    e = d.count(i)
    if e == 0:
        print(i)
        f += 1
print(f)
print(d)