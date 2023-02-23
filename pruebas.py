import datetime as dt
import locale

locale.setlocale(locale.LC_ALL, '')

fecha_actual = dt.datetime.now()
print(fecha_actual.strftime('%Y%m%d%H%M'))