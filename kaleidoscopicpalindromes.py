def check(n, k):
    if n == 0:
        return True
    digits = []
    while n:
        digits.append(int(n % k))
        n //= k
    niz = ''.join(map(str,digits[::-1]))
    if niz == niz[::-1]:
        return True
    return False

x, y, k = list(map(int, input().split(" ")))
summ = 0
for i in range(x,y+1):
    tk = 2
    while tk <= k:
        if check(i, tk)== 0:
            break
        tk += 1
    if tk==k+1:
        summ += 1
print(summ)

