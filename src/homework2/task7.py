#1. 
def mult_two(a, b):

    return a*b


#2
''' 3���� ������� ����� ������� �������, ������� �������� ������(tuple) � ���������� ����� � 3 ���������� - ������, �������, ������ � �����.

example

������� ������: ����� ������� �� ����� 3 ���������.

�������� ������: ����� ���������.'''

def easy_unpack(elements: tuple) -> tuple:
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    # your code here
    a = elements[0]
    b = elements[2]
    c = elements[-2]
    return a,b,c

if __name__ == '__main__':
    
    
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
    
   


#3'''���� ������ � ����� ����� �� ������ �����.

��� ���������� ������ ������ First Word.

������ ������� ������ �� ���������� �������� � ��������.
� ������ � � ����� ������ �������� ���.
������� ���������: ������.

�������� ���������: ������.'''

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    str_ = ''
    for i in text:
        if not i == ' ':
           str_ = str_ + i
        else:
            break
    print (str_)
    return str_


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
   


#4
'''� ��� ���� ������������� ����� �����. ���������� ������, ������� � ���� ����? 
����: ������������� Int. �����: Int. ������:'''





def end_zeros(num: int) -> int:
    
    s = str(a)
    x = len(s)


    return x

if __name__ == '__main__':
    print("Example:")
    print(number_length(10))

   


#5
'''�� ��� �������� �����. ��� ��� ����� ������� �����, ��� ������� �� ������ ��� �������� �� ����������.


   [1,2,3,4,5]


��� ����������� � ��� ���� ������ [3, 4, 5], � ��� ����� ������� ��� ��������, ������� ���� �� 3 - ��� 1 � 2.

� ��� ���� ��� ������� ������: (1) ���� ������� ������� �� ����� ���� ������, �� ������ �� ������ ����������. (2) ���� ������ ����, �� �� ������ ���������� ������.

����: ������ � ������� �������.

�����: Iterable (������, ������, �������� ...)."""



def remove_all_before(items: list, border: int) -> Iterable:
    # your code here
    lst_ = []
    
    
    if border== 0:
        lst_=items       
     
    elif border not in items:
        lst_=items 
    
    else:      
        for i in range(0,len(items)):
          if  border == items[i] :
            lst_= items[i:]
            break
          
           
            
    print(lst_)
    
    return lst_


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

