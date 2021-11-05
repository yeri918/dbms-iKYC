import PySimpleGUI as sg

DEFAULT_FONT = 'Lucida'

DEFAULT_WINDOW_SIZE = (720, 530)


def titleText(text="", justify='center', textSize=(100, 1)):
    return sg.Text(text, size=textSize, justification=justify, font='Helvetica 20')


def subTitleText(text="", justify='left', textSize=(20, 1)):
    return sg.Text(text, size=textSize, justification=justify, font='Helvetica 20')
