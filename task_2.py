'''
4.2[24]: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по 
окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Собирающий модуль за один 
заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь 
перед некоторым кустом. На входе задано количество ягод на каждом кусте. Не обязательно вводить их с клавиатуры, можно задать 
непосредственно в коде программы.
Примеры/Тесты:
Input1: 1, 2, 3, 4, 5, 6, 7, 8
Output1: Макс. кол-во ягод 21, собрано для куста 7
Input1: 11, 92, 1, 42, 15, 12, 11, 81
Output1: Макс. кол-во ягод 184, собрано для куста 1
'''

'''
Решение.
Программа запрашивает у пользователя – выбрать способ ввода: вручную с клавиатуры или в 2 вариантах рандомно.
При выборе вручную – пользователю предлагается ввести количество ягод на каждом кусте черники – в ряд через пробел, запятую или 
их сочетанием (запятые обрезаются при вводе). Окончание ввода клавишей Enter.
После ввода производится проверка введенного ряда – целое или не целое число, символ, буква, слово, отрицательное, 
дорбь и прочее – если значения не заданы, кустов больше 3 и все без ягод или введены не только числа – выводится сообщение что 
условие ввода не выполнено и выводится последовательность – вместо неверно введенных значений подставляется комментарий. 
Предлагается повторить ввод. Цикл продолжается пока последовательность не будет состоять из целых положительных чисел.
При выборе рандомно (вариант 2) – пользователю предлагается сформировать наборы чисел по алгоритму программы через ввод 
параметров (границы диапазона генерации рандомного целого числа (ягод), количество чисел (кустов) - при этом если генерируется 
последовательность из более 2 чисел из зачений 0 - рандомно одному из значений присваивается 1). 
При выборе варианта 3 - генерируется последовательность из 25 целых чисел (кустов) диапазона от 1 до 100 ягод на кусте.
По окончании ввода выводится набор целых чисел.
Далее программа итерируется по каждому кусту, вычисляет количество ягод, которое можно собрать с текущего куста и двух соседних,
сравнивает текущее количество ягод с максимальным, при выполнении условий обновляет максимальное количество и номер куста.  
Результат - выводится максимальное количество ягод и номер куста.
'''

import re
import random
from termcolor import colored 

print(colored(' Корелия известна красивыми историческими достопримечательностями и живописными пейзажами. ', 'green', 'on_light_grey', attrs=['bold']))
choice = input(colored('Выберите способ ввода количества ягод на каждом кусте черники :\n', 'magenta') + colored('" 1 " - набор с клавиатуры : \n', 'cyan') + colored('" 2 " - рандомно с заданием параметров : \n', 'green') + colored('"произвольный символ" - рандомно : ', 'cyan'))
if choice == '1':
    while True:       
        blueberries = input(colored('Введите количество ягод на каждом кусте через пробел или с запятыми : ', 'magenta')).replace(',', ' ').split()
        parBlu = []
        for part in blueberries:            
            if re.match('^[-]?\d+$', part):
                parBlu.append('{отрицательное число}' if int(part) < 0 else int(part))
            elif len(part) > 1 and re.match('^[a-zA-Zа-яА-ЯёЁ]+$', part):
                parBlu.append('слово')
            elif re.match('^[^a-zA-Zа-яА-ЯёЁ0-9]+$', part):
                parBlu.append('символ')
            elif len(part) == 1 and re.match('^[a-zA-Zа-яА-ЯёЁ]+$', part):
                parBlu.append('буква')
            elif re.match('^[-+]?\d+(\.\d+)?$', part):
                parBlu.append('{не целое число}')
            elif re.match('^[-+]?\d+(\/\d+)?$', part):
                parBlu.append('дробь')
            else:
                parBlu.append('хз')            
        yesBlu = all(isinstance(value, int) for value in parBlu)
        if len(parBlu) > 0:
            if yesBlu:
                resBlu = list(map(int, parBlu))                        
                if len(resBlu) > 3 and all(elem == 0 for elem in resBlu):
                    print(colored('Все кусты без ягод.', 'dark_grey'))
                    continue
                else:
                    break                
            else:
                resBlu = ' '.join(map(str, parBlu))
                print(colored('Ошибка! Введены не все целые положительные числа :\n', 'red') + colored(f'{resBlu}\nПовторите ввод.', 'dark_grey'))
        else:
            print(colored('Ошибка! Вы не ввели последовательность чисел. Повторите ввод.', 'red'))    
elif choice == '2':    
    while True:
        try:
            minBlu = int(input(colored('Введите минимальное количество ягод на кусте : ', 'dark_grey')))
            if minBlu < 0:
                print(colored('Ошибка! Значение не может быть меньше нуля.', 'red'))                 
                continue                  
            break
        except ValueError:
            print(colored('Ошибка! Введено не число.', 'red'))
    while True:
        try:
            maxBlu = int(input(colored('Введите максимальное количество ягод на кусте : ', 'dark_grey')))
            if maxBlu < minBlu or maxBlu == 0:
                print(colored('Ошибка! Значение должно быть больше минимального.', 'red'))                 
                continue 
            break           
        except ValueError:
            print(colored('Ошибка! Введено не число.', 'red'))
    while True:
        try:
            countBlu = int(input(colored('Введите количество кустов : ', 'dark_grey')))
            if countBlu <= 0:
                print(colored('Ошибка! Значение должно быть больше нуля.', 'red'))                 
                continue 
            break           
        except ValueError:
            print(colored('Ошибка! Введено не число.', 'red'))    
    resBlu = list(map(int, (random.randint(minBlu, maxBlu) for _ in range(countBlu))))
    print(resBlu)
    if countBlu > 2 and all(value == 0 for value in resBlu):
                index = random.randint(0, len(resBlu)-1)
                resBlu[index] = 1               
else:
    resBlu = list(map(int, (random.randint(1, 100) for _ in range(25))))        
print(colored(f' Заданы кусты с количеством ягод на каждом : \n{resBlu}', 'green', 'on_light_grey'))
blueberMax = sum(resBlu) if len(resBlu) < 3 else max(resBlu[i] + resBlu[(i-1)%len(resBlu)] + resBlu[(i+1)%len(resBlu)] for i in range(len(resBlu)))
bushMax = 1 if len(resBlu) < 2 else max(range(len(resBlu)), key=lambda i: resBlu[i] + resBlu[(i-1)%len(resBlu)] + resBlu[(i+1)%len(resBlu)]) + 1
bushWord = '.' if bushMax == 1 else ' и соседних с ним.'
print(colored('Максимальное количество ягод: {}, собрано c куста {}{}\n'.format(blueberMax, bushMax, bushWord), 'green'))