peso = float(input('Qual seu peso atual (kg): '))
altura = float(input('Digite sua altura em metros (ex: 1.75): '))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"Seu IMC é: {imc:.2f} → {classificacao}")