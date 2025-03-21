nome = input("Qual o seu nome completo?: ")
idade = input("Qual é a idade?: ")
cidade = input("Em que cidade você mora: ")
profissao = input("Qual a sua profissão?:? ")
atvhb = input("você poderia descrever um hobby ou atividade que gosta?")

print(f"Esses sõ seus dados: ."
      "Nome: {nome}"
      "Idade: {idade}"
      "Cidade: {cidade}"
      "Profissão: {profissão}"
      "Atividade ou hobby: {atvhb}")

# Função para coletar informações
def coletar_informacoes():
    nome = input("Qual é o seu nome? ")
    cargo = input("Qual é o seu cargo na empresa? ")
    empresa = input("Qual é o nome da empresa onde você trabalha? ")
    salario = input("Qual é o seu salário atual? R$ ")
    tempo_trabalho = input("Há quanto tempo você trabalha nesta empresa? ")
    
    # Exibindo as informações coletadas
    print("\nInformações coletadas:")
    print(f"Nome: {nome}")
    print(f"Cargo: {cargo}")
    print(f"Empresa: {empresa}")
    print(f"Salário: R${salario}")
    print(f"Tempo de trabalho na empresa: {tempo_trabalho}")

# Chama a função para coletar as informações
coletar_informacoes()

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

