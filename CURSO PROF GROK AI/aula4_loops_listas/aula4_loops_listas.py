# Aula 4 – Loops e Listas

print("=== Aula 4 – Repetição e Coleções ===\n")

# Exemplo while
tentativas = 0
while tentativas < 3:
    senha = input("Digite a senha (dica: python): ")
    if senha.lower() == "python":
        print("Acesso liberado!")
        break   # sai do loop imediatamente
    else:
        print("Senha incorreta. Tente novamente.")
        tentativas += 1

if tentativas == 3:
    print("Máximo de tentativas atingido. Bloqueado.")

# Exemplo for + lista
alunos = ["Ana", "Bruno", "Carla", "Daniel", "Eduarda"]

print("\nLista de alunos da turma:")
for aluno in alunos:
    print(f"- {aluno}")

# Usando range
print("\nNúmeros pares de 0 a 10:")
for i in range(0, 11, 2):    # início, fim (exclusivo), passo
    print(i)

