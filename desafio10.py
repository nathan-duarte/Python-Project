# calculando descontos

preco = float(input('Qual o preço do produto? R$ '))

desc = preco - (preco * 5 / 100)

print('O produto que custava R$ {}, na promoção com desconto de 5% vai custar R$ {}'.format(preco, desc))


