# - обычный комментарий на одну строку
# обычный вывод на экран
print("")
# задание переменной(в названии переменной не допускаются специальные символы(кроме знака подчеркивания))
some = ("phone")
# В пайтоне применяется два типа наименования переменных: camel case и underscore notation.
# Camel case подразумевает, что каждое новое подслово в наименовании переменной начинается с большой буквы. Например:
userName = "Tom"
# Underscore notation подразумевает, что подслова в наименовании переменной разделяются знаком подчеркивания. Например:
user_name = "Tom"
# Питон регистрозависимый язык, поэтому:
name = Tom # одна переменная
Name = Tom # другая переменная
# int Тип int представляет целое число, например, 1, 4, 8, 50.
nine = 9
# float Тип float представляет число с плавающей точкой, например, 1.2 или 34.76.
money = 22.5
# str(string) это строка
# При этом если строка имеет много символов, ее можем разбить ее на части и разместить их на разных строках кода. В этом случае вся строка заключается в круглые скобки, а ее отдельные части - в кавычки:
text = ("Привет"
    "друг")
print(text)
# Если же мы хотим определить многострочный текст, то такой текст заключается в тройные двойные или одинарные кавычки
# При использовани тройных одинарных кавычек не стоит путать их с комментариями: если текст в тройных одинарных кавычках присваивается переменной, то это строка, а не комментарий.
# myname = "Alexander"
# bool Тип bool представляет два логических значения: True (верно, истина) или False (неверно, ложь).
status = False
# Тип complex представляет комплексные числа в формате вещественная_часть+мнимая_частьj - после мнимой части указывается суффикс j
complexNumber = 1+2j
print(complexNumber)   # (1+2j)
"""масштабный
 комментарий"""
# вывод переменной
print(status)
# удаление переменной((на момент выполнения строки))
del status
# пример тайпкастинга (#float->>>#str)
print("Привет, у меня"+str(money)+"!")
# пример двойного тайпкастинга
name = "amanek"
age = "22"
weight = 64
print(name + str(weight + int(age)))
# для кавычек в тексте при выводе
print('Наша компания "Аквамарин"')
# второй вариант
print("Наша компания \"Аквамарин\"")
# перенос на строку отдельной части текста
print("Текст на первой строке \nтекст на второй строке")
# символ для большого пробела(пробел складывается)
print("Сейчас будет большой пробел \t текст продолжается")
# r(ставится перед строкой) от слова raw , т. е r – это сырые строки (необработанные строки). Нужны для того, чтобы слеш \ не вызывал экранирование символов. Популярные примеры \n , \t .
text = r"C:Python\name.txt"
# Python позволяет встравивать в строку значения других переменных. Для этого внутри строки переменные размещаются в фигурных скобках {}, а перед всей строкой ставится символ f:
userName = "Alex"
userAge = 23
user = f"name: {userName} age: {userAge}"
# Стоит учитывать, что все введенные значения рассматриваются как значения типа str, то есть строки. И даже если мы вводим число, как в втором случае в коде выше, то Python все равно будет рассматривать введенное значение как строку, а не как число.
print(user)
# С помощью встроенной функции type() динамически можно узнать текущий тип переменной:
name = "abc"
print(type(name))
name = 123
print(type(name))
# end - задание конца строки( в примере получается оба текста на одной)
print("Привет, товарищ", end="")
print("Привет")
# Важно знать, что не задавая конец строки он по умолчанию будет равен end="\n"
# То есть для того чтобы вывести текст, который задан на разных строчках, достаточно задать пустой конец строки для n-1 строчек(n-количество строчек),в данном случае я задал конец строки как "пробел"
print("Hello World", end=" ")
print("Hello friend", end=" ")
print("Hello Python")
# sep - задание символа между разными данными в текст(чек пример)
print("Привет, мир",5, "Привет", sep="!")
# (текст с несколькими переменными)
name = "Александр"
weather = "Солнечно"
money = 12415.2
print("Привет, меня зовут "+name)
print("На улице "+weather +",а у меня в кармане "+str(money)+"$")
# f-строки(оптимизированный вариант с несколькими переменными)P.S. АВТОТАЙПКАСТИНГ
print(f"Привет,{name}, у тебя в кармане {money}$")
# input
weight = input("Введите ваш вес:")
print(f"Ваше вес: {weight}")
# import
import random
print(random.randint(121, 12121))
# математические операции +, -, *, /, //(Данная операция возвращает целочисленный результат деления, отбрасывая дробную часть), **, %(Получение остатка от деления), унарный минус, округлени, Пи
print(5+5)
a=11
b=1321
#
# округление(до ближайшего четного числа)P.S. FLOOR- В МЕНЬШУЮ, CEIL- В БОЛЬШУЮ
x=4.5
print(round(x))
# Функция round() также может принимать второе число, которое указывает, сколько знаков после запятой должно содержать получаемое число:
first_number = 2.0001
second_number = 0.1
third_number = first_number + second_number
print(round(third_number, 4))
# В данном случае число third_number округляется до 4 знаков после запятой.
# Если в функцию передается только одно значение - только округляемое число, оно округляется то ближайшего целого
# Однако если округляемая часть равна одинаково удалена от двух целых чисел, то округление идет к ближайшему четному:
print(round(2.5)) # 2 - ближайшее четное
print(round(3.5)) # 4 - ближайшее четное
# Округление производится до ближайшего кратного 10 в степени минус округляемая часть:
# округление до двух знаков после запятой
print(round(2.554, 2))    # к 2.55
print(round(2.5551, 2))   # к 2.56
print(round(2.554999, 2)) # к 2.55
print(round(2.499, 2))    # к 2.5
# Однако следует учитывать, что функция round() не идеальный инструмент.  В Python в связи с тем, что десятичная часть числа не может быть точно представлена в виде числа float, то это может приводить к некоторым не совсем ожидаемым результатам.
# Например, выше при округление до целых чисел применяется правило, согласно которому, если округляемая часть одинаково удалена от двух значений, то округление производится до ближайшего четного значения.
# Например:
# округление до двух знаков после запятой
print(round(2.545, 2))   # 2.54
print(round(2.555, 2))   # 2.56 - округление до четного
print(round(2.565, 2))   # 2.56
print(round(2.575, 2))   # 2.58

print(round(2.655, 2))   # 2.65 - округление не до четного
print(round(2.665, 2))   # 2.67
print(round(2.675, 2))   # 2.67
# Подробнее про такое округление - https://docs.python.org/3/tutorial/floatingpoint.html#tut-fp-issues
# также с делением например
 print(round(5 / 3))
#
import math
x=26316.1
print(math.pi)
#
num1 = 5
# Ряд специальных операций позволяют использовать присвоить результат операции первому операнду:
# num1 += 5 будет эквивалентно num1 = num 1+5 (также с -,*,/,%)
# !=5(не равно 5)
# Ряд специальных операций позволяют использовать присвоить результат операции первому операнду:
# += Присвоение результата сложения
# -= Присвоение результата вычитания
# *= Присвоение результата умножения
# /= Присвоение результата от деления
# //=Присвоение результата целочисленного деления
# **= Присвоение степени числа
# %= Присвоение остатка от деления
max() максимальное
#
abs() модуль
#
pow(5, 6) степень (5 в 6 степени)
# По умолчанию стандартные числа расцениваются как числа в десятичной системе. Но Python также поддерживает числа в двоичной, восьмеричной и шестнадцатеричной системах.
# Для указания, что число представляет двоичную систему, перед числом ставится префикс 0b:
# Для указания, что число представляет восьмеричную систему, перед числом ставится префикс 0o:
# Для указания, что число представляет шестнадцатеричную систему, перед числом ставится префикс 0x:
# В какой-бы системе мы не передали число в функцию print для вывода на консоль, оно по умолчанию будет выводиться в десятичной системе.
# Поразрядные операции с числами ???

# Логические операции
# Для создания составных условных выражений применяются логические операции. В Python имеются следующие логические операторы:
 and (логическое умножение)
 Возвращает True, если оба выражения равны True
 age = 22
weight = 58
result = age > 21 and weight == 58
print(result)
 # В данном случае оператор and сравнивает результаты двух выражений: age > 21 weight == 58. И если оба этих выражений возвращают True, то оператор and также возвращает True.
 # Причем в качестве одно из выражений необязательно выступает операция сравнения: это может быть другая логическая операция или просто переменная типа boolean, которая хранит True или False.
 age = 22
weight = 58
isMarried = False
result = age > 21 and weight == 58 and isMarried
print(result)  # False, так как isMarried = False
#
or (логическое сложение)
Возвращает True, если хотя бы одно из выражений равно True
age = 22
isMarried = False
result = age > 21 or isMarried
print(result)    # True, так как выражение age > 21 равно True
#
not (логическое отрицание)
Возвращает True, если выражение равно False
age = 22
isMarried = False
print(not age > 21) # False
print(not isMarried) # True
# Если один из операндов оператора and возвращает False, то другой операнд уже не оценивается, так как оператор в любом случае возвратит False. Подобное поведение позволяет немного увеличить производительность, так как не приходится тратить ресурсы на оценку второго операнда.
# Аналогично если один из операндов оператора or возвращает True, то второй операнд не оценивается, так как оператор в любом случае возвратит True.
# Оператор in возвращает True если в некотором наборе значений есть определенное значение. Он имеет следующую форму:
# Например, строка представляет набор символов. И с помощью оператора in мы можем проверить, есть ли в ней какая-нибудь подстрока:
message = "hello world!"
hello = "hello"
print(hello in message)  # True - подстрока hello есть в строке "hello world!"
# не задавая переменную тоже все работает
message = "hello world!"
print("hello" in message)
 #
gold = "gold"
print(gold in message)  # False - подстроки "gold" нет в строке "hello world!"
# Если нам надо наоборот проверить, нет ли в наборе значений какого-либо значения, то мы можем использовать модификацию оператора - not in.
# Она возвращает True, если в наборе значений НЕТ определенного значения:
message = "hello world!"
hello = "hello"
print(hello not in message)  # False

gold = "gold"
print(gold not in message)  # True
# Выводом будет являтся True или False
# В самом простом виде после ключевого слова if идет логическое выражение.
# И если это логическое выражение возвращает True, то выполняется последующий блок инструкций, каждая из которых должна начинаться с новой строки и должна иметь отступы от начала выражения if (отступ желательно делать в 4 пробела или то количество пробелов, которое кратно 4):
language = "english"
if language == "english":
    print("Hello")
print("End")
#  Поскольку в данном случае значение переменной language равно "english", то будет выполняться блок if, который содержит только одну инструкцию - print("Hello").
# В итоге консоль выведет следующие строки:
Hello
End
# Обратите внимание в коде на последнюю строку, которая выводит сообщение "End".
# Она не имеет отступов от начала строки, поэтому она не принадлежит к блоку if и будет выполняться в любом случае, даже если выражение в конструкции if возвратит False.
# Если вдруг нам надо определить альтернативное решение на тот случай, если выражение в if возвратит False, то мы можем использовать блок else:
language = "russian"
if language == "english":
    print("Hello")
else:
    print("Привет")
 print("End")
# Если выражение language == "english" возвращает True, то выполняется блок if, иначе выполняется блок else. И поскольку в данном случае условие language == "english" возвращает False, то будут выполняться инструкция из блока else.
# Причем инструкции блока else также должны имет отступы от начала строки. Например, в примере выше print("End") не имеет отступа, поэтому она не входит в блок else и будет выполнятьься вне зависимости, чему равно условие language == "english".
# То есть консоль нам выведет следующие строки:
Привет
End
# Блок else также может иметь несколько инструкций, которые должны иметь отступ от начала строки:
language = "russian"
if language == "english":
    print("Hello")
    print("World")
else:
    print("Привет")
    print("мир")
    # Если необходимо ввести несколько альтернативных условий, то можно использовать дополнительные блоки elif, после которого идет блок инструкций.
    language = "german"
if language == "english":
    print("Hello")
    print("World")
elif language == "german":
    print("Hallo")
    print("Welt")
else:
    print("Привет")
    print("мир")
# Сначала Python проверяет выражение if. Если оно равно True, то выполнениются инструкции из блока if. Если это условие возвращает False, то Python проверяет выражение из elif.

# Если выражение после elif равно True, то выполняются инструкции из блока elif. Но если оно равно False то выполняются инструкции из блока else

# При необходимости можно определить несколько блоков elif для разных условий.
# Например:
language = "german"
if language == "english":
    print("Hello")
elif language == "german":
    print("Hallo")
elif language == "french":
    print("Salut")
else:
    print("Привет")
# Конструкция if в свою очередь сама может иметь вложенные конструкции if:
daytime == "morning"
if language == "english":
    print("English")
    if daytime == "morning":
        print("Good morning")
    else:
        print("Good evening")
# Стоит учитывать, что вложенные выражения if также должны начинаться с отступов, а инструкции во вложенных конструкциях также должны иметь отступы.
# Отступы, расставленные не должным образом, могут изменить логику программы.
# Подобным образом можно размещать вложенные конструкции if/elif/else в блоках elif и else:
language = "russian"
daytime = "morning"
if language == "english":
    if daytime == "morning":
        print("Good morning")
    else:
        print("Good evening")
else:
    if daytime == "morning":
        print("Доброе утро")
    else:
        print("Добрый вечер")

# ку
# создание региона
# region rules
фапфвпр
ф
фр
вр

фор
ф
# endregion
# конец региона
# break (выход из цикла)
# continue (скип в цикле)
# lol = None (задача пустой переменной)
tags = [] #список
# изменить список можно следующим образом tags[номер индекса] = чему-то
# важно(счет индексов начинается с 0)
tags[1,5, 41, 14141,]
tags[0] = 141
# можно вывести один элемент из списка
print(tags[2])
# часть списка можно задать другой список
facts = [1, 1, 234, 14124, [1, 14, 12341]]
# вывести последний элемент списка
print(facts[-1])
# элемент из списка в списке
print(factsp[-1][1])
# добавить элемент в конец списка
numsat = [1,2,2131,31,]
numsat.append(5)
# добавить элемент по номеру индекса(смещает индекс  который уже есть(если имеется))
numsat = [1,2,2131,31,]
numsat.insert(1, "xd")
