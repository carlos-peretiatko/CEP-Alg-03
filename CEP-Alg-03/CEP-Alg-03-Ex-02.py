# Idade canina. É comum dizermos que um ano de um cachorro equivale a 7 anos de um
# humano. Porém, essa conversão simples erra em não reconhecer que cachorros se tornam
# adultos em cerca de 2 anos. Assim, algumas pessoas acreditam que é melhor contar os dois
# primeiros anos como 10.5 anos caninos, e os anos restantes como 4 anos caninos cada.

# Escreva um programa que implemente a conversão de anos cronológicos para anos caninos.
# Certifique-se que seu programa funciona tanto para conversão de idades até 2 anos
# cronológicos e também maiores que 2 anos cronológicos. Seu programa deve exibir uma
# mensagem de erro se o usuário entrar com um número negativo.


anos = int(input("Informe a idade do cãozinho: "))

if anos <= 0:
    print("Não tem como o cachorro ter essa idade\nInsira um número positivo!")
else:
    if anos < 2 and anos != 0:
        anos = anos * 10.5
    else:
        anos = ((anos - 2) * 4) + 21
        
    print("O cãozinho tem ", anos, " anos (em anos de cachorro :3)") 