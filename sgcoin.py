starting_value = int(input())
for i in range(2):
    val = starting_value*31+ord("a")
    val %= 1000000007
    val *= 7
    val %= 1000000007
    token = 10000000 - (val % 10000000)
    print("a", token)
    starting_value = (val + token) % 1000000007
