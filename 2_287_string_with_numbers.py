a = input().split()
sum = 0
for i in a:
    if i.isdigit():
        sum += int(i)

print(sum)
