nome_carro = input("Digite o nome do carro: ")
valor_carro = float(input("Digite o valor do carro: R$"))
consumo_por_litro = input("Digite o consumo por litro: ")

print("-----------------------------------")
print(f"| Carro: {nome_carro}")
print(f"| Valor: R${valor_carro:.2f}")
print(f"| Consumo: {consumo_por_litro}km/l")
print("-----------------------------------")