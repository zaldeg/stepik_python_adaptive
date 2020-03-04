p = int(input())
x = int(input())
y = int(input())
k = int(input())
number = x + y / 100
for i in range(k):
    number *= 1 + p / 100
    number = int(number * 100) / 100
tmp = str(number).split(".")
print(f"{tmp[0]} {tmp[1]}")
