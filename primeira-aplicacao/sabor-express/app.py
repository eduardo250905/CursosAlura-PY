import os

restaurantes = []

def exibir_nome_do_programa():
    '''Essa função exibe o nome do programa'''
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def exibir_opcoes():
    '''Essa função exibe as opções de escolha do usuário'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar/Desativar restaurante')
    print('4. Sair\n')

def exibir_subtitulo(texto):
    '''Essa função exibe um subtitulo que depende da escolha do usuário
    
    Recebe: 
    -Título da função a ser execultada

    '''
    os.system('cls')
    print('*' * len(texto))
    print(texto)
    print('*' * len(texto))
    print()

def finalizar_app():
    '''Essa função é responsável por finalizar a aplicação'''
    exibir_subtitulo('Finalizando app')

def voltar_ao_menu_principal():
    '''Solicita uma tecla para voltar ao menu principal
    
    Output:
    -Volta ao menu principal
    
    '''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    '''Exibe uma mensagem de opção inválida
    
    Otuput:
    -Volta ao menu principal
    
    '''
    print('Opção inválida!')
    voltar_ao_menu_principal()

def cadastrar_restaurante():
    '''Essa função é responsável pelo cadastro de restaurantes
    
    Input: 
    -Nome do restaurante
    -Categoria

    Output:
    -Adiciona novo restaurante na lista restaurantes

    '''
    exibir_subtitulo('Cadastrando restaurante')
    nome_restaurante = input('Digite o nome do restaurante a ser cadastrado: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsável por listar os restaurantes cadastrados'''
    exibir_subtitulo('Listando restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função é responsável por ativar ou desativar um restaurante
    
    Input:
    -Nome do restaurante
    
    Output:
    -Ativa ou desativa o restaurante com o nome dado

    '''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante a ser ativado ou desativado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            if restaurante['ativo'] == True:
                print(f'O restaurante {nome_restaurante} foi ativado com sucesso!')
            else:
                print(f'O restaurante {nome_restaurante} foi desativado com sucesso!')
    if not restaurante_encontrado:
        print(f'Não existe nenhum restaurante com o nome {nome_restaurante}')
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função é responsável por tratar a escolha da opção feita pelo usuário
    
    Input:
    -Opção do usuário
    
    Output:
    -Função correspondente a opção
    
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match(opcao_escolhida):
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Essa é a função principal'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if(__name__ == '__main__'):
    main()
