# 1 - Solicite ao usuário que insira um número e, em seguida,
# use uma estrutura if else para determinar se o número é par ou ímpar.

num = int(input('Digite um numero: '))

if num % 2 == 0:
    print(f'{num} é par')
else:
    print(f'{num} é impar')

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura
# if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

idade = int(input('Digite sua idade: '))

if 0 <= idade <= 12:
    print('Você é uma criança')
elif 13 <= idade <= 18:
    print('Você é um adolescente')
else:
    print('Você é um adulto')

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else
# para verificar se o nome de usuário e a senha fornecidos correspondem aos valores
# esperados determinados por você.

login = 'Polyana'
senha = 'Senha123'

login_usuario = input('Login: ')
senha_usuario = input('Senha:' )

if login_usuario == login or senha_usuario == senha:
    if login_usuario == login:
        if senha_usuario == senha:
            print('Entrada Permitida')
        else:
            print('Senha Incorreta')
    else:
        print('Login Incorreto')
else:
    print('Login e Senha Incorreta')

# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize
# uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o
# ponto se encontra de acordo com as seguintes condições:

print('Digite as coordenadas (x, y)')
x = float(input('X = ' ))
y = float(input('Y = ' ))

if x > 0 < y:
    print('Primeiro Quadrante')
elif x < 0 and y > 0:
    print('Segundo Quadrante')
elif x < 0 > y:
    print('Terceiro Quadrante')
elif x > 0 and y < 0:
    print('Quarto Quadrante')
else:
    print('O ponto está localizado no eixo ou origem')

