"""
2.	Города
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк,
каждая строка начинается с названия страны, затем идут названия городов этой страны.
В следующей строке записано число M, далее идут M запросов — названия каких-то
M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.
Примеры
Входные данные
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa
"""

n = int(input('введите количество стран:'))
lst_ = []
lst_1 = []
dct_1 = {}
dct_ = {}


while n:
    str_ = input('введите страну и названия городов:')
    lst_ = str_.split()
    dct_ = dict(zip([lst_[0]], [lst_]))
    dct_1.update(dct_)
    n -= 1


n = int(input('введите количество вводов:'))
while n:
    str_ = input('введите названия городов:')
    lst_1.append(str_)
    n -= 1


for word in lst_1:
    for key, value in dct_1.items():
        if word in value:
            print(key)
