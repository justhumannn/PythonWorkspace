# a,b = map(int,input().split())
# c = list(map(int,input().split()))
# c.sort(reverse=True)
# f = []
# b1 = b
# for k in range(0,len(c)-1):
#     if c[k] < b1:
#         b1 -= c[k]
#         d = c[k]
#         e = 1
#         j = k + 1
#         for i in range(k+1,len(c)):
#             while j < len(c):
#                 if c[j] <= b1:
#                     b1 -= c[j]
#                     d += c[j]
#                     e += 1
#                 j += 1
#                 if e == 3:
#                     f.append(d)
#                     e = 1
#                     b1 = b - c[k]
#                     d = c[k]
#             j += i + 1
#             b1 = b - c[k]
#             e = 1
#             d = c[k]
#     b1 = b
#     e = 0
#     d = 0
# print(max(f))
N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0

# 3중 반복문으로 3장의 카드 선택
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            total = cards[i] + cards[j] + cards[k]
            if total <= M:
                max_sum = max(max_sum, total)

# 결과 출력
print(max_sum)