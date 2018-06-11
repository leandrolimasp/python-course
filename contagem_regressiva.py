def anoNovo(n):
	if n == 0:
		print('Feliz Ano Novo')
	else:
		print(n)
		anoNovo(n-1) #recursividade
'''
teste = anoNovo
teste(10)
10 9 8 7 6 5 4 3 2 1 Feliz Ano Novo
'''