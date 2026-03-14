# Aula 2 – Variáveis, tipos e operações
print("=== Aula 2 – Harvard CS adaptada ===\n")

# Exemplos de variáveis
nome = "Marcelo Silva"
idade_str = input("Digite sua idade novamente: ")   # vem como string
idade = int(idade_str)                               # convertemos para int

altura = float(input("Digite sua altura em metros (ex: 1.75): "))
cidade = "Toritama"

peso = float(input('Qual seu peso atual: '))

# Operações matemáticas
idade_em_5_anos = idade + 5
imc_caluco = peso / (altura ** 2)   # peso fictício 75 kg

if imc_caluco < 18.5:
    imc = "Abaixo do Peso"
elif imc_caluco < 24.9:
    imc = "Peso Normal"
else:
    imc = "Obeso"


# Saídas organizadas com f-strings (melhor prática)
print(f"Olá, {nome}!")
print(f"Você tem {idade} anos → em 5 anos terá {idade_em_5_anos} anos.")
print(f"Sua altura: {altura} m")
print(f"IMC (com {peso}): {imc_caluco:.2f}")   # :.2f = 2 casas decimais
print(f'Você está: {imc}')
print(f"Tipo da variável idade: {type(idade)}")
print(f"Tipo da variável altura: {type(altura)}")