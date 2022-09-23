primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (11 - 1) * razão
for c in range(primeiro, decimo, razão):
    print(c, end='  ➝  ')
print('fim!')