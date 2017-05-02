import random
osnavateli=('Ларри Пейдж','Сергей Брин')
osnavatel=random.randint(0,1)
rand=osnavateli[osnavatel]
print("Я загадал одного из оснавателей Googlе(а также желание о том,чтобы получить...не скажу, а то не сбудется)")
otvet=0
while (otvet)!=(rand):
	otvet=input("Введите одного из основателей:")
	if (otvet)!=(rand):
		print ("Вы не угадали. Попробуйте снова.")
	elif (otvet)==(rand):
		print ("Вы угадали.")
		break

input("Нажмите Enter для выхода.")
