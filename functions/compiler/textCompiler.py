from functions import letterCounter
from functions.compiler.dictionaryCompiler import encodeDictionary
from functions.dictionaryOfChart import letters as dictionary
from functions import dictionaryOfChart
from functions.compiler import binConverter
from functions import binary
from functions.compiler import dictionaryCompiler
from functions import letterCounter
import settings
import math

mainArray = []

def glueData(data):
    output = ""
    for set in data:
        for number in set:
            output += str(binary.toBinaryNumber(number, 8))
    return output

def numberAssigner():
    for letter in dictionary.keys():
        mainArray.append([dictionary[letter], letter])
    if settings.SHOW_FIRST_MAIN_ARRAY:
        print("First mainArray -> ", mainArray)
    mainArray.sort(reverse=True)
    if settings.SHOW_SORTED_MAIN_ARRAY:
        print("Sorted mainArray -> ", mainArray)
    binaryNumber = 1
    dictionaryOfChart.BINARY_LENGTH = 0
    while mainArray[0][0] > binaryNumber:
        dictionaryOfChart.BINARY_LENGTH = dictionaryOfChart.BINARY_LENGTH + 1
        binaryNumber = binaryNumber * 2
    if settings.SHOW_FIRST_BINARY_GENERATOR:
        print("MAX -> ", mainArray[0][0])
        print("BIN -> ", dictionaryOfChart.BINARY_LENGTH, " -> ", binary.toBinaryNumber(dictionaryOfChart.BINARY_LENGTH, 8))


def treeGenerator():
    numberAssigner()
    counter = 0
    left = 0
    for number, letter in mainArray:
        if counter % 2 == 0:
            left = left + 1
            binary = "1"
            for x in range(left - 1):
                binary = binary + "1"
            binary = binary + "0"
            mainArray[counter][0] = binary
        else:
            binary = "0"
            for x in range(left - 1):
                binary = binary + "1"
            binary = binary + "0"
            mainArray[counter][0] = binary
        counter = counter + 1
    if settings.SHOW_CODED_ARRAY:
        print(mainArray)


def textEncoder(text):
    print("-" * 5, "Encoding", "-" * 5)
    letterCounter.countLetters(text)
    if settings.SHOW_LENGTH_OF_DICTIONARY:
        print("Length of dict -> ", len(dictionaryOfChart.letters))
    treeGenerator()
    output = ""
    counter = 0
    leng = len(text)
    last = 0
    for letter in text:
        for particle in mainArray:
            if particle[1] == letter:
                output = output + particle[0]
                break
        if settings.SHOW_LOADING:
            if math.floor(last) < math.floor((counter / leng) * 100):
                last = math.floor((counter / leng) * 100)
                print(last, "%")
            counter = counter + 1
    exe = encodeDictionary() + output
    binConverter.saveBytes("inputEncode.bin", binConverter.sliceInput(exe))
    if settings.SHOW_BINARY_OUTPUT:
        print(exe)

def textDecoder(data):
    print("-"*5, "Decoding", "-"*5)
    binary = glueData(data)
    letterCounter.importLetterCount(dictionaryCompiler.decodeDictionary(binary))
    treeGenerator()
    counter = dictionaryOfChart.BINARY_LENGTH * len(dictionaryOfChart.letters) + 8
    print(counter)
    print("-"*8)
    temp = ""
    output = ""
    for bit in range(counter, len(binary)):
        temp += binary[bit]
        for value, character in mainArray:
            if value == temp:
                temp = ""
                output += character
    print(output)