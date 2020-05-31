#!/usr/bin/env python3

import argparse
import calendar
import datetime
import pathlib
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

MONTH_CAL_HEADER = '''
 Seg | Ter | Qua | Qui | Sex | Sáb | Dom 
 --- | --- | --- | --- | --- | --- | --- 
'''

DATE_BODY = '''


* [Manhã](#manha)
* [Tarde](#tarde)
* [Noite](#noite)

<a name="manha">

## Manhã

## Tarde

## Noite
'''

def year2md(year: int, year_dir: pathlib.Path, index: str):
    year_dir.mkdir()
    year_index = year_dir / index
    year_header = f'# Ano de {year}'
    with year_index.open('w', encoding='utf-8') as year_file:
        year_file.write(year_header)
        year_file.write(f'''

||||
|---|---|---|
|[Janeiro](01/{index})|[Fevereiro](02/{index})|[Março](03/{index})|
|[Abril](04/{index})|[Maio](05/{index})|[Junho](06/{index})|
|[Jullho](07/{index})|[Agosto](08/{index})|[Setembro](09/{index})|
|[Outubro](10/{index})|[Novembro](11/{index})|[Dezembro](12/{index})|
    '''
    )
    # LIST => 
    # lines.extend([f'* [{month_pt[m]}]({m:02d}/README.md)' for m in range(1, 13)])
    # MATRIX =>

def day2md(date: datetime.datetime, month_dir: pathlib.Path, index: str):
    date_dir = month_dir / f'{date.day:02d}'
    date_dir.mkdir()
    date_index = date_dir / index
    year = date.year
    month = date.month
    month_name = month_pt[month]
    day = date.day
    weekday = date.weekday()
    weekday_name = weekdays_pt[weekday][1]
    date_header = f'# {weekday_name}, {day} de {month_name} de {year}'
    with date_index.open('w', encoding='utf-8') as date_file:
        date_file.write(date_header)
        date_file.write(DATE_BODY)            

def month2md(year: int, month: int, year_dir: pathlib.Path, index: str):
    cal = calendar.Calendar(firstweekday=calendar.MONDAY)
    month_dir = year_dir / f'{month:02d}'
    month_dir.mkdir()
    month_index = month_dir / index
    month_header = f'# {month_pt[month]} de {year}'
    with month_index.open('w', encoding='utf-8') as month_file:
        month_file.write(month_header)
        month_file.write(MONTH_CAL_HEADER)
        for di,date in enumerate(cal.itermonthdates(year, month)):
            cel_content = '   '
            if month == date.month:
                day2md(date, month_dir, index)
                cel_content = f'[{date.day:>3}]({date.day:02d}/{index})'
            if (di%7) != 6:
                month_file.write(f'{cel_content}|')
            else:
                month_file.write(f'{cel_content}\n')


def calendar2markdown(year: int, index:str, path: pathlib.Path):
    year_dir = path / str(year)
    if not year_dir.exists():
        year2md(year, year_dir, index)
        for month in range(1, 12+1):
            month2md(year, month, year_dir, index)

def main():
    now = datetime.datetime.now()
    parser = argparse.ArgumentParser(description='Gerador de calendário em formato Markdown')
    parser.add_argument('year', 
                        default=now.year, 
                        help='Year from which you want to build the calendar in Markdown format', 
                        nargs='?',
                        type=int)
    parser.add_argument('-i', '--index',
                        default='index.md',
                        help='Index file to be created in each directory. Defaults to <index.md>',
                        )
    parser.add_argument('-p', '--path',
                        default=pathlib.Path.cwd(),
                        help='Path in which the calendar will be created.'
                        )

    args = parser.parse_args()
    path = pathlib.Path(args.path) if str==type(args.path) else args.path
    # Check if index is a valide filename
    index = pathlib.Path(args.index)
    if index.name != args.index:
        sys.exit(1)
    elif index.suffix != '.md':
        sys.exit(2)

    calendar2markdown(args.year, args.index, path)

if __name__ == '__main__':
    main()
