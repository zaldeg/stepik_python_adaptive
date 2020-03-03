sides = []
sides.append(int(input()))
sides.append(int(input()))
sides.append(int(input()))
sides = sorted(sides, reverse=True)
if sides[0] < sides[1] + sides[2]:
    print("YES")
else:
    print("NO")
