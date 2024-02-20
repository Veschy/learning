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

# # №2
# zodiak = {'март':[21,'рыбы','овен'],'апрель':[21,'овен','телец'],'май':[22,'телец','близнецы'],'июнь':[22,'близнецы','рак'],'июль':[23,'рак','лев']
#           ,'август':[22,'лев','дева'],'сентябрь':[24,'дева','весы'],'октябрь':[24,'весы','скорпион'],'ноябрь':[23,'скорпион','стрелец'],'декабрь':[23,'стрелец','козерог']
#           ,'январь':[21,'козерог','водолей'],'февраль':[20,'водолей','рыбы']}
#
# zod_month = input('Введите месяц :')
# zod_day = int(input('Введите число :'))
#
# if zod_day < zodiak[zod_month][0]:
#     print(f'Ваш знак  зодиака ****{zodiak[zod_month][1]}****')
# else:
#     print(f'Ваш знак зодиака ****{zodiak[zod_month][2]}****')

# типы  данных и циклы

# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
#
# boys.sort()
# girls.sort()
#
# pairs = zip(boys,girls)
# #print(list(pairs))
# print('Идеальные пары :')
# for boy, girl in pairs:
#     print(f'{boy} и {girl}')

cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],
      ]
  ]
]
persons = int(input('Количество персон :'))

for dish, recept in cook_book:
    print(f'{dish} :')
    for ingr , weight, vel in recept:
        print(f'{ingr}, {weight*persons}{vel}')
    print()

