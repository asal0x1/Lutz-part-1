# 3."ism=Ali;yosh=20;shahar=Toshkent" → dict va teskarisi.

text = "ism=Ali;yosh=20;shahar=Toshkent"

text = text.split(';')
ready = {}
for i in text:
    a = i.split('=')
    ready[a[0]] = a[1]
print(ready)

txt = ""

for key, val in ready.items():
    txt += key + '='
    txt += val + ';'

print(txt)

