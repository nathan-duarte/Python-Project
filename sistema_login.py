# programa de login e senha.

nome = str(input('Digite o seu usuário: '))

senha = str(input('Digite a sua senha: '))


if len(nome) < 3 or '':
    print('Usuário inválido. Digite novamente.')
else:
    print('Usuário ok!')

if len(senha) == 0:
    print('A senha não pode estar vazia. Digite novamente.')
elif len(senha) < 7:
    print('Sua senha não contém os caracteres necessários, favor digitar novamente.')
elif len(senha) == ' ':
    print('Sua senha não pode conter espaços em branco. Digitar novamente.')
elif len(senha).isalnum():
    print('Sua senha não tem cacactere especial. Digitar novamente.')
else:
    print('Senha digitada com sucesso!')

