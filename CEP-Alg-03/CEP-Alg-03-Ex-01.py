# Par ou ímpar. Escreva um programa Python que recebe do usuário um número inteiro. Seu
# programa deve então exibir uma mensagem indicando se o número fornecido é par ou ímpar.

n = int(input("Insira o número desejado: "))

if n % 2 == 0:
    print("O número informado é par!!")
else:
    print("O número informado é impar!!")