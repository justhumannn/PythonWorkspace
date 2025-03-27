a = ['A']
b = int(input())
for i in range(0,b):
    c = a.count('A')
    d = a.count('B')
    f = []
    for _ in range(d):
        f.append(a.index('B'))
    for _ in range(c):
        g = a.index('A')
        a[g] = 'B'
    for i in range(0,d):
        a.insert(f[i] + 1,'A')
h = int(a.count('A'))
i = int(a.count('B'))
print(h,i)