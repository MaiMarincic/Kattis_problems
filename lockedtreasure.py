l = [[1 for i in range(31)] for j in range(31)]
for i in range(1,31):
    for j in range(1, 31):
        if j > i:
            break
        l[i][j] = l[i-1][j] + l[i-1][j-1]


for x in l:
    print(x)

times = int(input())
for _ in range(times):
    n, m = input().split(' ')
    print(l[int(n)-1][int(m)-1])