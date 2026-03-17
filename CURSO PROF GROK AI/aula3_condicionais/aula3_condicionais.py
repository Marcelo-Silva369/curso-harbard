# Aula 3 – Condicionais e decisões

print("=== Aula 3 – Controle de Fluxo ===\n")

idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida!")
elif idade < 13:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")

# Exemplo com operadores lógicos
dinheiro = float(input("Quanto dinheiro você tem na carteira? R$ "))
tem_cartao = input("Tem cartão de crédito? (sim/não): ").lower() == "sim"

if dinheiro >= 100 or tem_cartao:
    print("Você pode comprar o lanche!")
else:
    print("Sem grana nem cartão... fica na vontade.")