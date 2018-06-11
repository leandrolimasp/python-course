def imprimeMultiplos(n,tamanho):
	i=1
	while i <= tamanho:
		print(n*i, '\t',end='')
		i += 1
	print()

'''
import teste
p=teste
p.imprimeMultiplos(10)
10      20      30      40      50      60
'''

def imprimeTabMult(tamanho):
	i = 1
	while i <= tamanho:
		imprimeMultiplos(i,tamanho)
		i +=1
'''
p.imprimeTabMult()
1       2       3       4       5       6
2       4       6       8       10      12
3       6       9       12      15      18
4       8       12      16      20      24
5       10      15      20      25      30
6       12      18      24      30      36
'''
