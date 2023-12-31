# Знакомство с языком Python (семинары)
## Урок 4. Словари, множества и профилирование
### Практическое задание 4. «Словари, множества и профилирование»
Обновлено 03.07.2023

Усложнение задач выделены (*). Они необязательны для решения и нужны для тех, кому мало выполнить обычное задание.
Если вы хотите решить усложненное задание - сначала сделайте задание обычной сложности.

**4.1[22]:** Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. Если таких чисел нет - выдать внятное диагностическое сообщение
Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры

__*Примеры/Тесты:*__

Input1: 2 4 6 8 10 12 10 8 6 4 2

Input2: 3 6 9 12 15 18

Output: 6 12     
__*Обратите внимание*__: Без скобочек, в одну строку

Input1: 2 4 6 8 10 10 8 6 4 2
Input2: 3 9 12 15 18
Output: Повторяющихся чисел нет

**4.2[24]:** В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом. На входе задано количество ягод на каждом кусте. Не обязательно вводить их с клавиатуры, можно задать непосредственно в коде программы

__*Примеры/Тесты:*__

Input1: 1, 2, 3, 4, 5, 6, 7, 8
Output1: Макс. кол-во ягод 21, собрано для куста 7

Input1: 11, 92, 1, 42, 15, 12, 11, 81
Output1: Макс. кол-во ягод 184, собрано для куста 1