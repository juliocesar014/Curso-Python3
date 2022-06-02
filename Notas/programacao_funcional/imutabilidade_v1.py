# from locale import setlocale, LC_ALL
# from calendar import mdays, month_name
# from functools import reduce

# PTBR
# setlocale(LC_ALL, 'pt_BR')

# Listar todos os meses do ano com 31 dias
meses = [
    {'mes': 'Jan', 'dias': 31},
    {'mes': 'Fev', 'dias': 28},
    {'mes': 'Mar', 'dias': 31},
    {'mes': 'Abr', 'dias': 30},
    {'mes': 'Mai', 'dias': 31},
    {'mes': 'Jun', 'dias': 30},
    {'mes': 'Jul', 'dias': 31},
    {'mes': 'Ago', 'dias': 31},
    {'mes': 'Set', 'dias': 30},
    {'mes': 'Out', 'dias': 31},
    {'mes': 'Nov', 'dias': 30},
    {'mes': 'Dez', 'dias': 31},
]

mes_trinta = filter(lambda d: (d['dias']) >= 31, meses)
print(list(mes_trinta))
