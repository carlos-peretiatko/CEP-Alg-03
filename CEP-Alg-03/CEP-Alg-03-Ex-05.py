# Nome do mês e número de dias. A quantidade de dias de um m6es pode variar de 28 a 31
# dias. Neste exercício você deve criar um programa Python que recebe do usuário o nome de
# um mês (como uma string). Então seu programa deve exibir uma mensagem informando a
# quantidade de dias daquele mês. Caso o mês seja fevereiro, sua mensagem pode informar
# “28 ou 29 dias”.


#achei necessario criar um vetor para validação, para nao fazer um macth case gigante
validos = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", 
         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

mes = input("Informe um mes para descobrir quantos dias ele terá: ")
mes = mes.strip().lower()

#diminui e remove espaco

if mes in validos:
    if mes == "fevereiro":
        print("28 ou 29 dias!")
    else:
        print("30 ou 31 dias !!")
else:
    print("Mes inválido!\nOu verifique sua ortografia...")