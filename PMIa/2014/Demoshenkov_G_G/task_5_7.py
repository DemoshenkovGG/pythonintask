﻿#Задача №5, Вариант 7
#Напишите программу, которая бы при запуске случайным образом отображала имя одного из семи гномов, друзей Белоснежки.

#Демошенков Г.Г.
#23.05.2016

import random
a="Ворчун"
b="Чихун"
c="Умник"
d="Соня"
e="Простак"
f="Весельчак"
g="Тихоня"
gnom=random.randint(1,7)
print("Программа случайным образом отображает имя одного из семи гномов")
if gnom==1:
	print(a)
elif gnom==2:
	print(b)
elif gnom==3:
	print(c)
elif gnom==4:
	print(d)
elif gnom==5:
	print(e)
elif gnom==6:
	print(f)
elif gnom==7:
	print(g)
input("Нажми Enter для выхода.")