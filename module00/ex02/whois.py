import sys

arg_list = sys.argv[1:]
n_arg = len(arg_list)
if n_arg == 0:
    print('Usage : whois.py [single int argument]')
elif n_arg == 1:
    try:
        converted_arg = int(arg_list[0])
    except ValueError:
        print("Error : argument is not an integer")
    else:
        if converted_arg == 0:
            print("I'm Zero. ")
        elif (converted_arg % 2) == 0:
            print("I'm Even. ")
        else:
            print("I'm Odd. ")
else:
    print("Error: more than one argument is provided")
