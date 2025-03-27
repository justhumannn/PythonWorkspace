a = int(input())
b1 = []
c1 = []
e = 1
def test(b,d,b1):
    if b == d:
        b1.append(b)
        return 0
    elif b % d == 0:
        b1.append(d)
        b = b//d
        print(b,d,b1)
        d = 2
        return test(b,d,b1)
    else:
        print(b,d,b1)
        return test(b,d+1,b1)
def test2(b,i):
    if i >= len(b)-1:
        return 0
    elif b[i] == b[i+1]:
        b[i] *= b[i+1]
        b.remove(b[i+1])
        return test2(b,i+1)
for _ in range(a):
    b,c = map(int,input().split())
    test(b,2,b1)
    test(c,2,c1)
    print(b1)
    print(c1)
    f = len(b1)
    b1.sort()
    c1.sort()
    test2(b1,0)
    test2(c1,0)
    b1 = set(b1)
    c1 = set(c1)
    bc = b1 | c1
    bc = list(bc)
    print(bc)
    for i in range(0,len(bc)):
        e *= bc[i]
print(e)