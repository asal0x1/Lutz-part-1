gap = "A roza upala na lapu Azora"

gap = gap.replace(" ", "").lower()

if gap == gap[::-1]:
    print("polindrom")
else:
    print("polindrom emas")
