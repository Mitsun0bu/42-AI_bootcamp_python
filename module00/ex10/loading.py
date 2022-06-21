import time
import timeit
import sys

def ft_progress(lst: list) -> None:
    start_time = timeit.default_timer()
    bar_len = 100
    lst_len = len(lst)
    i_bar = 0
    for i_lst in lst:
        yield i_lst
        if (i_lst / lst_len * bar_len >= i_bar + 1):
            i_bar += 1
        print_bar(i_bar + 1, i_lst + 1, bar_len, lst_len, start_time)
    
def print_bar(i_bar, i_lst, bar_len, lst_len, start_time):
    elapsed_time = timeit.default_timer() - start_time
    progress = i_bar / bar_len
    # ETA means estimated time of arrival
    # (elapsed_time / progress) : time required for current progress
    # (1 - progress) : progress still to be made 
    eta = elapsed_time / progress * (1 - progress)
    string = "ETA : {0:.2f}s [{1: >2.0f}%][{2}] {3}/{4} | elapsed time {5:.2f}s"
    bar = string.format(eta,
                        progress * 100,
                        "=" * (i_bar - 1) + ">" * (i_lst != lst_len) + " " * (bar_len - i_bar),
                        i_lst,
                        lst_len,
                        elapsed_time)
    sys.stdout.flush()
    sys.stdout.write("\r" + bar)
    sys.stdout.flush()

if __name__ == "__main__":
    lst = range(1000)
    ret = 0
    for elem in ft_progress(lst):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)