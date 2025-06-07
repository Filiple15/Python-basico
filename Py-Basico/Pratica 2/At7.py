## Atividade 7

p1 = int(25) ## Hamburguer
p2 = int(8) ## Refrigerante
p3 = int(15) ## Batata frita
p4 = int(10) ## Suco
p5 = int(12) ## Sorvete
p6 = int(6) ## Café

amigo1 = float(p1 + p2 + p5)
amigo2 = float(p3 + p4 + p6)
amigo3 = float(p1 + p4)

valorAmig1 = (amigo1 * 10) / 100
valorAmig2 = (amigo2 * 10) / 100
valorAmig3 = (amigo3 * 10) / 100

valorTotal1 = valorAmig1 + amigo1
valorTotal2 = valorAmig2 + amigo2
valorTotal3 = valorAmig3 + amigo3

print(' O valor dos produtos do (PRIMEIRO) amigo ficou de: ', amigo1 ,'''
  A taxa de 10% é de: ''', valorAmig1 ,'''
  Valor total é de: ''', valorTotal1)

print('''
  O valor dos produtos do (SEGUNDO) amigo ficou de: ''', amigo2 ,'''
  A taxa de 10% é de: ''', valorAmig2 ,'''
  Valor total é de: ''', valorTotal2)

print('''
  O valor dos produtos do (TERCEIRO) amigo ficou de: ''', amigo3 ,'''
  A taxa de 10% é de: ''', valorAmig3 ,'''
  Valor total é de: ''', valorTotal3)


