# criar um programa que pergunte os dados financeiros e informe se o empréstimo bancário foi aprovado ou negado.

valor_emprestimo = float(input('Qual o valor do empréstimo desejado? '))

quantidade_parcelas = int(input('Em quantas parcelas deseja pagar? '))

salario_mensal = float(input('Qual o salário mensal? '))

nome_limpo = input('Está com o nome limpo? (sim/não): ')

valor_parcelas = valor_emprestimo / quantidade_parcelas

print('O valor de cada parcela é {}'.format(valor_parcelas))

if valor_parcelas <= salario_mensal * 0.30 and nome_limpo == 'sim':
    print('\033[4;33;44m EMPRÉSTIMO APROVADO!! \033[m')
else:
    print('\033[0;30;41m EMPRÉSTIMO NEGADO!! \033[m')

