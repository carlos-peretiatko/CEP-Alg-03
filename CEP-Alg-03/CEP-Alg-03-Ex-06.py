# Classifique o triângulo. Baseado nos comprimentos dos seus lados, um triângulo pode ser
# classificado como equilátero (quando os três lados tem o mesmo tamanho), isósceles (quando
# apenas dois lados são iguais) ou escaleno (quando os três lados são diferentes). Escreva um
# programa Python que recebe do usuário os comprimentos dos 3 lados de um triângulo e exiba
# uma mensagem informando qual é o tipo do triângulo.

lados = []

for i in range(3):
    valor = float(input(f"Informe o valor do lado {i + 1}: "))
    
    while valor <= 0:
        valor = float(input(f"Valor inválido! Informe novamente o lado {i + 1}: "))
    
    lados.append(valor) #??

if lados[0] == lados[1] == lados[2]:
    print("Triângulo equilátero")
elif lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]:
    print("Triângulo isósceles")
else:
    print("Triângulo escaleno")