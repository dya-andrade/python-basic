import re

def extrairNumeros(texto):
    return re.findall(r'\d+', texto)


numeros = '''numero: 123456
numero: 14555
numero: 88999
issoENumero: 788854
'''

print(extrairNumeros(numeros))

def extrairCEPs(texto):
    return re.findall(r'\d{5}-\d{3}', texto)

ceps = '''CEP: 06815-390
issoECEP: 06217-155
cep: 72806-140
issoNaoECEP: 06812390
'''

print(extrairCEPs(ceps))

def extrairURLs(texto):
    return re.findall(r'\www\.\w+\.\w*', texto)

# https?://[A-Za-z0-9./]+

urls = '''URL: http://www.udemy.com/
issoEURL: https://www.udemy.com/
url: www.udemy.com/
issoNaoEURL:ww.udemy.com
'''

print(extrairURLs(urls))

print(re.findall(r'https?://[A-Za-z0-9./]+', urls))