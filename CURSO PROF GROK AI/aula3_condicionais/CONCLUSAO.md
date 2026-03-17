# Aula 3 concluída ✅

Dúvidas: Não

# Código completo do Exercício A (aprovado/reprovado):

nota1 = float(input('Digite a Primeira nota: '))
nota2 = float(input('Digite a Segunda nota: '))

calculo_media = (nota1 + nota2) / 2
media = calculo_media

if media >= 7:
    resultado = 'Aprovado'
elif media >= 5 and media < 7:
    resultado = 'Recuperação'
else:
    resultado = 'Reprovado'

print(f'\nMédia: {media:.1f}\nResultado: {resultado}')


# Código completo do Exercício B (adivinhação):

palpite = int(input('Qual é o número Secreto?\nDigite seu palpite aqui-->: '))

num_secreto = 33

if palpite > num_secreto:
    dica = 'Muito Alto!'
elif palpite < num_secreto:
    dica = 'Muito Baixo!'
else:
    dica = 'Parabéns você acertou!!!'

print(f'Papite: {dica}\nO npumero secreto era {num_secreto}')

# Saída de exemplo de um exercício:

Digite a Primeira nota: 10
Digite a Segunda nota: 5.5

Média: 7.8
Resultado: Aprovado

# Link do repositório atualizado:
https://github.com/Marcelo-Silva369/curso-harbard