﻿#Задача №4, Вариант 7
#Напишите программу, которая выводит имя, под которым скрывается Мария Луиза Чеччарелли. Дополнительно необходимо вывести область интересов указанной личности, место рождения, годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти). Для хранения всех необходимых данных требуется использовать переменные. После вывода информации программа должна дожидаться пока пользователь нажмет Enter для выхода.

#Демошенков Г.Г.
#22.05.2016



print("Мария Луиза Чеччарелли более известна, как итальянская актриса Моника Витти.")
born=1931
place="Рим, Италия"
age=2016-born
interes="Кино"
print("Место рождения: "+(place))
print("Год рождения: "+str(born))
print("Возраст: "+str(age))
print("Область интересов: "+(interes))
input("Нажмите Enter для выхода.")