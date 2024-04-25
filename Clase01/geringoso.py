cadena = 'boligoma'
capadepenapa = ''
for c in cadena:
    if c == 'a':
        c += 'pa'
    if c == 'e':
        c += 'pe'
    if c == 'i':
        c += 'pi'
    if c == 'o':
        c += 'po'    
    if c == 'u':
        c += 'pu'
    capadepenapa += c
print(capadepenapa)
