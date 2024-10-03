# Задача 1

year=int(input('Введите год:'))
if year % 4 == 0:
    print('Високосный год')
else: print('Обычный год')

# Задача 2

number=int(input("Введите номер билета: "))
a=number//100000
b=(number-a*100000)//10000
c=(number-a*100000-b*10000)//1000
d=(number-a*100000-b*10000-c*1000)//100
e=(number-a*100000-b*10000-c*1000-d*100)//10
f=number%10
#print(a,b,c,d,e,f)
if a+b+c==d+e+f:
    print('Cчастливый билет')
else:
    print('Несчастливый билет')