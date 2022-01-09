import math


def toBinaryChart(chart):
    number = ord(chart)
    binary = ""
    if number == 32:
        return "000000"
    if number == 46:
        return "111111"
    if number == 44:
        return "111110"
    while number != 1:
        if number % 2 == 0:
            binary = binary + "0"
        else:
            binary = binary + "1"
        number = math.floor(number / 2)
    return binary[::-1]


def fromBinary(binary):
    counter = len(binary) - 1
    number = 0
    for char in binary:
        if char == '1':
            number = number + pow(2, counter)
        counter = counter - 1
    return number


def toBinaryNumber(number, value):
    binary = ""
    if number == 0:
        output = ""
        for x in range(value):
            output = output + "0"
        return output
    while number != 0:
        if number % 2 == 0:
            binary = binary + "0"
        else:
            binary = binary + "1"
        number = math.floor(number / 2)
    if len(binary) < value:
        exe = value - len(binary)
        for x in range(exe):
            binary = binary + "0"
    return binary[::-1]
