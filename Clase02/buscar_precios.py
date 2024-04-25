def buscar_precio(producto_pedido):
	file_path = '../Data/precios.csv'
	fruta_encontrada = False
	
	with open(file_path, 'rt') as file:
		for line in file:
			row = line.split(',')
			nombre_producto = row[0]
			if nombre_producto == producto_pedido:
				fruta_encontrada = True
				precio = row[1]
				print(f'El precio de un cajon de {producto_pedido} es: {precio}', end = '')
				break
		if fruta_encontrada == False:
			print(f'{producto_pedido} no figura en el listado de precios.')

