# search - encontrar ou pesquisar posições de padrões dentro de uma string
# match - se o começo de uma string é de um determinado padrão
# findall - encontrar todas as substrings de uma string que correspondam a um padrão

# . - ponto, qualquer caractere (exceto linha nova)
# \w - qualquer caractere alfanumérico
# \W - qualquer caractere não-alfanumérico
# \d - qualquer caractere que seja um digio (0-9)
# \D - qualquer caractere não dígito
# \s - espaço em branco
# ^ - começa com
# $ - termina com
# "\" - usado antes de metacaracteres para especificar seu significado literal
# [] - opcional entre os que estão dentro dos colchetes
# () - captura grupos de caracteres
# * - de zero a mais vezes
# ? - zero ou mais vez
# + - uma ou mais vezes
# {m,n} - de m a n vezes
# | - ou

# gabrielcosta@hotmail.com
# felipearruda@gmail.com
# joaosilva@yahoo.com.br

# expressão regular -> \w+@\w+\.\w+
# \w - qualquer caracter alfanumérico, + - uma ou mais vezes
# @ - caracter, \w - qualquer caracter alfanumérico, + - uma ou mais vezes
# \. - ponto final
# \w - qualquer caracter alfanumérico, + - uma ou mais vezes

import re

frase = 'Olá, meu número de telefone é (42)0000-0000'
frase2 =  'A placa de carro que eu anotei durante o acidente foi FRT-1998'
frase3 = 'Entre em contato, meu email é teste@teste.com'

telefone = re.search(r'\(\d{2}\)\d{4,5}-\d{4}', frase)
print(telefone)

placa = re.search(r'[A-Z]{3}-\d{4}', frase2)
print(placa)

email = re.search(r'\w+@\w+\.com', frase3)
print(email)

frase4 =  'FRT-1998 é a placa do carro'
frase5 =  'A placa do carro é FRT-1998'

placa2 = re.match(r'[A-Z]{3}-\d{4}', frase4)
print(placa2)

placa3 = re.match(r'[A-Z]{3}-\d{4}', frase5)
print(placa3)

frase6 = 'Meu número de telefone atual é (42)0000-0000. O número (56)1111-1111 é o antigo'

frase7 = '''Nome: Teste 1
email: teste1@teste.com
Nome: Teste 2
email: teste2@teste.com
Nome: Teste 3
email: teste3@teste.com.br
'''

telefones = re.findall(r'\(\d{2}\)\d{4,5}-\d{4}', frase6)
print(telefones)

emails = re.findall(r'\w+@\w+\.\w+(?:\.br)?', frase7)
print(emails)