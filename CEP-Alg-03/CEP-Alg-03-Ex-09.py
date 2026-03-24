# Data de feriado. A tabela abaixo mostra os feriados nacionais brasileiros que caem sempre no
# mesmo dia (em oposição aos feriados variáveis como carnaval e corpus christi).

# Confraternização universal 1o. de janeiro
# Tiradentes 21 de abril
# Dia do trabalho 1o. de maio
# Independência do Brasil 7 de setembro
# Nossa Senhora Aparecida 12 de outubro
# Finados 2 de novembro
# Proclamação da República 15 de novembro
# Natal 25 de dezembro

# Escreva um programa Python que leia do usuário o mês e o dia de uma determinada data. Se
# o mês e o dia corresponderem a uma das datas da tabela acima, seu programa deve exibir o
# nome do feriado. Caso contrário o programa deve informar que o dia e o mês informados não
# correspondem a um feriado nacional.

base = {
    (1, 1): "Confraternização Universal",
    (4, 21): "Tiradentes",
    (5, 1): "Dia do Trabalho",
    (9, 7): "Independência do Brasil",
    (10, 12): "Nossa Senhora Aparecida",
    (11, 2): "Finados",
    (11, 15): "Proclamação da República",
    (12, 25): "Natal"
}

print("Verificador de Feriados Nacionais :3")
mes = int(input("Digite o número do mês (1-12): "))
dia = int(input("Digite o dia: "))

#verifica junto
data = (mes, dia)

if data in base:
    feriado = base[data]
    print(f"A data {dia}/{mes} corresponde ao feriado de: {feriado}")
else:
    print(f"O dia {dia} do mês {mes} não corresponde a um feriado nacional fixo.")