def fib(n):
    """
    >>> fib(5)
    5
    """
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# if n < 2:
#     return n
# else:
#     return fib(n - 1) + fib(n - 2)


def iter_fib(n):
    """
    >>> iter_fib(5)
    5
    """
    (n_1, n_2) = (0, 1)
    for i in range(0, n):
        # This computes n_1+n_2 before updating n_1
        (n_1, n_2) = (n_2, n_1 + n_2)
    return n_1

def count_change(value, coins):
    """Returns the number of ways to make change for amount.

    >>> denominations = [50, 25, 10, 5, 1]
    >>> count_change(7, denominations)
    2
    >>> count_change(100, denominations)
    292
    >>> denominations = [16, 8, 4, 2, 1]
    >>> count_change(7, denominations)
    6
    >>> count_change(10, denominations)
    14
    >>> count_change(20, denominations)
    60
    """
    if value < 0 or len(coins) == 0:
        return 0
    elif value == 0:
        return 1
    using_coin = count_change(value - coins[0], coins)
    not_using_coin = count_change(value, coins[1:])
    return using_coin + not_using_coin

### Pascal's Triangle
def generate_pascal_triangle(n):
    if n == 1:
        return [[1]]
    else:
        prev_triangle = generate_pascal_triangle(n - 1)
        last_row = prev_triangle[-1]
        new_row = [1]

        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])

        new_row.append(1)
        prev_triangle.append(new_row)

        return prev_triangle

# ############## OPTIONAL CONTENT BELOW THIS LINE ###########

import random

def random_list():
    return random.sample(range(0, 101), 20)

def split(x, s):
    return [i for i in s if i <= x], [i for i in s if i > x]

def quicksort(lst):
    """
    Sort a sequence - split it by the first element,
    sort both parts and put them back together.
    """
    if not lst:
        return []
    else:
        pivot = lst[0]
        smaller, bigger = split(pivot, lst[1:])
        return quicksort(smaller) + [pivot] + quicksort(bigger)


######### Example that's barely functional,
### but conveys the idea of trees.
### ignore all the stuff about dealing with filepaths...

import os
def is_file(directory, file_name):
    return os.path.isfile(os.path.join(directory, file_name))

def walk_directory(directory, indent=''):
    """
    This function just prints ALL files and folders, and goes through all subfolders.
    e.g. walk_directory('/Users/Michael/Desktop')
    """
    all_items = os.listdir(directory)
    for item in all_items:
        if is_file(directory,item):
            print(f'{indent}FILE: {item}')
        else:
            print(f'{indent}DIRECTORY: {item}')
            walk_directory(os.path.join(directory, item), indent + '\t')
