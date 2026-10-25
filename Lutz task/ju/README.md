## 2.Nima chiqaradi? t = (1, [2, 3]); t[1].append(4) va t[1] += [5] — nega xato beradi, lekin ro'yxat baribir o'zgaradi?

t[1].append(4) - bunda yuple ichidagi list ozgaradi chunki u mutable va xato bermaydi
t[1] += [5] - bu ham listga yangi element qoshadi keyin tuple obyektiga buni biriktirmoqchi boladi shunda TypeError chiqadi.