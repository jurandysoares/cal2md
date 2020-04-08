#!/usr/bin/env python3

#import argparse
import calendar
import datetime
import os
import sys

month_pt = { # Months in Portuguese
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

weekdays_pt = {
    0: ('Seg', 'Segunda-feira'),
    1: ('Ter', 'Terça-feira'),
    2: ('Qua', 'Quarta-feira'),
    3: ('Qui', 'Quinta-feira'),
    4: ('Sex', 'Sexta-feira'),
    5: ('Sáb', 'Sábado'),
    6: ('Dom', 'Domingo'),
}

def parse_args() -> (int, int):
    num_args = len(sys.argv)
    if num_args == 1:
        num_month = datetime.datetime.now().month
        year = datetime.datetime.now().year
    elif num_args == 2:
        num_month = int(sys.argv[1])
        year = datetime.datetime.now().year
    elif num_args == 3:
        num_month = int(sys.argv[1])
        year = int(sys.argv[2])
    else:
        sys.exit(1)

    return year, num_month

def make_dir_days(year, num_month, days):
    for day in range(1, calendar.monthrange(year, num_month)[1]+1):
        date_path = f'{year}/{num_month:02d}/{day:02d}'
        date_pt = f'{weekdays_pt[days[day].weekday()][1]}, {day} de {month_pt[num_month]} de {year}'
        os.makedirs(date_path, exist_ok=True)
        day_fname = f'{date_path}/README.md'
        if not os.path.exists(day_fname): # Doesn't overwrite existing file
            with open(day_fname, 'w') as dayfile:
                dayfile.write(f''' # {date_pt}

* [Manhã](#manha)
* [Tarde](#tarde)
* [Noite](#noite)

<a name="manha">

## Manhã

## Tarde

## Noite
''')

def year2md(year: int):
    lines = [f'# Ano de {year}', '']
    lines.extend([f'* [{month_pt[m]}]({m:02d}/README.md)' for m in range(1, 13)])
    return '\n'.join(lines)    

def month2md(num_month: int, month: list) -> str:
    abr_wkd_pt = [v[0] for _,v in weekdays_pt.items()]
    table_markup = 7*['---']
    lines = [
        '|'+('|'.join(abr_wkd_pt))+'|',
        '|'+('|'.join(table_markup))+'|'
        ]
    for week in month:
        week_line = [f'[{date.day:>3}]({date.day}/)' if date.month==num_month else '   ' for date in week]
        lines.append('|'+('|'.join(week_line))+'|')

    return '\n'.join(lines)

def main():
    #parser = argparse.ArgumentParser(description='Gera calendário em formato Markdown')
    year, num_month = parse_args()
    cal = calendar.TextCalendar(firstweekday=calendar.SUNDAY)
    month = cal.monthdatescalendar (year, num_month)

    days = {}
    for week in month:
        for date in week:
            if date.month == num_month:
                days[date.day] = date

    make_dir_days(year, num_month, days)
    year_fname = f'{year}/README.md'
    if not os.path.exists(year_fname):
        with open(year_fname, 'w') as year_file:
            year_file.write(year2md(year))    
    
    month_fname = f'{year}/{num_month:02d}/README.md'
    if not os.path.exists(month_fname):
        with open(month_fname, 'w') as month_file:
            month_file.write(month2md(num_month, month))

if __name__ == '__main__':
    main()