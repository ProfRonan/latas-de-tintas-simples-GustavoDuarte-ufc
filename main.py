print("Bem vindo à Loja de Tintas do seu ZÉ")
metros_quadrados = input("Qual a área em m²?\n")
metros_quadrados = float(metros_quadrados)

# Coloque o código para resolver o problema nessa parte do programa
cobertura = metros_quadrados / 3
if cobertura > 18:
    qtd_de_latas = int(cobertura / 18) + 1
    valor_total = qtd_de_latas * 80
    print(f"Serão necessárias {qtd_de_latas} latas totalizando R$ {valor_total}")
    StopIteration
if cobertura <= 18 and cobertura != 0:
    qtd_de_latas = 1
    valor_total = qtd_de_latas * 80
    print(f"Serão necessárias {qtd_de_latas} latas totalizando R$ {valor_total}")
if metros_quadrados == 0:
# As duas variáveis qtd_de_latas e valor_total devem guardar a resposta do problema
# Troque os zeros pelos valores corretos.
    qtd_de_latas = 0
    valor_total = 0

    print(f"Serão necessárias {qtd_de_latas} latas totalizando R$ {valor_total}")