from typing import Sized
from DEFINE import *
import PySimpleGUI as sg
from datetime import datetime


def getSearchFrame():
    search = [[subTitleText('Select Account Type: ', textSize=(20, 1)), comboElement(
        ["All Accounts", 'Current Account', 'Savings Account'], '-account1-')]]
    return search


def currentgetinfo():
    layout1 = [[subTitleText('Account Number: ', justify='left')],
               [subTitleText('Currency: HKD', justify='left')],
               [subTitleText('Overdraft: ', justify='left')],
               [subTitleText('Account Balance: HKD', justify='right')],
               [subTitleText('Account Status: ', justify='right')],
               [sg.Text("More Details", font=("Lucida", 13, "underline"), justification='left', text_color="white", enable_events=True,
                        key="-transcationPageDetails-")]
               ]

    return layout1


def savinggetinfo():
    layout1 = [[subTitleText('Account Number: ', justify='left')],
               [subTitleText('Currency: HKD', justify='left')],
               [subTitleText('Interest Rate: ', justify='left')],
               [subTitleText('Account Balance: HKD', justify='right')],
               [subTitleText('Account Status: ', justify='right')],

               [sg.Text("More Details", font=("Lucida", 13, "underline"), justification='left', text_color="white",
                        enable_events=True,
                        key="-transcationPageDetails1-")]
               ]

    return layout1


def accountsFrame():
    test1 = [[titleText('Account 1'), subTitleText('subtext')]]
    searchFrame = [sg.Frame('FILTER', [[sg.Frame('', getSearchFrame())],
                                       [buttonElement("Search", "-search1-", (100, 1))]], font=("Lucida", 18))]
    frame = [searchFrame,
             [titleText("Accounts", justify='center', textColor='Grey')],
             [sg.Frame('CURRENT ACCOUNT', currentgetinfo(), font=("Lucida", 18), size=(340, 400)), sg.Frame(
                 'SAVINGS ACCOUNT', savinggetinfo(), font=("Lucida", 18), size=(340, 400))],
             ]

    transactionsTab = [[sg.Column(frame)]]
    return transactionsTab
