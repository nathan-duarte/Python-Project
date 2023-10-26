# Aluguel de carros

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

pago = (dias * 60) + (km * 0.15)

# 60 = preço do aluguel
# 0.15 = preço de km rodado

print('O total a pagar é de R${:.2f} por dia'.format(pago))