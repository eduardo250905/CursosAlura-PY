lista = []

soma = 0
elementos = 0
for num in lista:
    elementos += 1
    soma += num
try:
    media = soma/elementos
    print(media)
except:
    print('Lista vazia')
