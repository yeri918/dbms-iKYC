import PySimpleGUI as sg

DEFAULT_FONT = 'Lucida'

DEFAULT_WINDOW_SIZE = (720, 530)


def titleText(text="", justify='center', textSize=(100, 1)):
    return sg.Text(text, size=textSize, justification=justify, font=(DEFAULT_FONT, 20))


def subTitleText(text="", justify='left', textSize=(20, 1)):
    return sg.Text(text, size=textSize, justification=justify, font=(DEFAULT_FONT, 15))


def comboElement(listOfItems, comboKey):
    return sg.Combo(listOfItems, size=(20, 1), key=comboKey, font=(DEFAULT_FONT, 13))


def buttonElement(text, buttonKey):
    return sg.Button(text, font=(DEFAULT_FONT, 12), key=buttonKey)
