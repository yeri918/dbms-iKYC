from DEFINE import *
import PySimpleGUI as sg


def getAccountList():
    return ['Account 1', 'Account 2']


def getTransferFrame():
    layout = [[titleText('Transfer', textSize=(30, 1))],
              [sg.HorizontalSeparator()],
              [sg.Frame('', [[titleText('From', justify='left', textSize=(30, 1))],
                             [subTitleText("*Select account*",
                                           justify='left')],
                             [comboElement(getAccountList(), '-accountTransfer-', comboSize=(35, 1), fontSize=17)]], size=(390, 90))],
              [sg.Frame('', [[titleText('To', justify='left', textSize=(30, 1))],
                             [subTitleText(
                                 "*Please enter the payee's account number*", justify='left', textSize=(35, 1))],
                             [inputText('-transferTo-', textSize=(45, 1))]])],
              [sg.Frame('', [[titleText('Amount', textSize=(30, 1), justify='left')],
                             [subTitleText(
                                 "*Please enter amount*", justify='left')],
                             [inputText('-amountTransfer-', textSize=(30, 1)),
                              comboElement(['HKD', 'USD'], '-currencyTransfer-')]])],
              [sg.Frame('', [[titleText('Remarks(optional)', justify='left', textSize=(30, 1))],
                             [subTitleText('*Add remarks*', justify='left')],
                             [inputText('-remarksTransfer-', textSize=(45, 1))]])],
              [buttonElement('Transfer', '-transferButton-', buttonSize=(50, 1))]]
    return layout


def getPayee(name, account):
    frame = sg.Frame('', [[subTitleText(name, justify='left')],
                          [subTitleText(account, justify='right', textSize=(30, 1))]], size=(280, 60))
    return frame


def getRecentPayees():
    layout = [[titleText('Recent Payees', textSize=(30, 1))],
              [sg.HorizontalSeparator()],
              [getPayee('Julie Park', '123456789')],
              [getPayee('Anishka Bhargava', '123456789')],
              [getPayee('Pranay Periwal', '123456789')],
              [getPayee('Ayoung Kwon', '123456789')],
              [getPayee('Sukmin Kim', '123456789')]
              ]
    return layout


def getTransferLayout():
    layout = [[sg.Frame('', getTransferFrame(), size=(400, 500)),
               sg.Frame('', getRecentPayees(), size=(300, 500))]]
    return layout
