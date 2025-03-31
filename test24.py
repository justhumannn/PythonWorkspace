a,b = map(int,input().split())
c = []
b -= 1
b1 = b
d = []
for i in range(1,a+1):
    c.append(i)
for _ in range(a):
    d.append(str(c.pop(b)))
    for _ in range(b1):
        b += 1
    if b >= len(c):
        b -= len(c)
print('<'+', '.join(d)+'>')