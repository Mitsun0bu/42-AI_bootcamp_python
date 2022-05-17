kata = "The right format"

str_init = ''
len_max = 42
str_dash_len = len_max - len(kata)
str_dash = str_init.ljust(str_dash_len, '-')
final_str = str_dash + kata
print(final_str)
