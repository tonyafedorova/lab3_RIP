#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as Unique

path = "C:/Users/User/Desktop/Любимый/РИП/lab3_RIP/data_light_cp1251.json"

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path) as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

#
@print_result
def f1(arg):
    data2 = list()
    for num in arg:
        data2.append(num["job-name"].lower())
    return list(Unique(sorted(data2)))

# @print_result
# def f2(arg):
#     raise NotImplemented
#
#
# @print_result
# def f3(arg):
#     raise NotImplemented
#
#
# @print_result
# def f4(arg):
#     raise NotImplemented
#
#
# with timer():
#    f4(f3(f2(f1(data))))


# f1(data)
# data2 = list()
# for i in data:
#     data2.append(i["job-name"])
# data_ = sorted(data[i]["job-name"], key=lambda x: x.lower())
# print(data_)
# print(data[6]["job-name"])
# print(data2)


f1(data)
