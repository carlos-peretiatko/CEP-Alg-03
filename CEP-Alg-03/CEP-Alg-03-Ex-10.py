# Cor da casa do tabuleiro. As posições das casas em tabuleiros de xadrez são identificadas
# por uma letra e um número. A letra identifica a coluna e o número define a linha, conforme a
# figura abaixo:

# Escreva um programa Python que receba do usuário um posição. Use um comando if para
# determinar se a coluna informada começa com quadrado preto ou branco. Então, use
# aritmética de inteiros para determinar a cor do quadrado da linha correspondente. Por
# exemplo, se o usuário entrou com o valor a1, então seu programa deve informar que o
# quadrado é preto. Se o usuário entrou com o valor d5, então seu programa deve informar que
# o quadrado é branco. Seu programa pode assumir que o usuário vai entrar valores válidos,
# não sendo necessário verificar eventuais erros de input.

posicao = input("Informe a posição para verificação: (a1, b2, c3 ...) ")

#pega a letra inicial apenas
letra = posicao[0]
numero = int(posicao[1])

coluna = ord(letra) - 96
#ord, se subtrair 96 temos as mesmas colunas de xadrez
#97 = a
#98 = b
#99 = c

if (coluna + numero) % 2 == 0:
    cor = "Preto"
else:
    cor = "Branco"

print(f"O quadrado {posicao} é {cor}.")