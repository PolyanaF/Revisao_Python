import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]


def exibir_nome_do_programa():
    '''Toda vez que essa função for chamada irá exibir o nome do programa, que esta no print abaixo'''
    print('SABOR EXPRESS\n')

def exibir_opcoes():
    '''Aqui listamos a opções que esse sistema oferece'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar estado do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Nesta função encerramos o programa e exibe a mesangem - Finalizando o app'''
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    input('Digite enter para voltar ao menu principal')
    main()
def opcao_invalida():
    '''caso o usuario digite uma opçao que não esteja dentro das nossas opcoes,
    dara um aviso de opcap imvalida e voltara ao menu de escolher as opcoes novamente'''
    print('Opção Invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Quando escolhemos uma opcao e somos encaminhados a ela, nos limpamos o console,
    para focarmos no objetivo escolhido e como parametro ele recebe um texto, que seria como
    um titulo e que sera exibido depois de limpar o console'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante

    Inputs:
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante a lista de restaurantes

    '''

    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}

    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Nesta funcao iremos exibir os restaurantes cadastrados
    Alem de definir, quando um restaurante ter um valor True na sua chave 'ativo',
    ele sera considerado 'ativado', caso contrario 'desativado'
    '''

    exibir_subtitulo('Listando os restaurantes')

    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']

            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'

            print(mensagem)

    if not restaurante_encontrado:
        print('O resturante não foi encontrado')

    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

# print(f'teste {opcao_escolhida}')

# ARREDONDAR UM NUMERO
# pi = 3.14159
# print(round(pi, 2))
