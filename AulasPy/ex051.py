count = 0
from datetime import date
pessoas = 0
data = date.today().year
for c in range(0,7):
    count += 1
    idade = int(input('Digite o ano da {} pessoa'.format(count)))
    if data - idade >= 21:
        pessoas += 1
print('{} pessoas são maior de idade'.format(pessoas))
print('{} pessoas são menor de idade'.format(7 - pessoas))