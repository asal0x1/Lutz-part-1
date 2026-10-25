## 3.Summani 1 234 567,50 so'm ko'rinishiga keltiruvchi funksiya (Decimal asosida).
from decimal import Decimal

def func(summa):
    summa = Decimal(str(summa)).quantize(Decimal("0.1"))
    print(summa)
    butun, kasr = f"{summa:.2f}".split(".")
    butun = f"{int(butun):,}".replace(",", " ")
    return f"{butun},{kasr} so'm"

print(func(1234567.50))
