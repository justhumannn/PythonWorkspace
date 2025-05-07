n = int(input())
a = [[0]*n for _ in range(n)]
print(a)
idx1,idx2 = 1,1
while True:
    idx1,idx2 = map(int,input().split())
    if idx1 == 0 and idx2 == 0:
        break
    a[idx1-1][idx2-1] = 1
    print(a)
print(a)
li = [[]*n for _ in range(n)]
while True:
    idx1, idx2 = map(int, input().split())
    if idx1 == 0 and idx2 == 0:
        break
    li[idx1-1].append(idx2)
print(li)