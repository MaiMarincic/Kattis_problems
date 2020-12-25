
n, m = map(int, input().split())
ballots = []
for _ in range(m):
  #samo parsing
  n_vote, ballot = input().split(" ")
  n_vote = int(n_vote)
  d = {}
  for ind, letter in enumerate(ballot):
    letter = int(ord(letter) - ord('A'))
    d[letter] = ind
  ballots.append([n_vote, d])

win = dict(zip(list(range(n)), [set() for _ in range(n)]))

for v in range(n):  #nardi dict win k ma kluce kdo in value koga premaga
  for w in range(v + 1, n):
    i_p, j_p = 0, 0
    for p, ballot in ballots:
      if ballot[v] < ballot[w]:
        i_p += p
      else:
        j_p += p
    if i_p > j_p:
      win[v].add(w)
    else:
      win[w].add(v)


loss = dict(zip(list(range(n)), [set() for _ in range(n)]))

for v in win.keys():             # Sam nardim obratno od win
  for w in win.keys():
    if v != w and v in win[w]:
      loss[v].add(w)


def check(win, v, visited): 
  #nardi graf
  visited.add(v)
  for w in win[v]:
    if w not in visited:
      check(win, w, visited)

for i in range(n):
  beats = set()
  check(win, i, beats)
  beaten_by = loss[i]
  #prever ce je v grafu zmagovalna kombinacija
  if beaten_by.issubset(beats):
    print(chr(ord('A') + i) + ": can win")
  else:
    print(chr(ord('A') + i) + ": can't win")