try:
    print(f'0.{input().split(".")[1]}')
except IndexError:
    print(0)
