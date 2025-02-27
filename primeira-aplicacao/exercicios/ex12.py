informacoes = [{'nome': 'Eduardo', 'idade': 18, 'cidade': 'Guarulhos'}, {'nome': 'Francisco' , 'idade': 40, 'cidade': 'São José dos Campos'}]
for pessoa in informacoes:
    print(f'{pessoa['nome']}, {pessoa['idade']}, {pessoa['cidade']}')
informacoes[0]['idade'] = 19
for pessoa in informacoes:
    print(f'{pessoa['nome']}, {pessoa['idade']}, {pessoa['cidade']}')
