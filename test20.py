a,b = map(int,input().split())
c = list(map(int,input().split()))
c.sort(reverse=True)
d = 0
i = 0
while b > 0 and i < len(c):
    if c[i] <= b:
        b -= c[i]
        d += c[i]
        i += 1
    else:
        if i >= len(c):
            break
        else:
            i += 1
print(d)