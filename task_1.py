'''
4.1[22]: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания 
все те числа, которые встречаются в обоих наборах. Если таких чисел нет - выдать внятное диагностическое сообщение
Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры
Примеры/Тесты:
Input1: 2 4 6 8 10 12 10 8 6 4 2
Input2: 3 6 9 12 15 18
Output: 6 12     Обратите внимание: Без скобочек, в одну строку
Input1: 2 4 6 8 10 10 8 6 4 2
Input2: 3 9 12 15 18
Output: Повторяющихся чисел нет
'''
'''
Решение.
Программа запрашивает у пользователя – выбрать способ ввода чисел: вручную с клавиатуры или в 2 вариантах рандомно.
При выборе вручную – пользователю предлагается ввести два неупорядоченных набора целых чисел – в ряд через пробел, запятую или 
их сочетанием (запятые обрезаются при вводе).  Окончание ввода каждого набора клавишей Enter.
После ввода каждого набора чисел производится проверка введенного ряда – целое или не целое число, символ, буква, слово, 
дорбь и прочее – если значения не заданы или введены не только числа – выводится сообщение что введена не последовательность 
целых чисел и выводится последовательность – вместо неверно введенных значений подставляется комментарий. 
Пользователю предлагается повторить ввод. Цикл продолжается пока последовательность не будет состоять из целых чисел.
При выборе рандомно – пользователю предлагается сформировать наборы чисел по алгоритму программы, либо через ввод параметров для 
каждой из двух последовательностей (границы диапазона генерации рандомного целого числа, количество чисел). По окончании ввода 
выводятся два неупорядоченных набора целых чисел.
Результат - выводятся без повторений в порядке возрастания все числа, которые встречаются в обоих наборах чисел. 
Если таких чисел нет - выводится внятное диагностическое сообщение.
'''

import re
import random
from termcolor import colored 
'''
Если нет модуля termcolor - для установки можно использовать команду в терминале: pip install termcolor
Для Linux или macOS, возможно потребуется sudo pip install termcolor
'''
choice = input(colored('Выберите способ ввода :\n', 'magenta') + colored('" 1 " - набор с клавиатуры : \n', 'cyan') + colored('" 2 " - рандомно с заданием параметров : \n', 'green') + colored('"произвольный символ" - рандомно : ', 'cyan'))
if choice == '1':
    while True:       
        seqFir = input(colored('Введите первую последовательность чисел через пробел или с запятыми: ', 'magenta')).replace(',', ' ').split()
        parFir = []
        for part in seqFir:
            if re.match('^[-]?\d+$', part):
                parFir.append(int(part))
            elif len(part) > 1 and re.match('^[a-zA-Zа-яА-ЯёЁ]+$', part):
                parFir.append('слово')
            elif re.match('^[^a-zA-Zа-яА-ЯёЁ0-9]+$', part):
                parFir.append('символ')
            elif len(part) == 1 and re.match('^[a-zA-Zа-яА-ЯёЁ]+$', part):
                parFir.append('буква')
            elif re.match('^[-+]?\d+(\.\d+)?$', part):
                parFir.append('{не целое число}')
            elif re.match('^[-+]?\d+(\/\d+)?$', part):
                parFir.append('дробь')
            else:
                parFir.append('хз')
        yesFir = all(isinstance(value, int) for value in parFir)
        if len(parFir) > 0:
            if yesFir:
                resFir = ' '.join(map(str, parFir))                
                break
            else:
                resFir = ' '.join(map(str, parFir))
                print(colored(f'Ошибка! Введена последовательность не из всех целых чисел:\n{resFir}\nПовторите ввод.', 'red'))
        else:
            print(colored('Ошибка! Вы не ввели последовательность чисел. Повторите ввод.', 'red')) 
    while True:
        seqSec = input(colored('Введите вторую последовательность чисел через пробел или с запятыми: ', 'magenta')).replace(',', ' ').split()
        parSec = []
        for part in seqSec:
            if re.match('^[-]?\d+$', part):
                parSec.append(int(part))
            elif len(part) > 1 and re.match('^[a-zA-Zа-яА-ЯёЁ]+$', part):
                parSec.append('слово')
            elif re.match('^[^a-zA-Zа-яА-ЯёЁ0-9]+$', part):
                parSec.append('символ')
            elif len(part) == 1 and re.match('^[a-zA-Zа-яА-ЯёЁ]+$', part):
                parSec.append('буква')
            elif re.match('^[-+]?\d+(\.\d+)?$', part):
                parSec.append('{не целое число}')
            elif re.match('^[-+]?\d+(\/\d+)?$', part):
                parSec.append('дробь')
            else:
                parSec.append('хз')
        yesSec = all(isinstance(value, int) for value in parSec)
        if len(parSec) > 0:
            if yesSec:
                resSec = ' '.join(map(str, parSec))                
                break
            else:
                resSec = ' '.join(map(str, parSec))
                print(colored(f'Ошибка! Введена последовательность не из всех целых чисел:\n{resSec}\nПовторите ввод.', 'red'))
        else:
            print(colored('Ошибка! Вы не ввели последовательность чисел. Повторите ввод.', 'red'))
elif choice == '2':    
    while True:
        try:
            minFir = int(input(colored('Введите минимальное число в первой последовательности : ', 'dark_grey')))                  
            break
        except ValueError:
            print(colored('Ошибка! Введено не число.', 'red'))
    while True:
        try:
            maxFir = int(input(colored('Введите максимальное число в первой последовательности : ', 'dark_grey')))
            if maxFir < minFir:
                print(colored('Ошибка! Значение должно быть больше минимального.', 'red'))                 
                continue 
            break           
        except ValueError:
            print(colored('Ошибка! Введено не число.', 'red'))
    while True:
        try:
            countFir = int(input(colored('Введите количество целых чисел первой последовательности : ', 'dark_grey')))
            if countFir <= 0:
                print(colored('Ошибка! Значение должно быть больше нуля.', 'red'))                 
                continue 
            break           
        except ValueError:
            print(colored('Ошибка! Введено не число.', 'red'))
    while True:
        try:
            minSec = int(input(colored('Введите минимальное число во второй последовательности : ', 'light_grey')))                  
            break
        except ValueError:
            print(colored('Ошибка! Введено не число.', 'red'))
    while True:
        try:
            maxSec = int(input(colored('Введите максимальное число во второй последовательности : ', 'light_grey')))
            if maxSec < minSec:
                print(colored('Ошибка! Значение должно быть больше минимального.', 'red'))  
                continue 
            break           
        except ValueError:
            print(colored('Ошибка! Введено не число.', 'red'))
    while True:
        try:
            countSec = int(input(colored('Введите количество целых чисел второй последовательности : ', 'light_grey')))    
            if countSec <= 0:
                print(colored('Ошибка! Значение должно быть больше нуля.', 'red')) 
                continue 
            break           
        except ValueError:
            print(colored('Ошибка! Введено не число.', 'red'))
    resFir = ' '.join(map(str, [str(int(random.randint(minFir, maxFir))) for _ in range(countFir)]))
    resSec = ' '.join(map(str, [str(int(random.uniform(minSec, maxSec))) for _ in range(countSec)]))     
else:
    resFir = ' '.join(map(str, [str(int(random.randint(-100, 100))) for _ in range(15)]))
    resSec = ' '.join(map(str, [str(int(random.uniform(-100, 100))) for _ in range(15)]))
print(colored(f' Первая последовательность состоит из целых чисел : \n[ {resFir} ]', 'green', 'on_light_grey'))
print(colored(f' Вторая последовательность состоит из целых чисел : \n[ {resSec} ]', 'green', 'on_light_grey'))    
com = list(set(map(int, resFir.split())) & set(map(int, resSec.split()))) # сравниваем числа, а не их абсолютные значения
if not com:
    print(colored('Совпадения чисел в двух заданных последовательностях не найдено.', 'yellow'))
else:
    sortNums = sorted(com)    
    result = ' '.join(map(str, sortNums))    
    print(colored(f'Совпадение чисел в порядке возрастания в двух заданных последовательностях :\n{result}\n', 'green'))