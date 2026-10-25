## str

n = "123"
sum = 0

for i in n:
    sum += int(i)
print(sum)

## % and //

n = 123
sum = 0

while n > 0:
    qoldiq = n % 10 
    sum += qoldiq 
    n = n // 10 
    
print(sum)
