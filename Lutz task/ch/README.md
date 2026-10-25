## 1.
a = [1, [2, 3]]: b = a, a[:], copy.copy, copy.deepcopy farqi — har holatda id(), is va izoh.

# 1.
a = [1, [2, 3]]
b = a
print(id(a), id(b)) #Bir xil id
print(a is b) # True

# hozirgi holatda obyekt oziga ikkita reference olgan 
# va ularning id si bir xil shuning uchun 
# is bilan tekshirganimizda True javobini olamiz

# 2.
a[:]
# shu obyektdan copy olish uchun ishlatiladi copy.copy bilan bir xil ishlaydi

# 3. 
copy.copy 
# bu ham obyektdan copy oladi va boshqa obyekt yaratadi
# faqat copy olingani ozgartiriladi 
# ammo bu ichki listni copy qila olmaydi
# va shu payt ichki listka ozgartirish kiritilsa butun obyekt ozgaradi 
# id() si har xil is bilan tekshirilganda False 

# 4.
copy.deepcopy
# bu yerda ham copy olinib yangi obyekt yaratiladi 
# faqat endi bu ichki listni ham copy ga oladi ozgartirilsa 
# birinchi obyekt ozgarmaydi 
id() si har xil is False