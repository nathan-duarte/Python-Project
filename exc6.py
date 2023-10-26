# sorteio de apresentação de trabalho dos alunos

import random

n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno: '))

lista = [n1, n2, n3, n4]

random.shuffle(lista) #embaralhar a lista

print('A ordem de apresentação será: ')

print(lista)

