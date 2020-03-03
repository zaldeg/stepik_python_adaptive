def f(x):
    m = 1
    for i in range(x, 0, -2):
        m *= i
    return m


print(f(7))
