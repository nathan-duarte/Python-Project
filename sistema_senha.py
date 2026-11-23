# Esse será um programa de senhas para praticar a função len().

usuario = str(input('Digite seu usuário: '))
senha = str(input('Digite a sua senha: '))

if len(senha) >= 8 :
    print('Acesso confirmado!')
else:
    print('Essa senha contém menos do que 8 caracteres, favor digitar novamente.')

