# 1.Dublikatlarni tartibni saqlab o'chirish: [3, 1, 3, 2, 1] → [3, 1, 2].

n = [3, 1, 3, 2, 1]
ready = []
for i in n:
    if i in ready:
        continue
    ready.append(i)
print(ready)





