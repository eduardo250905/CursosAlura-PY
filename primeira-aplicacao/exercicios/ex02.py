def classifica_idade(idade):
    if idade <= 12:
        print('Tu é bebê ainda paizao')
    elif idade <= 18:
        print('Ta amadurecendo em paizao')
    else:
        print('Ta veio')

idade = int(input('Digite sua idade: '))
classifica_idade(idade)
