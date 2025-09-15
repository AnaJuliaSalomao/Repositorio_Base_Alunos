nome = input("Digite seu nome:")
temperatura = float(input("Digite sua temperatura: "))

if temperatura > 37.5:
    print("Você está com febre")
else:
    print("Temperatuara normal")

print(f"o nome do paciente é: {nome}\nE a temperatura é: {temperatura}")