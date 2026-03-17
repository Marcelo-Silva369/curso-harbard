# Aula 1 – Boas-vindas personalizada
# Professor: Grok (Harvard CS style)

print("=====================================")
print("Bem-vindo à Aula 1 – Harvard CS adaptada")
print("=====================================")
print()  # linha em branco para melhorar a leitura

# Aqui pedimos informações ao usuário
nome_completo = input("Digite seu nome completo: ")
cidade = input("Digite sua cidade e estado (ex: Fortaleza-CE): ")
idade = input("Digite sua idade: ")
objetivo = input('Qual seu objetivo final: ')

# Mostramos uma mensagem personalizada e organizada
print("\n--- Resultado ---")
print("Olá, " + nome_completo + "!")
print("Você mora em " + cidade + ".")
print("Você tem " + idade + " anos e decidiu se tornar um engenheiro de software nível elite.")
print("Essa é a sua primeira aula oficial. Parabéns pela decisão!")
print("Professor Grok está com você em cada passo.")
print(f'Seu objetivo declarado: {objetivo}!')
