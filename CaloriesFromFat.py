cal_in_g = [9, 4, 4, 4, 7]


def calories(inp):
    #Pretvori list inp v kalorije ($t$)
    values = inp.split(' ')
    percentage_sum = 0
    total = 0
    index_where_percentage = []

    for i in range(5):
        if values[i][-1] == 'C':
            values[i] = float(values[i][0:-1])
            total += values[i]
        elif values[i][-1] == 'g':
            values[i] = float(values[i][0:-1]) * cal_in_g[i]
            total += values[i]
        else:
            percentage_sum += float(values[i][0:-1])
            index_where_percentage += [i]

    total = total / (1 - percentage_sum / 100)
    for i in index_where_percentage:
        values[i] = total * float(values[i][0:-1]) / 100

    return values


while True:
    inp = input()
    if inp == '-':
        break
    t = calories(inp) # $t$ so kalorije maščob
    while True:
        inp = input()
        if inp == '-':
            break
        t = [sum(x) for x in zip(t, calories(inp))]#Kliče funkcijo in hkrati sešteva rešitve 

    ans = round(100 * t[0] / sum(t))
    print(str(ans) + "%")
