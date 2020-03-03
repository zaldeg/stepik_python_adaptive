grades = input().split()
count_a = grades.count("A")
print(f"{round(count_a / len(grades), 2):.2f}")
