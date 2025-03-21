# Função para coletar informações do produto
def coletar_informacoes_produto():
    nome_produto = input("Qual é o nome do produto? ")
    categoria_produto = input("Qual é a categoria ou tipo do produto? ")
    quantidade_estoque = input("Qual é a quantidade disponível em estoque? ")
    data_validade = input("Qual é a data de validade do produto? (dd/mm/aaaa) ")
    validade_aplicavel = input("A data de validade é aplicável? (sim/não) ")
    
    # Exibindo as informações coletadas
    print("\nInformações coletadas sobre o produto:")
    print(f"Nome do Produto: {nome_produto}")
    print(f"Categoria: {categoria_produto}")
    print(f"Quantidade em Estoque: {quantidade_estoque}")
    print(f"Data de Validade: {data_validade}")
    print(f"Validade Aplicável: {validade_aplicavel.capitalize()}")

# Chama a função para coletar as informações do produto
coletar_informacoes_produto()
