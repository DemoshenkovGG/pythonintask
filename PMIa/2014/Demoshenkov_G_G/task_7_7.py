#Задача №7, Вариант 7
#1-50. Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.

#Демошенков Г.Г.
#24.05.2016

import random
osnavateli=('Ларри Пейдж','Сергей Брин')
osnavatel=random.randint(0,1)
rand=osnavateli[osnavatel]
Ball=100
print("Я загадал одного из оснавателей Google")
print (rand)
otvet=0
while (otvet)!=(rand):
	otvet=input("Введите одного из основателей:")
	if (otvet)!=(rand):
		print ("Вы не угадали. Попробуйте снова.")
		Ball/=2
	elif (otvet)==(rand):
		print ("Вы угадали.")
		print ("Ваши баллы:"+str(Ball))
		break

input("Нажмите Enter для выхода.")