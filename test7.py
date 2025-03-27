n = int(input())
a = ['A']
def test(a,b):
    if a[b] == 'Z':
        a[b] = 'A'
        return test(a,b-1)
    else:
        a[b] = ord(a[b])
        a[b] += 1
        a[b] = chr(a[b])
for _ in range(n-1):
    if a.count('Z') == len(a):
        b = len(a) + 1
        a = []
        for _ in range(b):
            a.append('A')
    elif a[-1] == 'Z':
        a[-1] = 'A'
        b = len(a) - 2
        test(a,b)
    else:
        a[-1] = ord(a[-1])
        a[-1] += 1
        a[-1] = chr(a[-1])
print(*a)