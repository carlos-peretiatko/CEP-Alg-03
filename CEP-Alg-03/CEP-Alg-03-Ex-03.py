# Vogal ou consoante. Escreva um programa Python que peça para o usuário uma letra do
# alfabeto. Se o usuário entrar com as letras a, e, i, o ou u, o programa deve exibir uma
# mensagem dizendo que a letra é uma vogal. Caso contrário, o programa deve exibir a
# mensagem informando que a letra é uma consoante.

letra = input("Informe uma letra!\nDirei se ela é consoante ou vogal: ")
letra = letra.title()

if len(letra) != 1:
    print("Digite apenas uma letra por favor!")
elif not letra.isalpha():
    print("Digite apenas letras!")
else:
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        print("É uma vogal!")
    else:
        print("É uma consoante")