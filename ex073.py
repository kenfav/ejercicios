times = ('Philadelphia 76ers', 'Brooklyn Nets', 'Milwaukee Bucks', 'Atlanta Hawks', 'Miami Heat',
    'New York Knicks', 'Charlotte Hornets', 'Boston Celtics', 'Indiana Pacers', 'Chicago Bulls',
    'Toronto Raptors', 'Washington Wizards', 'Cleveland Cavaliers', 'Orlando Magic', 'Detroit Pistons')
print(f"{'CLASSIFICACAO NBA':=^35}")
print("Playoffs elegibles: ")
for time in range(0,5):
    print(f"{time + 1} - {times[time]:.>30}")
print(f'{"Ultimos 4 colocados":=^35}')
for time in range(len(times)-3, len(times)+1):
    print(f"{time} - {times[time-1]:.>30}")
print(f"{'Ordem alfabetica:':=^35}")
for time in sorted(times):
    print(f"{time:.>30}")
print(f" O time Miami Heat esta na {times.index('Miami Heat')+1} posicao")
