#fatorial é um numero multiplicado pelo seus antecessores
#ex: 5! = 5*4*3*2*1=120
def fatoriando(n):
	#1 é um número inteiro
	if type(n) != type(1):
		return 'Somente n°s inteiros'
	elif n < 0:
		return 'Somente n°s inteiros positivos'
	elif n == 0 or n == 1:
		return 1
	else:
		return n * fatoriando(n-1)
'''
import fatorial
teste=fatorial
teste.fatoriando(5)
120
'''

#ou

'''
from fatorial import fatoriando
teste=fatoriando
teste(5)
120
'''

