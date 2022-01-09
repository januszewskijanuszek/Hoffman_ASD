from functions import binary


def sliceInput(text):
    bit = []
    counter = 0
    length = len(text)
    while length % 8 != 0:
        length = length + 1
        text = text + "0"
    for x in range(int(length / 8)):
        temp = text[counter: counter + 8]
        counter = counter + 8
        bit.append(binary.fromBinary(temp))
    return bit


def saveBytes(filename, byt):
    with open(filename, "wb") as file:
        for b in byt:
            file.write(b.to_bytes(1, byteorder="big"))


def readBytes(filename):
    byt = []
    with open(filename, "rb") as file:
        while True:
            b = file.read(1)
            if not b:
                break
            byt.append(int.from_bytes(b, byteorder="big"))
    return byt

