# import copy

# a = [1, [2, 3]]
# c = copy.deepcopy(a)
# c[1].append(4)
# print(a, c)
# print(a is c)
# print(id(a), id(c))

''' bu yerda huddi osha list 3 marta kopaytirib qoyadi 
    va uning ichki listini ozgartirmoqchi bolganimizda
      boshqa ichki listlarga ham tasir qiladi'''

a = [[0] * 3] * 3
a[0][0] = 1
print(a) # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

''' bu kodda list comrehension ishlatilgan 
 endi ichki listni ozgartirsak boshqalariga tasir qilmaydi '''

a = [[0] * 3 for _ in range(3)]
a[0][0] = 1
print(a)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]


