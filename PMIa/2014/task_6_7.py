#Задача №6, Вариант 7
#Создайте игру, в которой компьютер загадывает имя одного из двух сооснователей компании Google, а игрок должен его угадать.

#Демошенков Г.Г.
#24.05.2016

import random
osnavateli=('Ларри Пейдж','Сергей Брин')
osnavatel=random.randint(0,1)
rand=osnavateli[osnavatel]
print("Я загадал одного из оснавателей Google")
#print (rand)
otvet=0
while (otvet)!=(rand):
	otvet=input("Введите одного из основателей:")
	if (otvet)!=(rand):
		print ("Вы не угадали. Попробуйте снова.")
	elif (otvet)==(rand):
		print ("Вы угадали.")
		break

input("Нажмите Enter для выхода.")