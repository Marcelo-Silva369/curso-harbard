# Exercício C - Lista de compras

# 1. Criamos uma lista vazia (como uma sacola vazia)
compras = []

print("Digite os itens da lista de compras")
print("Quando terminar, digite 'fim' ou 'sair'\n")

# 2. Loop infinito até o usuário querer parar
while True:
    item = input("Item: ").strip()   # .strip() remove espaços extras
    
    # 3. Verificamos se o usuário quer parar
    if item.lower() in ["fim", "sair", ""]:
        break   # sai do loop imediatamente
    
    # 4. Se não for para parar, adicionamos na lista
    compras.append(item)
    print(f"Adicionado: {item}")

# 5. Mostramos a lista completa, numerada
print("\n--- Sua lista de compras ---")

if len(compras) == 0:
    print("Você não adicionou nenhum item.")
else:
    for i in range(len(compras)):
        print(f"{i+1}. {compras[i]}")
        