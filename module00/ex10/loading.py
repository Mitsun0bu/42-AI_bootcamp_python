import time
import timeit
import sys

def ft_progress(listy, wdth = 60):
    start_time = timeit.default_timer()
    lst_size = len(listy)
    j = 0
    for i in listy:
        yield i
        if (i / lst_size * wdth >= j + 1):
            j += 1
        print_bar(j + 1, i + 1, wdth, lst_size, timeit.default_timer() - start_time)
    
def print_bar(j, i, wdth, lst_size, elapsed_time):
    progress = j / wdth
    eta = elapsed_time / progress * (1 - progress)
    string = "ETA : {0:.2f}s [{1: >2.0f}%][{2}] {3}{4} | elapsed time {5:.2f}s"
    bar = string.format(eta,
                        progress * 100,
                        "=" * (j - 1) + ">" * (i != lst_size) + " " * (wdth - j),
                        i,
                        lst_size,
                        elapsed_time)
    sys.stdout.flush()
    sys.stdout.write("\r" + bar)
    sys.stdout.flush()

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)