import sys

table = []

def run(table):
    locations = []
    num = []
    small = []
    big = []
    for i in range(len(table)):
        for j in range(len(table[i])):
            if str(table[i][j]) != ".":
                if table[i][j].isdigit():
                    num.append([table[i][j], [i, j]])
                elif table[i][j].islower():
                    small.append([table[i][j], [i, j]])
                else:
                    big.append([table[i][j], [i, j]])
    num.sort()
    small.sort()
    big.sort()
    locations = num + small + big
    size = len(locations)
    
    i = 1
    while i < size:
        p1 = locations[i-1][1]
        p2 = locations[i][1]
        if p1[0] == p2[0]:
            if p1[1] > p2[1]:
                k = p2[1] + 1
                while True:
                    if k > p1[1]:
                        break
                    else:
                        if table[p1[0]][k] == '|':
                            table[p1[0]][k] = '+'
                        elif table[p1[0]][k] == '.':
                            table[p1[0]][k] = '-'
                        k += 1
                        
            else:
                k = p1[1] + 1
                while True:
                    if k > p2[1]:
                        break
                    else:
                        if table[p1[0]][k] == '|':
                            table[p1[0]][k] = '+'
                        elif table[p1[0]][k] == '.':
                            table[p1[0]][k] = '-'
                        k += 1

        else:
            if p1[0] < p2[0]:
                k = p1[0]+1
                while True:
                    if k > p2[0]:
                        break
                    else:
                        if table[k][p1[1]] == '-':
                            table[k][p1[1]] = '+'
                        if table[k][p1[1]] == '.':
                            table[k][p1[1]] = '|'
                    k += 1
            else:
                k = p2[0] + 1
                while True:
                    if k > p1[0]:
                        break
                    else:
                        if table[k][p1[1]] == '-':
                            table[k][p1[1]] = '+'
                        if table[k][p1[1]] == '.':
                            table[k][p1[1]] = '|'
                    k += 1

        i+=1 

    for n in range(len(table)):
        for m in range(len(table[n])):
            print(table[n][m], end = "")
        print()



for i in sys.stdin:
    if i == "\n":
        run(table)
        print()
        table = []
    else:
        i = i.replace("\n","")
        table.append(list(i))
run(table)
