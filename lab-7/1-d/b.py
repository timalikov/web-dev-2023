n = int(input())
ls = list(map(int, input().split()))

for i in range(n):
    if ls[i] % 2 == 0:
        print(ls[i], end=' ')