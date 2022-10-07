# """Задание 1"""
# import string
#
# str = input('Введите строку:')
# upper_case = any([True if i in string.ascii_uppercase else False for i in str])
# lower_case = any([True if i in string.ascii_lowercase else False for i in str])
# punctuation = any([True if i in string.punctuation else False for i in str])
# digits = any([True if i in string.digits else False for i in str])
# if (upper_case, lower_case, punctuation, digits) == (True, True, True, True):
#     print('Yes')
# else:
#     print('No')
#
#
# """Задание 2"""
# n1 = 1    #Первое число в ряду фибоначчи
# n2 = 1    #Второе число в ряду фибоначчи
#
# count = int(input('Введите количество чисел:'))
# print(n1, n2, end = ' ')
# while count > 2:
#     n1, n2 = n2, n1 + n2
#     print(n2, end = ' ')
#     count -= 1
#
#
# """Задание 3"""
# import string
#
# password = input('Введите пароль:')
# punctuations = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
#
# upper_case = any([True if i in string.ascii_uppercase else False for i in password])
# lower_case = any([True if i in string.ascii_lowercase else False for i in password])
# punctuation = any([True if i in string.punctuation else False for i in password])
# digits = any([True if i in string.digits else False for i in password])
# length = len(password)
#
# characters = [upper_case, lower_case, punctuation, digits]
# print(characters)
#
# password_difficulty_mark = 1
# for i in range(len(characters)):
#     if characters[i] and password != "admin" and "qwerty" and " ":
#         password_difficulty_mark += 1
# if length <= 8:
#     password_difficulty_mark -= 1
# print('Сложность пароля: %s из 5' % password_difficulty_mark)
#
#
# """Задание со звездочкой"""
# import random
# import string
#
# symbol_len = int(input('Введите желаемую длину пароля:'))
#
# ascii_lowercase = string.ascii_lowercase
# ascii_uppercase = string.ascii_uppercase
# digits = string.digits
# punctuation = string.punctuation
#
# A = ascii_lowercase + ascii_uppercase + digits + punctuation
# B = random.sample(A, symbol_len)
# password = ''.join(B)
# print(password)