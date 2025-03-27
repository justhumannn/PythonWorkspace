a,b = map(int,input().split())
c = list(map(int,input().split()))
c.sort(reverse=True)
f = []
b1 = b
for k in range(0,len(c)-1):
    if c[k] < b1:
        b1 -= c[k]
        d = c[k]
        e = 1
        j = k + 1
        for i in range(k+1,len(c)):
            while j < len(c):
                if c[j] <= b1:
                    b1 -= c[j]
                    d += c[j]
                    e += 1
                j += 1
                if e == 3:
                    f.append(d)
                    e = 1
                    b1 = b - c[k]
                    d = c[k]
            j += i + 1
            b1 = b - c[k]
            e = 1
            d = c[k]
    b1 = b
    e = 0
    d = 0
print(max(f))