import random


def add(values: [float]) -> float:
    """
    Adds all positive numbers in values
    :param values: [float]
    return: float
    """
    tot = 0
    for num in values:
        if num > 0:
            tot += num
    return tot


def subtract(values: [float]) -> float:
    """
    Sums up all negative numbers in values
    :param values: [float]
    :return: float
    """
    negSum = 0
    for num in values:
        if num < 0:
            negSum += num
    return negSum


def multiply(values: [float]) -> float:
    """
    Multiplies all non-zero numbers in values
    :param values: [float]
    :return: float
    """
    product = values[0]
    for num in values[1:]:
        if not num == 0:
            product *= num
    return product


def divide(values: [float]) -> float:
    """
    Divides the numbers in values in order
    :param values: [float]
    :return: float
    """
    quo = values[0]
    if values[0] == 0:
        quo = 0
    for num in values[1:]:
        if num == 0:
            raise ZeroDivisionError
        else:
            quo /= num
    return quo


def choose(values: [float]) -> float:
    """
    Chooses a random number in values
    :param values: [float]
    :return: float
    """
    return random.choice(values)
