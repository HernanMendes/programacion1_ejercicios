# Imprimir cabecera de la tabla
def print_headers():
	print(f"{'':>3s}", end='')

	for i in range(10):
		print(f"{i:>5d}", end='')
	print()

	for i in range(4):
		print('-', end='')
	for i in range(10):
		for i in range(5):
			print('-', end='')
	print()


# Imprimir tabla de multiplicar
def print_table():
	for i in range(10):
		suma = 0
		print(f"{i:>2d}:", end='')
		for j in range(10):
			print(f"{(suma):>5d}", end='')
			suma += i
		print()
		

def main():
	print_headers()
	print_table()
	

if __name__ == '__main__':
	main()
	

