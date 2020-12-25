f_input_row = input().split(' ')
f_input_row = list(map(int, f_input_row))
p = f_input_row[0] #row
q = f_input_row[1] #col
n = f_input_row[2] #n_dots
dots = []

if n != 0:
    for el in range(n):
        c = input().split(' ')
        c = list(map(int, c))
        dots.append([c[0]-1, c[1]-1])
    dots_in_row = []
    for i in range(p):
        dots_in_row.append(0)
    dots.sort()

    for d in dots:
        dots_in_row[d[0]] += 1

    print(dots_in_row)
    slices = []
    slice_ = []
    start_row = 0
    start_col = 0
    dot_counter = 0
    for i in range(p):
        if dots_in_row[i] > 1:
            for j in range(dots_in_row[i]):
                if j == dots_in_row[i] - 1:
                    slice_ = [start_row, start_col, i, q-1]
                    slices.append(slice_)
                    dot_counter += 1
                else:
                    slice_ = [start_row, start_col, i, dots[dot_counter][1]]
                    slices.append(slice_)

                    start_col = dots[dot_counter][1] + 1
                    dot_counter += 1

            start_row = i + 1
            start_col = 0
        elif dots_in_row[i] == 1:
            slice_ = [start_row, 0, i, q-1]
            slices.append(slice_)
            start_row = i + 1
            dot_counter += 1

    a = len(slices)
    tmp_ind = 0
    dots_in_last_row = 0
    tmp_ind = len(dots_in_row) - 1

    while True:
        if dots_in_row[tmp_ind] != 0:
            dots_in_last_row = dots_in_row[tmp_ind]
            break
        else:
            tmp_ind = tmp_ind - 1

    if slices[a-1][2] != p-1:
        for i in range(dots_in_last_row):
            slices[a - i - 1][2] = p - 1

    for i in range(n):
        print(slices[i][0] + 1, slices[i][1] + 1, slices[i][2] + 1, slices[i][3] + 1)
    print(0)
    slices.clear()
    dots.clear()
    dots_in_row.clear()
    slice_.clear()
else:
    print(p*q)