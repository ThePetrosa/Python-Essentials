def suma(*a):
	print("\nTipo de datos del argumento: " ,type(a))
	sum = 0
	for n in a:
		sum += n
		
	print("Suma: ", sum)
suma(1)
suma(5, 8)
suma(9, 3, 5)
