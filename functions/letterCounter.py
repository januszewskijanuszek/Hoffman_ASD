from functions.dictionaryOfChart import letters
from functions.dictionaryOfChart import letters as dictionary


# Returns dictionary of counted letters
def countLetters(text):
    for letter in text:
        try:
            dictionary[letter] = dictionary[letter] + 1
        except:
            raise TypeError("There is no letter ", letter, " in dictionary")

def importLetterCount(array):
    counter = 0
    for letter in dictionary.keys():
        dictionary[letter] = array[counter]
        counter = counter + 1
    return dictionary