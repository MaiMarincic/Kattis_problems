options = {"#", "."}
error = False
img_len = 0
endl = False
while True:
    error = False
    n = int(input())
    if n == 0:
        break
    if endl:
        print()
    for i in range(n):
        line = input().split(' ')
        char = line[0]
        code = line[1:]
        code = list(map(int, code))
        if i == 0:
            img_len = sum(code)
        else:
            if sum(code) != img_len:
                error = True
        output = ""
        for el in code:
            output += (str(char)*el)
            char = options - set(char)
            for x in char:
                char = x
        print(output)
    if error:
        print("Error decoding image")
    endl = True

