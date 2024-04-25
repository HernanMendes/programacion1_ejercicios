import random


valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor, palo) for valor in valores for palo in palos]

# Una carta al azar
print(random.choice(naipes))

# Tres cartas al azar (con reposicion)
print(random.choices(naipes, k=3))

# Tres cartas al azar (sin reposicion)
print(random.sample(naipes, k=3))
