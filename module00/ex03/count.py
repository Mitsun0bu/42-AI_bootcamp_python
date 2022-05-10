def text_analyzer(*arg):
    """This function analyze a single string arg

    It counts the total number of char and lists :
    - the number of upper characters,
    - the number of lower characters,
    - the number of punctuation marks,
    - spaces."""
    if len(arg) == 0:
        analyze_user_input()
    else:
        analyze_text(arg[0])


def analyze_user_input():
    print('What is the text to analyze?')
    text = input()
    if input_is_int(text) is False:
        analyze_text(text)
    else:
        print("Error: argument is not a string")


def input_is_int(str):
    if str[0] in ('-', '+'):
        return str[1:].isdigit()
    else:
        return str.isdigit()


def analyze_text(text):
    try:
        n_char = len(text)
    except TypeError:
        print("Error: argument is not a string")
        return
    n_uppercase = sum(1 for c in text if c.isupper())
    n_lowercase = sum(1 for c in text if c.islower())
    n_punct_mark = count_punct_mark(text)
    n_space = sum(1 for c in text if c.isspace())
    print("The text contains", n_char, "character(s):\n",
          "-", n_uppercase, "upper letter(s)\n",
          "-", n_lowercase, "lower letter(s)\n",
          "-", n_punct_mark, "punctuation mark(s)\n",
          "-", n_space, "space(s)")


def count_punct_mark(str):
    count = 0
    for c in range(0, len(str)):
        if str[c] in ('!', ",", "\'", ";", "\"", ".", "-", "?"):
            count = count + 1
    return (count)
