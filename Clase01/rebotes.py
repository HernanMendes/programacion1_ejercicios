# rebotes.py
# Archivo de ejemplo
# Ejercicio
altura = 100
amortiguacion = 3/5
cant_rebotes = 1

while cant_rebotes <= 10:
    altura *= amortiguacion
    print(cant_rebotes, round(altura, 4))
    cant_rebotes += 1

