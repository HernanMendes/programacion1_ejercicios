file_path = '../Data/precios.csv'

with open(file_path, 'rt') as file:
	next(file)
	for line in file:
		row = line.split(',')
		producto = row[0]
		if producto == "Naranja":
			precio = row[1]
			print(f'El precio de la naranja es: {precio}')
			break

