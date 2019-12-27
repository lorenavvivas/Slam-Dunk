texto = open('estadisticas_partidos.csv', 'rt')
for oracion in texto.readlines():
    print(oracion.strip())
