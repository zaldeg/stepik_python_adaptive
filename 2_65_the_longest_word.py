a = input().split()
tmp_index = 0
max_word = 0
for i, word in enumerate(a):
    if len(word) > max_word:
        tmp_index = i
        max_word = len(word)
print(a[tmp_index])
