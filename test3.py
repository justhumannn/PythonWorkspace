a = int(input())
e = []
triangle = [1,1,1]
for _ in range(a):
    b = int(input())
    for i in range(3,b):
        triangle.append(triangle[i-3] + triangle[i-2])
    e.append(triangle[b-1])
    
for i in range(a):
    print(e[i])