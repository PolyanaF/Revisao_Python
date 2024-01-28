# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

dic_pessoa = {'nome': 'Polyana', 'idade': 23, 'cidade': 'Embu das Artes'}


# 2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa)

dic_pessoa['idade'] = 24

mensagem = dic_pessoa['idade']
print(mensagem)

# Adicione um campo de profissão para essa pessoa

dic_pessoa['profissao'] = 'Engenheira'

print(dic_pessoa)

# Remova um item do dicionário.

del dic_pessoa['cidade']
print(dic_pessoa)

# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.

numeros_quadrados = {x: x**2 for x in range(1, 6)}

print(numeros_quadrados)

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}

if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."

contagem_palavras = {}

# o split() ele separa a string em partes, podemos definir onde ele vai dividir,
# como eu não coloquei nada entre os parenteses, ele eira separar pelos espaçoes
# em branco, mas se eu colocasse (",") virgula, ele separaria a frase pelas virgulas

# Apos ter separado a frase, se tornou uma lista
palavras = frase.split()

for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)



