#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 3, 5, 2, 2, 2, 4, 2, 2]
data2 = list(gen_random(1, 3, 10))

# Реализация задания 2

my_iter = Unique(data1)
for i in my_iter:
    print(i)
print('\n')

my_iter2 = Unique(data2)
print(data2)
for i in my_iter2:
    print(i)
print('\n')

data3 = ['A', 'a', 'B', 'b']
my_iter3 = Unique(data3, ig=True)
for i in my_iter3:
    print(i)
print('\n')

my_iter4 = Unique(data3)
for i in my_iter4:
    print(i)
