from functions import dictionaryOfChart
from functions.binary import toBinaryNumber, fromBinary


def encodeDictionary():
    output = toBinaryNumber(dictionaryOfChart.BINARY_LENGTH, 8)
    for number in dictionaryOfChart.letters.values():
        output = output + toBinaryNumber(number, dictionaryOfChart.BINARY_LENGTH)
    return output


def decodeDictionary(text):
    counter = 0
    output = []
    for letter in dictionaryOfChart.letters.keys():
        if counter == 0:
            dictionaryOfChart.BINARY_LENGTH = fromBinary(text[0: 8])
            counter = 8
        output.append(fromBinary(text[counter: counter + dictionaryOfChart.BINARY_LENGTH]))
        counter = counter + dictionaryOfChart.BINARY_LENGTH
    return output
