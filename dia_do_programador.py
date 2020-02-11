import math
import os
import random
import re
import sys


def dayOfProgrammer(year):
    if year == 1918:
        return '26.09.1918'
    elif ((year <= 1917) and (year % 4 == 0)) or ((year > 1918) & (year % 400 == 0 or ((year % 4 == 0) & (year % 100 != 0)))):
        return '12.09.%s' % year
    else:
        return '13.09.%s' % year

#print(int(input(dayOfProgrammer('Insira o ano que deseja saber o dia exato do programador: '))))

ano = int(input('Insira o ano: '))
print(dayOfProgrammer(ano))