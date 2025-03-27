a,b = map(int,input().split())
c = list(map(int,input().split()))
c.sort()
d = 0
i = 0
while b > 0 and i < len(c):
    if c[i] <= b:
        b -= c[i]
        d += c[i]
        e = c[i]
    else:
        if i >= len(c):
            break
        else:
            if b + e >= c[i]:
                print(b,c[i],e,d)
                b += e
                b -= c[i]
                d -= e
                d += c[i]
                print(b,c[i],e,d)
    i += 1
print(d)
print(c)