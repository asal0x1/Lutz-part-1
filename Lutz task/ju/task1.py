# 1.Faylni o'qib, qatorlarini teskari tartibda yangi faylga yozsin (with, encoding).

with open('file.txt', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()


with open('reversefile.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines[::-1])

