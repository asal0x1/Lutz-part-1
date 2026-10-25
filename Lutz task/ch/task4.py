# Telefonni normallashtirish: "90 123-45-67", "(90)1234567", "+998901234567" → "+998901234567"

n = "(90)1234567"

bad = [" ", "-", "(", ")"]
for b in bad:
    if b in n:
        n = n.replace(b, "")
if "+998" not in n[:4]:
    n = "+998" + n
print(n)