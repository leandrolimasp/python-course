#fibonacci de um número é a soma dos 2 fibonaccis antecessores
# fa = (fa-1) + (fa-2) = fb + fc = resultado
#ex: 5f = (4f(4-1)+(4-2)) + (3f(3-1)+(3-2))
#5f = 8 

def fibonacci(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

# teste = fibonacci
# teste(5)
# 8