senha = input('Digite sua senha: ')

if len(senha) < 6:
    validacao = 'Senha muito curta!'
else:
    validacao = 'Senha validada!'

print(validacao)