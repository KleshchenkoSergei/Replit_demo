# комментарии
#a = 10 + 20
#b = a * 30
#c = a/b
#print('Ответ:',c)

#print(2 > 1)
#print(4 > 2 > 3)
#print('c' > 'a')
# print(len('b') > len('a'))
# x = 5
# if x % 2 == 0:
#   print('Число', x, 'четное')
# else:
#   print('Число', x, 'нечетное')

# height = 195
# age = 17
# if age >= 18:
#   if height < 170:
#     print('В танкисты')
#   elif height < 185:
#     print('На флот')
#   elif height < 200:
#     print('В десант')
#   else:
#     print('В другие войска')
# else:
#   print('Непризывной возраст')

# name = input('Input your name: ')
# if name:
#   print('Hello,', name)
# else:
#   print('Hello, world!')

# number = int(input('Input a number: '))
# print(number)
# if number:
#   print('Number not 0')
# else:
#   print('Number = 0')

# account_amount = 1000
# loan_amount = 10000
# days_to_pay = 20
# is_holiday = False
# should_notify = account_amount < loan_amount and ((days_to_pay <10 and not is_holiday) or (days_to_pay ==15))
# print(should_notify)

#определение высокосного года
#Високосными являются года, которые делятся на 4, за исключением столетий, которые не делятся на 400

# year = int(input('Введите год: '))
# if (year % 100) == 0:
#   n = 400
# else:
#   n = 4
# if year % n == 0:
#   print('Год',year, 'високосный')
# else:
#   print('Год',year, 'невисокосный')

year = int(input('Введите год: '))
if ((year % 100 == 0) and (year % 400 == 0)) or ((year % 100 != 0) and (year % 4 == 0)):
  print('Год',year, 'високосный')
else:
  print('Год',year, 'невисокосный')