l = [int(i) for i in input().split()]
num = int(input())
counter = 0
for i, item in enumerate(l):
    if item == num:
        print(i, end=" ")
        counter += 1
if counter == 0:
    print("Missing")
