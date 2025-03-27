# def test(a,b,c):
#     while b != 'z':
#         c = c + str(a.find(b)) + ' '
#         b = ord(b)
#         b += 1
#         b = chr(b)
#     c = c +  str(a.find(b))
#     return c
# a = input()
# c = ''
# print(test(a,'a',c))
a = int(input())
b = list(map(int,input().split()))
c,d = map(int,input().split())
t = 0
c1 = c
for i in range(0,len(b)):
    if b[i] != 0:
        t += 1
        if b[i] > c:
            t += (b[i] // c)
print(t)
print(a // d, a % d)