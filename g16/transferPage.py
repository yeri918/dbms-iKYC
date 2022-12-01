from DEFINE import *
import PySimpleGUI as sg
import database as db
from forex_python.converter import CurrencyRates


def getAccountList(conn, userID):
    accountList = db.getAllAccountNumberOfCustomer(conn, userID)
    account = []
    for i in accountList:
        account.append(i['account_type']+" "+i['account_number'])
    return account


def getTransferFrame(conn, userID):
    layout = [[titleText('Transfer', textSize=(30, 1))],
              [sg.HorizontalSeparator()],
              [sg.Frame('', [[titleText('From', justify='left', textSize=(30, 1))],
                             [subTitleText("*Select account*",
                                           justify='left')],
                             [comboElement(getAccountList(conn, userID), '-accountTransfer-', comboSize=(35, 1), fontSize=17)]], size=(390, 90))],
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


def getRecentPayees(conn, userID):
    payees = db.getRecentPayee(conn, userID)
    layout = [[titleText('Recent Payees', textSize=(30, 1))],
              [sg.HorizontalSeparator()]]
    for i in payees:
        name = i['first_name']+' '+i['last_name']
        layout.append([getPayee(name, i['to_account'])])

    return layout


def getTransferLayout(conn, userID):
    layout = [[sg.Frame('', getTransferFrame(conn, userID), size=(400, 500)),
               sg.Frame('', getRecentPayees(conn, userID), size=(300, 500))]]
    return layout


def convertToHKD(value, currency):
    # print(value, currency)
    c = CurrencyRates()
    rate = c.get_rate(currency, 'HKD')
    # print(rate)
    return int(value)*rate
