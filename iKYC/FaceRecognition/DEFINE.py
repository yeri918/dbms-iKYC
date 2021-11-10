import PySimpleGUI as sg

DEFAULT_FONT = 'Lucida'

DEFAULT_WINDOW_SIZE = (720, 530)


def titleText(text="", justify='center', textSize=(100, 1), textColor='white'):
    return sg.Text(text, size=textSize, justification=justify, font=(DEFAULT_FONT, 20), text_color=textColor)


def subTitleText(text="", justify='center', textSize=(20, 1)):
    return sg.Text(text, size=textSize, justification=justify, font=(DEFAULT_FONT, 15))


def subText(text="", justify='left', textSize=(30, 1)):
    return sg.Text(text, size=textSize, justification=justify, font=(DEFAULT_FONT, 13))


def comboElement(listOfItems, comboKey, comboSize=(10, 1), fontSize=13):
    return sg.Combo(listOfItems, size=comboSize, key=comboKey, font=(DEFAULT_FONT, fontSize), default_value=listOfItems[0])


def buttonElement(text, buttonKey, buttonSize=(10, 1)):
    return sg.Button(text, font=(DEFAULT_FONT, 12), key=buttonKey, size=buttonSize)


def inputText(inputKey, default="", textSize=(10, 1)):
    return sg.InputText(key=inputKey, size=textSize, default_text=default, font=(DEFAULT_FONT, 13))