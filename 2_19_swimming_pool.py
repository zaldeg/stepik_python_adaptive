N = int(input())
M = int(input())
X = int(input())
Y = int(input())
a = [X, Y, abs(min(N, M) - X), abs(max(M, N) - Y)]
print(min(a))
