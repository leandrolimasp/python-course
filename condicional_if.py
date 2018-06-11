#if elif else
x = 10
y = 20
if x < y:
	print('x é menor que y')
elif x > y:
	print('x é maior que y')
else:
	print('x é igual a y')
# x é menor que y

#checar se um número é par ou ímpar
def par_ou_impar(x):
	if x % 2 == 0:
		print(x, 'é um número par')
	elif x % 2 != 0:
		print(x, 'é um número impar')
	else:
		print('número inválido !')
# numero = par_ou_impar
# numero(43)
# 43 é um número impar
# numero(50)
# 50 é um número par

def par_ou_impar(x,y):
		if x % y == 0:
			return True
		else:
			return False



