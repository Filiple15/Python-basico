## Atividade 6

prod1 = int(input('Coloque os kilos do primeiro produto: '))
prod2 = int(input('Coloque os kilos do segundo produto: '))
prod3 = int(input('Coloque os kilos do terceiro produto: '))

produtos = prod1 + prod2 + prod3
kilos = float(produtos * 12.50)

print('O valor dos 3 produtos é de :', kilos, 'R$')