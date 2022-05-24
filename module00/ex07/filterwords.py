import sys


def print_error():
    print('Error !')
    print('Usage : python3 filterwords.py [arg_1] [arg_2]')
    print('arg_1 should be a str and arg_2 should be an int')


def arg_is_int(str):
    if str[0] in ('-', '+'):
        return str[1:].isdigit()
    else:
        return str.isdigit()


def args_are_valid(arg_1, arg_2):
    if (isinstance(arg_1, str) and arg_is_int(arg_2)):
        return True
    else:
        print_error()
        return False


arg_list = sys.argv[1:]
n_arg = len(arg_list)
if n_arg != 2:
    print_error()
else:
    a_1 = arg_list[0]
    a_2 = arg_list[1]
    if (args_are_valid(a_1, a_2)):
        a_2 = int(arg_list[1])
        lst = a_1.split()
        trm = [lst[i].strip(" .,;\'\"-!?") for i in range(0, len(lst))]
        res = []
        [res.append(trm[i]) for i in range(0, len(trm)) if len(trm[i]) > a_2]
        # for i in range(0, len(trm)):
        #     if len(trm[i]) > a_2:
        #         res.append(trm[i])
        print(res)
