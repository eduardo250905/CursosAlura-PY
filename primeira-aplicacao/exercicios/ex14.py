dicionario = [{'nome': 'Eduardo', 'idade': 18}, {'nome': 'Rebecca', 'idade': 20}, {'nome': 'Gustavo', 'idade': 19}]
nome = input('Digite o nome para saber se esta no dicionario: ')
for pessoa in dicionario:
    if(nome == pessoa['nome']):
        print(f'{nome} esta no dicionario')
        exit()
print(f'{nome} não esta no dicionario')
