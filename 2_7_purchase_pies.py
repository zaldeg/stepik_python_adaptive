A = int(input())
B = int(input())
N = int(input())
a = [A * N + B * N // 100, B * N % 100]
print(*a)
