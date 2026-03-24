# A tabela abaixo mostra uma lista de volume sonoro em decibéis para
# diferentes tipos comuns de barulhos.

# #Britadeira 130
# Cortador de grama 106
# Despertador 70
# Sala silenciosa 40


# Escreva um programa Python que receba do usuário um nível de volume em decibéis. Se o
# usuário entrar com um valor igual a um daqueles listados na tabela, então seu programa deve
# exibir uma mensagem informando o tipo de barulho da tabela equivalente ao valor informado.
# Se o usuário entrar um valor intermediário entre dois valores da tabela, então seu programa
# deve exibir uma mensagem informando que o nível está entre os dois barulhos (deve informar
# quais são eles). Certifique-se também que seu programa exiba mensagens apropriadas caso o
# usuário entre com valor menor que o menor valor da tabela ou maior que o maior valor.

barulho = float(input("Informe o valor do barulho em dB: "))

if barulho < 40 or barulho > 130:
    print("I    nforme um valor em decibeis validos!\nEntre 40 e 130 dB")
else:
    if barulho > 40 and barulho < 70:
        print("\nEsse barulho está entre uma sala silenciosa e um despertador!")
    elif barulho > 70 and barulho < 106:
        print("\nEsse barulho está entre um despertador e um cortador de grama!")
    elif barulho > 106 and barulho < 130:
        print("\nEsse barulho está entre um cortador de grama e uma britadeira ")
    else:
        match barulho:
            case 40:
                print("\nEsse barulho é de uma sala silenciosa")
            case 70:
                print("\nEsse barulho é de um despertador")
            case 106:
                print("\nEsse barulho é de um cortador de grama")
            case 130:
                print("\nEsse barulho é de uma britadeira")