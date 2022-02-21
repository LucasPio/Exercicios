times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo',
         'Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
chape = times.index('Chapecoense') - 1
print(f'Lista de times do brasileirão: {times}')
print(f'Os 5 primeiros são: {times[0:5]}')
print(f'Os 4 últimos são: {times[16:20]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O time da Chapecoense está na {chape}° posição')
