## Modulo datetime

El módulo datetime nos permite trabajar con fechas y horas en Python.

Posee las clases:
- date: fecha
- time: hora
- datetime: fecha y hora
- timedelta: duración

Y los métodos:
- today(): fecha actual
- now(): fecha y hora actual
- utcnow(): fecha y hora actual en UTC
- fromtimestamp(t): fecha y hora a partir de un timestamp
- strptime(s, f): fecha y hora a partir de un string
- strftime(f): string a partir de una fecha y hora
- combine(d, t): fecha y hora a partir de una fecha y una hora
- replace(): reemplaza partes de una fecha y hora
- astimezone(tz): cambia la zona horaria
- timestamp(): timestamp a partir de una fecha y hora
- isoformat(): string en formato ISO

Se usan los siguientes formatos:
- %Y: año
- %m: mes
- %d: día
- %H: hora
- %M: minuto
- %S: segundo
- %f: microsegundo
- %z: zona horaria
- %a: día de la semana
- %b: mes
- %j: día del año
- %U: semana del año
- %W: semana del año
- %c: fecha y hora
- %x: fecha
- %X: hora
- %I: hora (12 horas)
- %p: AM/PM
- %Z: zona horaria
