for _ in range(int(input())):
    useless, m, n = map(int,input().split(" "))
    poss_num = [1]
    i = 0
    while (poss_num[i]*m) <= n:
        poss_num.append(poss_num[i]*m)
        i += 1
    
    r = [1]
    for i in range(n):
        r.append(0)
    

    for i in range(len(poss_num)):
        j = poss_num[i]
        while j <= n:
            r[j] += r[j - poss_num[i]]
            j += 1
        
    print(str(useless) + " " + str(r[-1]))