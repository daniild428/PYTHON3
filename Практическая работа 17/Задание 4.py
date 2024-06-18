from datetime import datetime, timedelta


def is_happy_date(date, n):
    if date.weekday() == 0 or date.day % 4 == 0:
        return False
    return (date + timedelta(days=n)).weekday() != 0


def find_happy_dates(start_date, n, count):
    happy_dates = []
    current_date = datetime.strptime(start_date, '%Y/%m/%d')

    while len(happy_dates) < count:
        if is_happy_date(current_date, n):
            happy_dates.append(current_date.strftime('%d %B, %A'))
        current_date += timedelta(days=1)

    return happy_dates


# Пример использования
start_date = '2023/06/01'
n = 7
count = 3

happy_dates = find_happy_dates(start_date, n, count)
print('Счастливые даты экзамена:')
for date in happy_dates:
    print(date)