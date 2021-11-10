from typing import Sized
from DEFINE import *
import PySimpleGUI as sg
from datetime import datetime


def getSearchFrame():
    search = [[subTitleText('Select Account Type: ', textSize=(20, 1)), comboElement(
            ["All Accounts",'Current Account', 'Savings Account'], '-account-')]]
    return search

def currentgetinfo():
    yes = [[subTitleText('Account Number: ', justify='left')],
           [subTitleText('Currency: HKD', justify='left')],
           [subTitleText('Account Balance: HKD', justify='right')],
           [subTitleText('Credit Limit: HKD', justify='right')],
           [subTitleText('Credit Remaining: HKD', justify='right')],
           ]

    return yes

def savinggetinfo():
    yes = [[subTitleText('Account Number: ', justify='left')],
           [subTitleText('Currency: HKD', justify='left')],
           [subTitleText('Account Balance: HKD', justify='right')],
           [subTitleText('Credit Limit: HKD', justify='right')],
           [subTitleText('Credit Remaining: HKD', justify='right')],
           ]

    return yes

def accountsFrame():
    test1 = [[titleText('Account 1'), subTitleText('subtext')]]
    searchFrame = [sg.Frame('FILTER', [[sg.Frame('', getSearchFrame())],
                                       [buttonElement("Search", "-search-", (100, 1))]])]
    frame = [searchFrame,
             [titleText("Accounts", justify='center', textColor='pink')],
             [sg.Frame('Current Account', currentgetinfo(),size=(700,180))],
             [sg.Frame('Savings Account', savinggetinfo(),size=(700,180))],
             ]

    transactionsTab = [[sg.Column(frame)]]
    return transactionsTab

