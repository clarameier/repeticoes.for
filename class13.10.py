from datetime import date

hoje  = date.today().year
total1 = 0
total2 = 0

for c in range(1, 8):
    data = int(input('Digite a {}° data de nascimento: '.format(c)))
    idade = hoje - data
    print('A {}° pessoa tem {} anos!'.format(c, idade))
    if idade >= 18:
        total1 = total1 + 1
        print('E ela(e) já atingiu a sua maioridade!')
    else:
        print('E ela(e) ainda não atingiu a maioridade.')
        total2 = total2 + 1
        print('Ao todo, {} pessoas já são de maior e {} ainda são de menor idade.'.format(total1, total2))