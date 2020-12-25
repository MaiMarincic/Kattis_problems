for i in range(int(input())):
    operations = input()
    n_el = int(input())
    elements = input()
    elements = elements[1:-1]
    elements = elements.split(",")
    front = True
    start_ind = 0
    end_ind = n_el
    if operations.count("D") > n_el:
        print("error")
    else:
        for command in operations:
            if command == "R":
                front = not front
            elif command == "D":
                if front:
                    start_ind += 1
                else:
                    end_ind -= 1
        if elements != ['']:
            elements = list(map(int, elements))
        if front:
            elements = elements[start_ind:end_ind]
            print(str(elements).replace(" ", ""))
        else:
            elements = elements[start_ind:end_ind]
            elements = elements[::-1]
            print(str(elements).replace(" ", ""))