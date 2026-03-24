# Raízes de equação quadrática. Uma função quadrática pode ser descrita da seguinte forma:

#f(x) = ax² + bx + c

# , onde a, b e c são constantes, e a é diferente de zero. As raízes da
# função quadrática podem ser encontradas determinando-se os valores de x que satisfaçam a
# equação quadrática ax² + bx + c = 0. Uma função quadrática pode ter 0, 1 ou 2 raízes
# reais. Essas raízes podem ser calculadas pela fórmula da Bháskara, mostrada abaixo:

# raiz = (-b (+-) raiz(b² - 4ac)) / 2a

# A parte da expressão dentro da raiz quadrada é chamada de discriminante. Se o discriminante
# for negativo, a equação não possui raízes reais. Se o discriminante for igual a zero, então a
# equação tem apenas uma raiz real. Caso contrário, a equação tem duas raízes reais e a
# expressão deve ser computada duas vezes, uma com o sinal de + e a outra com o sinal de -
# ao se calcular o numerador da fração.
# Escreva um programa Python que calcula as raízes reais de uma função quadrática. Seu
# programa deve iniciar solicitando ao usuário os valores de a, b e c. Então o programa deve
# exibir uma mensagem informando a quantidade de raízes reais e o(s) valor(es) da(s) raiz(es).
import math

a = float(input("informe o valor de A na sua equação: "))
b = float(input("informe o valor de B na sua equação: "))
c = float(input("informe o valor de C na sua equação: "))

delta = b**2 - 4 * a * c

if delta < 0:
    print("\nNão possui raizes reais!")
elif delta == 0:
    print("\nPossui uma raiz apenas!!")
    #claculo da raiz
    raiz = (-b + delta ** 0.5) / (2 * a) #modo de mostrar raiz mais facil
    
    print("A unica raiz possivel é ", raiz)
else: 
    print("\nPossui duas raizes reais")
    
    #calculo duas vezes 
    raiz = (-b + delta ** 0.5) / (2 * a) #modo de mostrar raiz mais facil
    raiz2 = (-b - delta ** 0.5) / (2 * a) #modo de mostrar raiz mais facil
    
    print("As raizes reais possiveis são: \n", raiz , "\n", raiz2)