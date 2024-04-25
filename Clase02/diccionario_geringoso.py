def diccionario_geringoso(palabras):
	dict_geringoso = {}
	for palabra in palabras:
		palabra_geringoso = ''
		for c in palabra:
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
			palabra_geringoso += c
		dict_geringoso[palabra] = palabra_geringoso
		
	return dict_geringoso
	
# Usando palabras = ['banana', 'manzana', 'mandarina'] como input
# nos devuelve {'banana': 'bapanapanapa', 'manzana': 'mapanzapanapa', 'mandarina': 'mapandaparipinapa'}

