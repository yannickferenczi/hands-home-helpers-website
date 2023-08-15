def get_day_link(year, month, day_number):
    return f'<a href="/appointments/dailycalendar/{year}/'\
        f'{month}/{day_number}/">{day_number}</a>'
