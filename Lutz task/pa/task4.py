# Ikki dict'ni qo'shish, bir xil kalitlarda qiymatlar yig'iladi.

a = {"olma": 3, "anor": 5}
b = {"olma": 2, "banan": 4}

for akey in a.keys():
    for bkey in b.keys():
        if akey == bkey:
            val = a[akey] + b[bkey]
            b[bkey] = val
a.update(b)

print(a)


