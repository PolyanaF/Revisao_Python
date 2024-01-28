import os
# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.
lista_num = [1,2,3,4,5,6,7,8,9,10]
lista_nomes = ['Polyana','Carla','Matheus','Maria']
lista_ano = [2000,2024]

"""def ler_lista(lista):
    print(lista)
    print()

print('Lista de Numeros')
ler_lista(lista_num)

print('Lista de Nomes')
ler_lista(lista_nomes)

print('Lista de Ano')
ler_lista(lista_ano)
"""

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

"""lista = [1,8,9.0,'Poly']

for l in lista:
    print(l)"""


# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
"""soma = 0
for lista in lista_num:
    # print(lista)
    if lista % 2 == 1:
       soma += lista

print(soma)"""

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

"""print('Lista Decrescente', sorted(lista_num, reverse = True))"""

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a
# tabuada desse número, indo de 1 a 10.

"""try:
    numero_escolhido = int(input('Digite um numero: '))

    for l in lista_num:

        resultado = numero_escolhido * l
        print(f'{numero_escolhido} x {l} = {resultado}')

except:
    os.system('cls')
    print('Solicitação Invalida!')"""

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos.
# Utilize um bloco try-except para lidar com possíveis exceções.

"""lista_aleatoria = [1, 2, 3,'8',4, 5]
# print(lista_aleartoria)

soma = 0

try:
    for l in lista_aleatoria:
        # print(l)
        soma += l

    print(soma)
except:
    print('A lista contem caracteres que não pertence ao grupo de numeros')"""


# 7 - Construa um código que calcule a média dos valores em uma lista.
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

lista_de_media = [1,2,3,4]
tamanho_da_lista = len(lista_de_media)

# print(f'A lista {lista_de_media} contem um coleção {tamanho_da_lista} itens')
# print(type(tamanho_da_lista))

soma = 0
try:
    for l in lista_de_media:
        soma += l

    resultado = soma / tamanho_da_lista
    print(f'A Media da lista {lista_de_media} é igual a {resultado}')
except:
    print('A lista esta vazia')