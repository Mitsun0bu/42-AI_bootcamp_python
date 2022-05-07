import sys

args_list = sys.argv[1:]
str = ' '.join(args_list)
rev_str = str[::-1]
print(rev_str.swapcase())
