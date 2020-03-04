sum = 0
n = int(input())
for i in range(n):
    number = int(input())
    sum += number if number % 10 == 4 else 0
print(sum)
