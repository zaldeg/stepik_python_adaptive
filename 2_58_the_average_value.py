seq = []

while True:
    a = int(input())
    if a == 0:
        break
    else:
        seq.append(a)

print(sum(seq) / len(seq))
