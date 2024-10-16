"""a = int(input())
if a > 14:
    print("Добро пожаловать!")
elif a < 14:
    print("Вам ещё рано!")
elif a == 14:
    print("Вам 14 лет! Поздравляю!")"""

"""a = input()
if a == 'secret':
    print("Доступ разрешён")
else:
    print("Неверный пароль!")"""

""""a = input()
if a.isalpha():
    print("Это буква!")
elif a. isdigit():
    print("Это цифра!")
else:
    print("Это не цифра и не буква!")"""

"""a = int(input())
if a > 500 and a < 1000:
    a1 = a - a * 5 // 100
elif a > 1000:
    a1 = a - a * 10 // 100
print(a1)"""

"""a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
print(a+b+c+d+e)"""

"""sum=0
for i in range(5):
    a = int(input())
    sum+=a
print(sum)"""

"""a = int(input())
b = 1
for i in range(1, a + 1):
    b *= i
print(b)"""

"""a = int(input())
s = 0
for i in range(2, a // 2 + 1):
    if (a % i == 0):
        s = s + 1
if s <= 0:
    print("Число простое")
else:
    print("Число не является простым")"""

a = input()
s = 0
b = set("eaiou")
for i in a:
    if i in b:
        s += 1
print(s)



