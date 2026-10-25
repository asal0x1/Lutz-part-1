

1.
## 1) REPL 

PS C:\Users\user\Desktop\Lutz task> python 

>>> a = 12
>>> b = a
>>> print(a is b)
True

REPL da hamma narsa qolda boshqariladi avtomatik emas har bir kod qatorma-qator kiritiladi

## 2) python file.py

PS C:\Users\user\Desktop\Lutz task> python main.py
Hello World

file ning ichidagi buyruqlar ketma-ket bajariladi va toxtaydi

## 3) python -i file.py 

PS C:\Users\user\Desktop\Lutz task> python -i main.py
Hello World
>>> a = 12
>>> b = a
>>> print(b)
12

bu buyruqda avval file dagi buyruqlar bajariladi va REPL ochiladi 

2. 

## other.py da funksiyalar yaratildi va main.py ga import qilindi 
## ularni bytcode ni o'qish va tahlil qilish uchun dis funksiyasi ishlatildi 
## code ishga tushgan vaqt import paytida __pycache__ papka yaratildi
## papka ichida import qilinganlarning bytecode saqlanadi va bu keyinchalik yana kodga run berilsa tezroq ishlashga yordam beradi 

 2           0 LOAD_CONST               1 ('Function 1')
              2 RETURN_VALUE
  5           0 LOAD_CONST               1 (12)
              2 RETURN_VALUE
  8           0 LOAD_CONST               1 (30)
              2 RETURN_VALUE
