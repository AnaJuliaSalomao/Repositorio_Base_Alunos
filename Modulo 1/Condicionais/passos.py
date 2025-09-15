nome = input("Digite seu nome: ")
passos = float(input("digite seus passos: "))

if passos > 8000:
    print("Ótimo, você se movimentou bem hoje. ")
else:
    print("Tente se movimentar mais amanhã! ")

print(f"o nome é: {nome}\nE o passo é: {passos}")