n = int(input())
l = [int(i) for i in input().split()]
length = len(l)
if length % 2 == 1:
    length -= 1
for i in range(0, length, 2):
    l[i], l[i + 1], = l[i + 1], l[i]

print(*l)

