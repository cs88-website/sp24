"""Homework 6"""
"""
C88C Spring 2024:

Please credit any folks in C88C that you collaborated with,
and any online sources you searched for.
Remember, it's OK to ask for help, and to search for topics, but
you may not search for specific solutions or copy any code directly.

List Collaborators:

Credit Any Online Sources (google searches, etc):


"""


# Probably a die-re situation

def count_digit(n, digit):
    """Return how many times digit appears in n.

    >>> count_digit(55055, 5)
    4
    >>> count_digit(1231421, 1)
    3
    >>> count_digit(12, 3)
    0
    """
    if n == 0:
        return 0
    if n % 10 == digit:
        return count_digit(n // 10, digit) + 1
    else:
        return count_digit(n // 10, digit)


from operator import add, mul

def reduce(reducer, seq, start):
    """Reduce a sequence under a two-argument function starting from a start value.

    >>> def add(x, y):
    ...     return x + y
    >>> def mul(x, y):
    ...     return x*y
    >>> reduce(add, [1,2,3,4], 0)
    10
    >>> reduce(mul, [1,2,3,4], 0)
    0
    >>> reduce(mul, [1,2,3,4], 1)
    24
    """
    if seq == []:
        return start
    next_base = reducer(start, seq[0])
    return reduce(reducer, seq[1:], next_base)


def remove_last(x, lst):
    """Create a new list that is identical to lst but with the last
    element from the list that is equal to x removed.

    >>> remove_last(1,[])
    []
    >>> remove_last(1,[1])
    []
    >>> remove_last(1,[1,1])
    [1]
    >>> remove_last(1,[2,1])
    [2]
    >>> remove_last(1,[3,1,2])
    [3, 2]
    >>> remove_last(1,[3,1,2,1])
    [3, 1, 2]
    >>> remove_last(5, [3, 5, 2, 5, 11])
    [3, 5, 2, 11]
    """
    if not lst:
        return []
    elif lst[-1] == x:
        return lst[0:-1]
    else:
        return remove_last(x, lst[0:-1]) + [lst[-1]]


def map(f, seq):
    """
    Map a function f onto a sequence.

    >>> def double(x):
    ...     return x * 2
    >>> def square(x):
    ...     return x ** 2
    >>> def toLetter(x):
    ...     alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ...     return alpha[x%26]
    >>> map(double, [1,2,3,4])
    [2, 4, 6, 8]
    >>> map(square, [1, 2, 3, 4, 5, 10])
    [1, 4, 9, 16, 25, 100]
    >>> map(toLetter, [3, 0, 19, 0])
    ['d', 'a', 't', 'a']

    """
    if seq == []:
        return seq
    return [f(seq[0])] + map(f, seq[1:])


def hailstone_iterative(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone_iterative(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone_iterative(n // 2)
    else:
        return 1 + hailstone_iterative(3 * n + 1)


def hailstone_recursive(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone_recursive(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone_recursive(n // 2)
    else:
        return 1 + hailstone_recursive(3 * n + 1)


def count_generations(family_tree):
    """
    Count the number of generations in a nested list-based family tree.

    >>> count_generations([("A"), []])
    1
    >>> count_generations([("A"), [[("B"), []], [("C"), []] ] ])
    2
    >>> family_tree = [("Jordan", "Alex"), [
    ...     [("Taylor", "Morgan"), [
    ...         [("Riley", None), []],
    ...         [("Avery", None), []]
    ...     ]]
    ... ]]
    >>> count_generations(family_tree)
    3
    >>> family_tree = [("Jordan", "Alex"), [
    ...     [("Taylor", "Morgan"), [
    ...         [("Riley", "Sam"), [
    ...             [("Avery", None), []]
    ...         ]]
    ...     ]],
    ...     [("Casey", "Jamie"), [
    ...         [("Quinn", "Chris"), [
    ...             [("Dakota", None), []],
    ...             [("Skyler", None), []]
    ...         ]],
    ...         [("Jesse", "Jordan"), []]
    ...         ]]
    ...     ]]
    >>> count_generations(family_tree)
    4
    """
    if not family_tree:
        return 0
    parents = family_tree[0]
    children = family_tree[1]

    max_gen = 0
    # for child in children:
    #     gen = count_generations(child)
    #     if gen > max_gen:
    #         max_gen = gen
    if len(children) > 0:
        max_gen = max([count_generations(child) for child in children])
    return 1 + max_gen

