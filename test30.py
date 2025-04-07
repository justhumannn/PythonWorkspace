import sys
input = sys.stdin.readline
a = list(input())
a.pop()
b = int(input())
c = []
cursor = len(a)
for _ in range(b):
    command = list(map(str,input().split()))
    if command[0] == 'L':
        if cursor != 0:
            c.append(a.pop())
            cursor -= 1
    elif command[0] == 'D':
        if cursor != len(a) - 1:
            a.append(c[len(c)-1])
            cursor += 1
    elif command[0] == 'B':
        if cursor != 0:
            a.pop()
            cursor -= 1
    else:
        a.append(command[1])
print(''.join(a)+''.join(c,reversed=True))