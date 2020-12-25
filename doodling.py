def nsd(x, y):
#Največji skupni delitelj
   while(y): 
       x, y = y, x % y 
   return x

st_pr = int(input())
for i in range(st_pr):
    tab = input().split(' ')
    n = int(tab[0]) - 1
    m = int(tab[1]) - 1
    nsm = n * m / nsd(n,m) #Najmanjši skupni mnogokratnik
    print(nsm, (nsm / n - 1), (nsm / m - 1))
    odg = nsm + 1 - ((nsm / n - 1) * (nsm / m - 1) / 2)
    print(int(odg))