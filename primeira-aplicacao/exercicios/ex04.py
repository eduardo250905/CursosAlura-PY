x = int(input('Digite as coordenadas de x: '))
y = int(input('Digite as coordenadas de y: '))

if(x > 0):
    if(y > 0):
        print('Primeiro quadrante')
    elif(y < 0):
        print('Quarto quadrante')
    else:
        print('Entre primeiro e quarto quadrante')
elif(x < 0):
    if(y > 0):
        print('Segundo quadrante')
    elif(y < 0):
        print('Terceiro quadrante')
    else:
        print('Entre segundo e terceiro quadrante')
else:
    if(y > 0):
        print('Entre primeiro e segundo quadrante')
    elif(y < 0):
        print('Entre terceiro e quarto quadrante')
    else:
        print('Na origem')
