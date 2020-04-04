import calendar
import datetime
import sys

texto_mes = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}

def linha2md(texto: str) -> str:
    lista = list(f'{texto:<20}')
    lista.insert(0, '|')
    lista.append('')
    for i in range(3, 22, 3):
        lista[i] = ' |'
    return ''.join(lista)

def principal():
    num_args = len(sys.argv)
    if num_args == 1:
        num_mes = datetime.datetime.now().month
        ano = datetime.datetime.now().year
    elif num_args == 2:
        num_mes = int(sys.argv[1])
        ano = datetime.datetime.now().year
    elif num_args == 3:
        num_mes = int(sys.argv[1])
        ano = int(sys.argv[2])

    calendario = calendar.TextCalendar(firstweekday=calendar.SUNDAY)
    txt_mes = calendario.formatmonth(ano, num_mes).splitlines()
    txt_md = [f'# {texto_mes[num_mes]}', '']

    mes_md = ['|Dom|Seg|Ter|Qua|Qui|Sex|Sáb|', '|---|---|---|---|---|---|---|']

    for linha in txt_mes[2:8]:
        mes_md.append(linha2md(linha))

    txt_md.extend(mes_md)
    print('\n'.join(txt_md))

if __name__ == '__main__':
    principal()