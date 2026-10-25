# 2.Matndagi so'zlar chastotasi (tinish belgilari tozalanadi), dict bilan, collectionssiz.

gap =  "Salom, dunyo! Salom Python. Dunyo ajoyib!"

signs = [",", "!", "."]
ready = {}

for sign in signs:
    if sign in gap:
        gap = gap.replace(sign, "").lower()

gap = gap.split() 
print(gap)  

for i in gap:
    count = 0
    for j in gap:
        if i == j:
            count += 1
    
    ready[i] = count


print(ready)

