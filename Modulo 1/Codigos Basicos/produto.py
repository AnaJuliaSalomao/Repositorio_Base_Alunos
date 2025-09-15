nome_produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual do desconto %: "))

valor_desconto = preco * desconto / 100 

preco_final = preco - valor_desconto
print("---------------------------")
print(f"Produto: {nome_produto}\n Preco final; {preco_final}")
print("---------------------------")