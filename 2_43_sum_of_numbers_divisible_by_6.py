n = int(input())
result = []
for i in range(n):
    x = int(input())
    if x % 6 == 0:
        result.append(x)
print(sum(result))
