# largura e altura da parede em metros. Calcular a área e quantidade de tintas

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura * altura

print('Sua parede tem a dimensão de {} x {} e sua área de é de {} m²'.format(largura, altura, area))

tinta = area / 2

print('Para pintar essa parede voce precisará de {} litros de tinta'.format(tinta))