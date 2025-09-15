try:
   nome = input("Digite seu nome: ")
   altura = float(input("Digite sua altura: "))
   peso = float(input("Digite seu peso: "))
   imc = peso / (altura * altura)

   if imc < 18.5:
    print("Abaixo do peso")
   elif imc < 24.9: 
    print("peso normal")
   elif imc < 29.9:
    print("sobrepeso")
   elif imc < 34.9:
    print("obesidade Grau I")
   elif imc < 39.9:
    print("obesidade Grau II")
   else:
    print("obedidade Grau III (morbida)")


   print(f"o nome do paciente é: {nome}\nE o imc é: {imc}")
except:
   print("informação incorreta, tente novamente" )