import random


def add(values):
    tot = 0
    for num in values:
        if num > 0:
            tot += num
    return tot


def subtract(values):
    negSum = 0
    for num in values:
        if num < 0:
            negSum += num
    return negSum


def multiply(values):
    product = values[0]
    for num in values[1:]:
        if not num == 0:
            product *= num
    return product


def divide(values):
    quo = values[0]
    if values[0] == 0:
        quo = 0
    for num in values[1:]:
        if num == 0:
            raise ZeroDivisionError
        else:
            quo /= num
    return quo


def choose(values):
    return random.choice(values)
