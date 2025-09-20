class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def resultado(self):
        if self.media() >= 6.0:
            return 'Aprovado!'
        else:
            return 'Reprovado!'

    def imprime(self):
        return (f'Aluno: {self.nome}, possui as seguintes notas: {self.nota1} e {self.nota2}. '
                f'Com a média {self.media()} e {self.resultado().lower()}')


aluno1 = Aluno('Dyane', 7.8, 8.0)
aluno2 = Aluno('Guilherme', 4.5, 5.0)

print(aluno1.imprime())
print(aluno2.imprime())