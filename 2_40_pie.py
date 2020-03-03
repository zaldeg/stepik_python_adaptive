a = int(input())
b = int(input())

counter = max(a, b)
step = counter
while True:
    if counter % a == 0 and counter % b == 0:
        print(counter)
        break
    counter += step
