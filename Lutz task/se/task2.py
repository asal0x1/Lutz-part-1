
from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")
c = Decimal("0.3")

print(a + b)
print(a + b == c)

from fractions import Fraction

a = Fraction("0.1")
b = Fraction("0.2")
c = Fraction("0.3")

print(a + b)
print(a + b == c)