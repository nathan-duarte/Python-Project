# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math
from math import floor
num = float(input('Digite um número: '))
parte_inteira = math.floor(num)
print('O número inteiro de {} é {}'.format(num, parte_inteira))
