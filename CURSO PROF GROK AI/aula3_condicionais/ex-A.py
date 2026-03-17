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
