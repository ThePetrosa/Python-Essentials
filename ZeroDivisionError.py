def reciproco(n):
	try:
		n = 1/n
	except ZeroDivisionError:
		print("Division Fallida")
		return None
	else:
		print("Bien")
		return n
print(reciproco(2))
print(reciproco(0))
