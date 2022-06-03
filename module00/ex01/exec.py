import sys

args_list = sys.argv[1:]
str = ' '.join(args_list)
str = str[::-1]
print(str.swapcase())
