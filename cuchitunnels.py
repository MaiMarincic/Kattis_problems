n = int(input())
rooms = input().split(' ')
rooms = list(map(int, rooms))
connections = 0

for i, el in enumerate(rooms):
    if i != 0:
        rooms[i] = rooms[i] - 1
    connections += rooms[i]

branches = 0
bool_ = True
rooms = rooms[::-1]
for el in rooms:
    if el > branches:
        bool_ = False
    branches -= el
    branches += 1

if bool_ and connections + 1 == n:
    print("YES")
else:
    print("NO")
