import time
import timeit
import sys


def ft_progress(lst: list) -> None:
    """In this function :
    - The starting time of the program is obtained thanks to timeit package.
    - The length of the progress bar is set.
    - The for loop iterates in lst from 0 to len(lst).
    - i_bar is incremented if lst_progress reaches a value that corresponds to
      a 1% increment (in progress bar referential).
    - The print_bar function is called.
    """
    start_time = timeit.default_timer()
    bar_len = 100
    lst_len = len(lst)
    i_bar = 0
    for i_lst in lst:
        yield i_lst
        lst_progress = i_lst / lst_len
        bar_progress = i_bar / bar_len
        if (lst_progress >= bar_progress + (1 / bar_len)):
            i_bar += 1
        print_bar(i_bar + 1, i_lst + 1, bar_len, lst_len, start_time)


def print_bar(i_bar, i_lst, bar_len, lst_len, start_time) -> None:
    """In this function :
    - The time elapsed since the program started is obtained.
    - The progession is calculated (in progress bar referential).
    - The Estimated Time of Arrival (ETA) is calculated by multiplying :
        ~ (elapsed_time / progress) : time required for current progress
        and
        ~ (1 - progress) : progress still to be made
    """
    elapsed_time = timeit.default_timer() - start_time
    progress = i_bar / bar_len
    eta = elapsed_time / progress * (1 - progress)
    string = "ETA : {0:.2f}s [{1: >2.0f}%][{2}] {3}/{4} | elapsed time {5:.2f}s"
    bar = string.format(eta,
                        progress * 100,
                        "=" * (i_bar - 1) + ">" * (i_lst != lst_len) + " " * (bar_len - i_bar),
                        i_lst,
                        lst_len,
                        elapsed_time)
    sys.stdout.write("\r" + bar)
    sys.stdout.flush()


if __name__ == "__main__":
    lst = range(1000)
    ret = 0
    for elem in ft_progress(lst):
        ret += 1
        time.sleep(0.005)
    print()
    print(ret)
