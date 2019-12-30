texto = open("estadisticas_partidos.csv", "rt")
filas = 0
for i in texto.readlines():
    columnas = 0
    for j in i.split(','):
        columnas += 1
        if len(j) > filas:
            filas = len(j)
texto.seek(0)
for i in texto.readlines():
    print('-' * (filas * columnas + ((columnas - 1) * 3) + 2 * 2))
    for k in i.split(','):
        print('| {:^{filas}} '.format (k.strip(), filas=filas), end='')
    print('|')

print('-' * (filas * columnas + ((columnas - 1) * 3) + 2 * 2))
texto.close()