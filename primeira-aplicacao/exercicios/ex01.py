def par_ou_impar(numero):
    if numero % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é impar')

numero = int(input('Digite um número: '))
par_ou_impar(numero)
