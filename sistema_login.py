# programa de login e senha.

nome = str(input('Digite o seu usuário: '))

senha = str(input('Digite a sua senha: '))

especiais = '!@#$%&*'

if ' ' in nome or len(nome) < 3:
    print('Usuário inválido. Digite novamente.')
else:
    print('Usuário ok!!')

if ' ' in senha or len(senha) < 8 or not (set(senha) & set(especiais)):
    print('Senha inválida. Favor, digitar novamente.')
else:
    print('Senha correta! Pode acessar!!')
