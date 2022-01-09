from functions.binary import toBinaryChart, fromBinary, toBinaryNumber
from functions import letterCounter
from functions.dictionaryOfChart import letters as dictionary
from functions.compiler import dictionaryCompiler as testOfCompiler, dictionaryCompiler
from functions.compiler import textCompiler
from functions.compiler import binConverter
import textGenerator

data = ""
with open("inputEncode.bin", "rb") as myFile:
    data = myFile.readlines()

data1 = ""
with open("inputDecode.txt", "r") as myFile:
    data1 = myFile.readlines()

if __name__ == '__main__':
    # textCompiler.textEncoder(data1[0])
    textCompiler.textDecoder(data)
    # print(binConverter.readBytes("inputEncode.bin"))
