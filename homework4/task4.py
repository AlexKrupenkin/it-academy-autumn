"""
4.	Даны два списка чисел. Посчитайте, сколько
различных чисел входит только в один из этих списков
"""

dct_1 = {}
dct_2 = {}
lst_1 = [1, 2, 2, 2, 2, 2, 2, 111]
lst_2 = [22, 3, 4, 5, 6, 7, 7, 7, 8, 8, 6, 4, 3]


for i in lst_1:
    dct_1[i] = dct_1.get(i, 0) + 1


print('в списке содедержится', len(dct_1), 'различных чисел')
