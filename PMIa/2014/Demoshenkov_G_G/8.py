import random
osnavateli=('Ларри Пейдж','Сергей Брин')
osnavatel=random.randint(0,1)
rand=osnavateli[osnavatel]
ochki=100
print("Я загадал одного из оснавателей Google(а также желание о том,чтобы получить...не скажу, а то не сбудется)")
otvet=0
while (otvet)!=(rand):
	otvet=input("Введите имя одного из основателей:")
	if (otvet)!=(rand):
		print ("Вы не угадали. Попробуйте снова.")
		ochki/=2
	elif (otvet)==(rand):
		print ("Вы угадали.")
		print ("Ваши баллы:"+str(ochki))
		break

input("Нажмите Enter для выхода.")
