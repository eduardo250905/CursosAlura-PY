nome_usuario = input('Digite o nome de usuário: ')
senha = input('Digite uma senha: ')

if(len(senha) < 8 or senha == nome_usuario):
    print('Senha inválida')
else:
    print('Dados armazenados com sucesso')
