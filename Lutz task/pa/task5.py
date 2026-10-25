#5.Ikki ro'yxatdagi user_id'lar: umumiy, faqat birinchida, faqat ikkinchida — set bilan va sikl bilan, tezligini time bilan solishtirsin.

import time
a = [101, 102, 103, 104, 105]
b = [103, 104, 105, 106, 107]
start = time.perf_counter()
combine= set(a) | set(b)
justa = set(a) - set(b)
justb = set(b) - set(a)

end = time.perf_counter()
f = end - start
print(f"Bu set vaqti: {f}")

start2 = time.perf_counter()
c = []
for i in a:
    c.append(i)
for j in b:
    if j not in c:
        c.append(j)

jfirst = []
for i in a:
    if i not in b:
        jfirst.append(i)

jsec = []
for i in b:
    if i not in a:
        jsec.append(i)

end2 = time.perf_counter()
f2 = end2 - start2
print(f"Bu sikl vaqti: {f2}")