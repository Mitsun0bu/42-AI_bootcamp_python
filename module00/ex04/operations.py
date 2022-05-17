import sys

n_arg = len(sys.argv[1:])
if n_arg < 2:
	print('Usage : operations.py [integer_1] [integer_2]')
elif n_arg > 2:
	print('Error : too many arguments')
else:
	arg_1 = sys.argv[1]
	arg_2 = sys.argv[2]
	try:
		A = int(arg_1)
		B = int(arg_2)
	except ValueError:
		print('Error : argument should be an int')
	else:
		print("Sum		:	", A + B)
		print("Difference	:	", A - B)
		print("Product		:	", A * B)
		if B != 0:
			print("Quotient	:	", A / B)
			print("Remainder	:	", A % B)
		else:
			print("Quotient	:	ERROR (division by zero)")
			print("Remainder	:	ERROR (modulo zero)")
