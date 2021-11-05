from tkinter import *
from typing import ClassVar
from tkcalendar import *

root = Tk()
root.title('Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry('600x400')

cal = Calendar(root, selectmode="day")
