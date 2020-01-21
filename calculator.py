
class Calculator:
	def __init__(self):
		pass

	def calculate(f):
		while True:
			print('\n===== CALCULATOR =====\n')
			print('	 1 -- Addition')
			print('	 2 -- Subtraction')
			print('	 3 -- Multiplication')
			print('	 4 -- Division')
			print('	 5 -- Percentage')
			print('	 6 -- Exponentiation')
			print('	 7 -- Floor Division')
			print('	 8 -- Exit\n')
			x = int(input('Choice an option: '))
			
			if x == 8:
				print('Byee...'); exit()

			elif x not in range(1,8):
				print('Invalid Option')
			
			else:
				a = float(input('1° Number: '))
				b = float(input('2° Number: '))

				if x==1:
					print('Result:',a+b)
				elif x==2:
					print('Result:',a-b)
				elif x==3:
					print('Result:',a*b)
				elif x==4:
					print('Result:',a/b)
				elif x==5:
					print('Result:',int(a*b)/100)
				elif x==6:
					print('Result:',a**b)
				elif x==7:
					print('Result:',a//b)

x = Calculator()
x.calculate()
