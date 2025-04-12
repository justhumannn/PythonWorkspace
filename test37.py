a = int(input())
b = []
x = [0] * a
for _ in range(a):
    b.append(list(map(int,input().split())))
for i in range(0,a):
    for j in range(i+1,a):
        c = 0
        if b[i][i] == 0:
            for t in range(i+1,a):
                if b[t][i] != 0:
                    b[t],b[i] = b[i],b[t]
        else:            
            mul = -(b[j][i]/b[i][i])
            for k in range(0,a+1):
                b[j][k] += mul*b[i][k]
                if b[j][k] % 1 != 0:
                    c = 1
            if c:
                for k in range(0,a+1):
                    b[j][k] *= b[i][0]
if b[a-1][-2] == 0:
    for i in range(0,a-1):
        if b[i][-2] != 0:
            b[a-1],b[i] = b[i],b[a-1]
            break
x[a-1] = b[a-1][a]/b[a-1][-2]
for j in range(a-2,-1,-1):
    sum = 0
    for k in range(a-1,j,-1):
        sum += b[j][k] * x[k]
    if b[j][j] != 0:
        x[j] = (b[j][-1] - sum) / b[j][j]

print(*x)
