# Polígono regular. Crie um programa Python que determina e exibe o nome de um polígono
# regular sendo fornecida pelo usuário a quantidade de lados. Seu programa deve suportar
# polígonos de 3 a 10 lados (inclusive). Caso o usuário forneça valores fora desta faixa, o
# programa deve exibir uma mensagem de erro.

lado = int(input("Informe quantos lados os polígono possui: "))

if lado < 3 or lado > 10:
    print("Não calculo polígonos assim!\nSó consigo calcular polígonos de 3 a 10 lados")
else:
    match lado:
        case 3:
            print("\nTriângulo")
        case 4:
            print("\nQuadilátero")
        case 5:
            print("\nPentágono")
        case 6:
            print("\nHexágono")
        case 7: 
            print("\nHeptágono")
        case 8:
            print("\nOctógono")
        case 9:
            print("\nEneágono")
        case 10:
            print("\nDecágano")