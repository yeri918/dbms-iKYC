from typing import Sized
from DEFINE import *
import PySimpleGUI as sg
from datetime import datetime


def getSearchFrame():
    l1 = ['Current Account', 'Savings Account']
    search = [[subTitleText('My Account Types: ', textSize=(20, 1), justify='left')],
              # [subTitleText('* Current Account *')],
              # [subTitleText('* Savings Account *')],
              [sg.Listbox(l1, font=('Lucida', 14), size=(70, 20))]
              ]

    return search


def currentgetinfo(accNum, overdraft, balance, status):
    layout1 = [[subTitleText2("")],
               [subTitleText2('Account Number: ' + accNum,
                              justify='left', textSize=(50, 1))],
               [subTitleText2('Currency: HKD', justify='left')],
               [subTitleText2('Overdraft Fee: ' +
                              str(overdraft), justify='left')],
               [subTitleText2('Account Balance: HKD'+str(balance),
                              justify='right', textSize=(50, 1))],
               [subTitleText2('Account Status: '+status,
                              justify='right', textSize=(50, 1))],
               [subTitleText2("")],
               [buttonElement2("View Transactions",
                               '-transactionPageDetails-', buttonSize=(50, 1))]
               #    [sg.Text("More Details", font=("Lucida", 13, "underline"), justification='left', text_color="white", enable_events=True,
               #             key="-transcationPageDetails-")]
               ]

    return layout1


def savinggetinfo(accNum, intRate, balance, status):
    layout1 = [[subTitleText2("")],
               [subTitleText2('Account Number: '+accNum,
                              justify='left', textSize=(50, 1))],
               [subTitleText2('Currency: HKD', justify='left')],
               [subTitleText2('Interest Rate: '+str(intRate) +
                              "%", justify='left')],
               [subTitleText2('Account Balance: HKD'+str(balance),
                              justify='right', textSize=(50, 1))],
               [subTitleText2('Account Status: '+status,
                              justify='right', textSize=(50, 1))],
               [subTitleText2("")],
               [buttonElement2("View Transactions",
                               '-transactionPageDetails1-', buttonSize=(50, 1))]

               ]

    return layout1


def accountsFrame(savingAccNum, currentAccNum, overdraft, intRate, savingBalance, currentBalance, status):
    test1 = [[titleText('Account 1'), subTitleText('subtext')]]
    searchFrame = [
        sg.Frame('Accounts', getSearchFrame(), font=("Lucida", 18), size=(650, 120))]
    layout_column = [[sg.Button('Sign Out', font=("Lucida", 10), size=(5, 2))]
                     ]
    # [sg.Column(layout_column, element_justification='right', expand_x=True)],
    frame = [searchFrame,
             [titleText("Accounts", justify='center', textColor='Orange')],
             [sg.Frame('Current Account', currentgetinfo(currentAccNum, overdraft, currentBalance, status), font=("Lucida", 20), size=(340, 400)), sg.Frame(
                 'Savings Account', savinggetinfo(savingAccNum, intRate, savingBalance, status), font=("Lucida", 20), size=(340, 400))],
             ]

    accTab = [[sg.Column(frame)]]
    return accTab
