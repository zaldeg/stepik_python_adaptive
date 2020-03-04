n = int(input())
max_4 = 0
for i in range(n):
    tmp = int(input())
    if tmp % 4 == 0 and tmp > max_4:
        max_4 = tmp
print(max_4)
