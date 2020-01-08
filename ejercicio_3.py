import csv
with open('estadisticas_partidos.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    print('-' * 65)
    print('|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Team 1', 'S', 'Team 2', 'S'))
    for i, v in enumerate(reader):
        try:
            score_1, score_2 = v['Score'].split('-')
        except ValueError as e:
            score_1 = 'Unknown'
            score_2 = 'Unknown'
        if i == 0:
            print('-' * 65)
        if v['Team 1'] == v['Winner']:
            print('|{:^15}|{:^15}|{:^15}|{:^15}|'.format(v['Team 1'], score_1, v['Team 2'], score_2))
        else:
            print('|{:^15}|{:^15}|{:^15}|{:^15}|'.format(v['Team 1'], score_2, v['Team 2'], score_1))
    print('-' * 65)


