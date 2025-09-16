idade_usuario = int(input('Digite sua idade: '))

if 0 <= idade_usuario <= 12:
    print('O usuário é criança')
elif 13 <= idade_usuario <= 17:
        print('O usuário é adolescente')
elif 18 <= idade_usuario:
        print('O usuário é adulto')
else:
    print('Idade informada é inválida')