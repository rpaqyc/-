m = int(input("Введите пятизначное число"))
if m>99999:
    print ("Ошибка")
k = m//10000
q = m%10000
w = q//1000
e = q%1000    
r = e//100
t = e%100
y = t//10
u = t%10
print("Предпоследняя цифра",y)
print("Последняя цифра",u)
    
