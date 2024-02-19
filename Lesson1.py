# import math

# def energy (t,p,n):
#      e = t*p*n
#      return e

# time = 10
# power = 30000
# efficiency = 0.9
# energy_1 = energy (time,power,efficiency)
# print (energy_1)
# print(math.sqrt(energy_1))



# def binary_search(list, item):
#      ''' бинарный  поиск'''
#      low = 0
#      n = 0
#      high = list
#      while low <= high:
#           n += 1
#           mid = round((low + high)/2)
#           print(f'попытка {n}',mid)
#           guess = mid
#           if guess == item:
#                return print(f'угадал с {n}-ой попытки = ',guess)
#           if guess > item:
#                high = mid -1
#           else:
#                low = mid + 1
#
#
# help(binary_search)
#
# print(binary_search(40000000000 , 33))


# РЕКУРСИВНЫЙ ВЫЗОВ  -  НЕ ПОНИМАЮ  !!!
# def sum(income_list):
#      ''' пример рекурсии '''
#      if income_list == []:
#           return 0
#      else:
#           return income_list[0] + sum(income_list[1:])

#   ДЗ   на условия
# № 1
# far_east = input('Если ваш регион Дальний  Восток введите да/нет: ')
# base_rate = 10
#
# if far_east == 'да':
#     base_rate -= 2
# else:
#     kids = int(input('Сколько у вас  детей : '))
#     if kids > 3:
#         base_rate -= 1
#     client = input('Вы зарплатный клиент нашего банка  ? да/нет : ')
#     if client == 'да':
#         base_rate -=0.5
#     ensuarance = input('Будете страховаться  в нашей  компании ? да/нет : ')
#     if ensuarance == 'да':
#         base_rate -= 1.5
#
# print(f'Ваша  ипотечная ставка {base_rate} %')

# №2
zodiak = [
    ['март','рыбы'],['апрель','овен'],['май','телец'],['июнь','близнецы'],['июль','рак'],['август','лев'],
    ['сентябрь','дева'],['октябрь','весы'],['ноябрь','скорпион'],['декабрь','стрелец'],['январь','козерог'],['февраль','водолей']]
zod_month = input('Введите месяц :')
zod_day = int(input('Введите число :'))

if zod_month in zodiak:
    if zod_day < 21:
        print(zodiak[zod_month])
    else:
        print(zodiak[zod_month+1])




