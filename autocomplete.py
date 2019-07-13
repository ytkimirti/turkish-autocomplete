#!/usr/bin/env python3

from pynput.keyboard import Key, Listener, Controller
import copy

print("Autocomplete started and ready...")

# PREFERENCES
minCharCount = 3
wordsFileName = 'words.txt'

# Other vars
currInput = ''

keyboard = Controller()

trChars = ['ç', 'ı', 'ö', 'ş', 'ü', 'ğ']


def hasTrChar(word):
    for c in word:
        if(c in trChars):
            return True
    return False


def trans_char_eng(char):
    chars = {
        'ç': 'c',
        'ı': 'i',
        'ö': 'o',
        'ş': 's',
        'ü': 'u',
        'ğ': 'g',
    }

    return chars.get(char, char)


def trans_word_eng(word):
    newStr = ''
    for c in word:
        newStr = newStr + trans_char_eng(c)
    return newStr

# Special characters


def makeI():
    keyboard.press(Key.shift)
    keyboard.press(Key.alt)

    keyboard.press('b')

    keyboard.release(Key.shift)
    keyboard.release(Key.alt)


def makeC():
    keyboard.press(Key.alt)

    keyboard.press('c')

    keyboard.release(Key.alt)


def makeO():
    keyboard.press(Key.alt)

    keyboard.press('u')

    keyboard.release(Key.alt)

    keyboard.press('o')


def makeU():
    keyboard.press(Key.alt)

    keyboard.press('u')

    keyboard.release(Key.alt)

    keyboard.press('u')


def emptyFunction():
    return


def makeSpecialCharacter(char):
    functions = {
        'ç': makeC,
        'ü': makeU,
        'ö': makeO,
        'ı': makeI,
    }

    functions.get(char, emptyFunction)()


f = open(wordsFileName, 'r')

words = f.readlines()

words = [x.strip() for x in words]

wordsDict = dict()

for word in words:
    wordsDict[trans_word_eng(word)] = word

f.close()


def on_word(word):
    correctedWord = wordsDict.get(word, word)

    if(word != correctedWord):
        print('!')
        print(correctedWord)
        correctWord(correctedWord)

    # TODO: Somehow correct it by erasing the wrong version


def correctWord(word):
    for i in range(len(word) + 1):
        keyboard.press(Key.backspace)

    typeWord(word + ' ')


def typeWord(word):
    for c in word:
        if(c in trChars):
            makeSpecialCharacter(c)
        else:
            keyboard.type(c)


def on_press(key):
    keyStr = str(format(key)).replace("'", '')

    global currInput

    if(len(keyStr) == 1):
        currInput = currInput + keyStr
    elif(keyStr == 'Key.space' and len(keyStr) > minCharCount):
        on_word(currInput)
        currInput = ''
    elif(keyStr == 'Key.backspace' and len(currInput) != 0):
        currInput = currInput[:-1]


def on_release(key):
    #print('Key {} released.'.format(key))
    if str(key) == 'Key.esc':
        print('Exiting...')
        return False


with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
