# Exercício B - Somador de números (versão simples e explicada)

# 1. Perguntamos quantos números vamos somar
quantidade = int(input("Quantos números você quer somar? "))

# 2. Criamos uma variável para guardar a soma (começa em 0)
soma = 0

# 3. Vamos usar um contador para controlar quantas vezes perguntamos
contador = 1   # começa em 1 para ficar mais natural para o usuário

# 4. Enquanto o contador for menor ou igual à quantidade desejada...
while contador <= quantidade:
    # Perguntamos o número atual
    numero = float(input(f"Digite o número {contador} de {quantidade}: "))
    
    # Somamos ele na variável soma
    soma = soma + numero   # ou soma += numero (mesma coisa)
    
    # Aumentamos o contador para a próxima vez
    contador = contador + 1   # ou contador += 1

# 5. Depois que sai do loop, calculamos a média
if quantidade > 0:   # evitamos divisão por zero
    media = soma / quantidade
else:
    media = 0

# 6. Mostramos o resultado
print("\n--- Resultado ---")
print(f"Você digitou {quantidade} números")
print(f"Soma total: {soma}")
print(f"Média: {media:.1f}")