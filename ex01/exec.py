from sre_constants import NOT_LITERAL_IGNORE
import sys

# n_arg = len(sys.argv)
# n_arg = n_arg - 1
# str = '';
# for arg in sys.argv[1:];
#     if i != n_arg:
#         str += '{} '.format(arg);
#     else:
#         str += '{}'.format(arg);
# print(str);

args_list = sys.argv[1:]
print(args_list)
str = ' '.join(args_list)
rev_str = str[::-1]
print(rev_str.swapcase())
