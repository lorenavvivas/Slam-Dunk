texto = open('estadisticas_partidos.csv', 'rt')
x = texto.readlines()
for oracion in x:
    print(oracion.strip())