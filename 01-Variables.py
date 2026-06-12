# Apenas testando e relembrando sobre variáveis.

nome = "Stefany"
developer = 'Steh' 
idade = 21
altura = 1.62
Formada = False

print(type(developer)) # Serve para descobrir o tipo de dados de uma variável.

# Input e Output de dados

print("Hello World")

user_name = input("Digite o seu nome: ")
user_age = int(input("Digite a sua idaide: "))
user_height = float(input("Digite sua altura: "))

#Operadores matemáticaos

10 + 5
123 - 23
8 * 4
70 / 35
3 ** 3  #Potencia
10 % 3  #Resto da divisão

#Concatenação

print("Eu me chamo" + nome)
print(f"Eu me chamo {nome}")    # Forma mais moderna

#=============================================================================

# Exercícios

#Exercício 1:
nome = "Stefany"
idade = 21
cidade = "Curitiba"
altura = 1.62

print(f"Eu me chamo {nome}, tenho {idade} de idade. Sou meio baixote, tenho cerca de {altura} de altura e moro em {cidade} desde de que nasci." )