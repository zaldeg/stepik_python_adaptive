d = {1: "move up", 2: "move down", 3: "move left", 4: "move right", 0: "do not move"}
a = int(input())
if a in d:
    print(d[a])
else:
    print("error!")
