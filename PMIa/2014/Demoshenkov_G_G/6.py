
import random
a="Ворчун"
b="Чихун"
c="Умник"
d="Соня"
e="Простак"
f="Весельчак"
g="Тихоня"
h="хочу зачёт"
gnom=random.randint(1,8)
print("Программа случайным образом отображает имя одного из семи гномов,друзей Белосжнежки(а иногда и желание автора программы(примерно с шансом 1/8))")
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
elif gnom==8:
	print(h)
input("Нажмите Enter для выхода")
