tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

try:
    numero = int(input('Digite um número para saber a sua tabuada: '))
    for num in tuple:
        print(f'{numero} x {num} = {numero*num}')
except:
    print('Valor inválido')