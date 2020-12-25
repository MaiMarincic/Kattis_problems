l, r = input().split()
l = int(l)
r = int(r)

def f(x):
    i = 0
    while x != 1:
        if x % 2 == 0:
            x = x//2
        else:
            x += 1
        i += 1
    return i

def solve(x):
    if x == 1:
        return 0
    elif x % 2 == 0:
        return solve(x//2)*2 + x//2 + x - 2 
    else:
        return solve(x-1) + f(x)

if l == 1:
    print (int(solve(r)) % (10**9 + 7))
else:
    print(int(solve(r) - solve(l-1)) % (10**9 + 7))
