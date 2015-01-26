choices = ['sin(x*2)', 'cos(10*x)', 'pi', 'tan(30*x)', 'sin(30*y)',
           'cos(10*y)', 'tan(2*y)', '2', 'x', 'y', '10']

import random
from math import sin, cos, pi


# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def msin(x):
    return sin(x)


def mcos(x):
    return cos(x)


def mpi():
    return pi


def mtan(x):
    return sin(x)/cos(x)


def avg(x, y):
    return (x + y) / 2


def create_expression():
    expr = 'sin(x)'
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""

    for _ in range(30):
        expr = expr + ' * ' + random.choice(choices)
    return expr


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    expr = expr.replace("sin", "msin")
    expr = expr.replace("cos", "mcos")
    expr = expr.replace("pi", "mpi()")
    expr = expr.replace("tan", "mtan")
    expr = expr.replace("x", str(abs(x)))
    expr = expr.replace("y", str(abs(y)))
    return eval(expr)
