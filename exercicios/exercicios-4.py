print('Calcular a média de um aluno que cursou a disciplina de Programação 1')

m1 = float(input('Digite a nota M1: '))
m2 = float(input('Digite a nota M2: '))
m3 = float(input('Digite a nota M3: '))

media_aritmetica = round((m1 + m2 + m3) / 3, 1)
print('Nota final do aluno:', media_aritmetica)

if 0.0 <= media_aritmetica <= 4.0:
    print('Aluno reprovado')

elif 4.1 <= media_aritmetica <= 6.0:
        print('Aluno pegou exame')

        nota_exame = float(input('Digite a nota Exame: '))

        if nota_exame > 6.0:
            print('Aluno aprovado')
        else:
            print('Aluno reprovado')

elif media_aritmetica > 6.0:
        print('Aluno aprovado')