from operator import invert


frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for c in range(len(junto)):
    inverso += junto[c]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Esta frase/palavra é um palíndromo!')
else:
    print('Esta frase/palavra não é um palíndromo!')