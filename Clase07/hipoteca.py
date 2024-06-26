# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
mes = 0

while saldo > 0:
    mes += 1
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo -= pago_extra
        total_pagado += pago_extra
    if saldo < 0:
        total_pagado += saldo
        saldo -= saldo
    print(mes, round(total_pagado,2), round(saldo,2))

print('Total pagado', round(total_pagado, 2))
print('Meses:', mes)
