"""Homework 2."""
"""
C88C Spring 2024:

Please credit any folks in C88C that you collaborated with,
and any online sources you searched for.
Remember, it's OK to ask for help, and to search for topics, but
you may not search for specific solutions or copy any code directly.

List Collaborators:

Credit Any Online Sources (google searches, etc):


"""


def fib(n):
    """Returns the nth Fibonacci number.

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(100)
    354224848179261915075
    """
    "*** YOUR CODE HERE ***"


def total_cost(shopping_cart):
    """ Returns a float that is the total cost of all items in the shopping cart.
    >>> fruit_cart = [("apple", 0.5, 3), ("banana", 0.25, 4)]
    >>> total_cost(fruit_cart)
    2.5
    >>> cal_cart = [("oski", 1000, 1), ("go", 1.25, 2), ("bears", 3.5, 2)]
    >>> total_cost(cal_cart)
    1009.5
    """
    "*** YOUR CODE HERE ***"
    

def tax(shopping_cart, percent):
    """ Returns a new list where a `percent` tax is added to each item's price in a shopping cart.
    >>> fruit_cart = [("apple", 0.5, 3), ("banana", 0.25, 4)]
    >>> tax(fruit_cart, 10)
    [('apple', 0.55, 3), ('banana', 0.275, 4)]
    >>> cal_cart = [("oski", 1000, 1), ("go", 1.25, 2), ("bears", 3.5, 2)]
    >>> tax(cal_cart, 100)
    [('oski', 2000.0, 1), ('go', 2.5, 2), ('bears', 7.0, 2)]
    """
    "*** YOUR CODE HERE ***"
    


def deck(suits, numbers):
    """Creates a deck of cards (a list of 2-element lists) with the given
    suits and numbers. Each element in the returned list should be of the form
    [suit, number].

    >>> deck(['S', 'C'], [1, 2, 3])
    [['S', 1], ['S', 2], ['S', 3], ['C', 1], ['C', 2], ['C', 3]]
    >>> deck(['S', 'C'], [3, 2, 1])
    [['S', 3], ['S', 2], ['S', 1], ['C', 3], ['C', 2], ['C', 1]]
    >>> deck([], [3, 2, 1])
    []
    >>> deck(['S', 'C'], [])
    []
    """
    "*** YOUR CODE HERE ***"
    


def arange(start, end, step=1):
    """
    arange behaves just like np.arange(start, end, step).
    You only need to support positive values for step.

    >>> arange(1, 3)
    [1, 2]
    >>> arange(0, 25, 2)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
    >>> arange(999, 1231, 34)
    [999, 1033, 1067, 1101, 1135, 1169, 1203]

    """
    "*** YOUR CODE HERE ***"
    


def reverse_iter_for(lst):
    """Returns the reverse of the given list.

    >>> reverse_iter_for([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"

def reverse_iter_while(lst):
    """Returns the reverse of the given list.

    >>> reverse_iter_while([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    rev_lst = []
    i = 0
    while i < len(lst):
        "*** YOUR CODE HERE ***"

