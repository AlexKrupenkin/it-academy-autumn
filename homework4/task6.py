"""
6.	Слова
Во входной строке записан текст. Словом считается
последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами
конца строки. Определите, сколько различных слов содержится в этом тексте.
"""
dct_ = {}
lst_ = []
str_ = 'Во входной  строке записан тоь гп нпа нек к      текст ..... Словом с  .  читается'
str_ = str_.split()
for word in str_:
    if not len(word) <= 1:
         lst_.append(word)
for i in lst_:
    dct_[i] = dct_.get(i,0)+1
print(len(dct_), 'различных слов')
