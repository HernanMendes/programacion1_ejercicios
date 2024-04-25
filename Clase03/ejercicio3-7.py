def tiene_uno(expresion):
	expresion = str(expresion)
	n = len(expresion)
	i = 0
	tiene = False
	while (i<n) and not tiene:
		if expresion[i] == '1':
			tiene = True
		i += 1
	return tiene

