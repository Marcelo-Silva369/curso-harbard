palpite = int(input('Qual é o número Secreto?\nDigite seu palpite aqui-->: '))

num_secreto = 33

if palpite > num_secreto:
    dica = 'Muito Alto!'
elif palpite < num_secreto:
    dica = 'Muito Baixo!'
else:
    dica = 'Parabéns você acertou!!!'

print(f'Papite: {dica}\nO npumero secreto era {num_secreto}')