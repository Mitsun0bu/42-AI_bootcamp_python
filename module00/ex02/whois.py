import sys

arg_list = sys.argv[1:]
n_arg = len(arg_list)
if n_arg == 1:
	try:
		converted_arg = int(arg_list[0])
	except TypeError:
		print("Error : argument is not an integer")
	else:
		print(converted_arg)
else:
	print("Error: more than one argument is provided")
