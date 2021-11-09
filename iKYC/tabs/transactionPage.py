from DEFINE import *
import PySimpleGUI as sg
from datetime import datetime


def getAccountList():
    # get the account info from db
    accounts = {1: {'Title': 'Savings', 'amount': 1235, 'currency': 'HKD'}}
    frame_layout = []
    for account in accounts:
        print(accounts[account])
        accountInfo = []
        accountInfo.append(titleText(accounts[account]['Title']))
        for info in accounts[account]:
            print(info)
            if info != 'Title':
                accountInfo.append(subTitleText(accounts[account][info]))
        print(accountInfo)
        frame_layout.append(accountInfo)

    frame = sg.Frame('Accounts', frame_layout)
    return frame


def getAccountList():
    account = ['All', 'Account 1', 'Account 2']
    return account


def getSearchFrame():
    search = [
        [subTitleText('Select Account Type: ', textSize=(15, 1)), comboElement(
            getAccountList(), '-account-')],
        [sg.Text('_'*50)],
        [subTitleText('Indicate the range of Amount (HKD):',
                      textSize=(25, 1))],
        [subTitleText('From:', textSize=(5, 1)), inputText(
            "-fromAmount-", default=0), subTitleText('To:', textSize=(3, 1)), inputText('-toAmount-', default="MAX")]]
    return search


def getSearchTimeFrame():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string)
    time = [[subTitleText('Indicate the range of time frame: ', textSize=(30, 1))],
            [sg.Text("*Please type in 'dd/mm/yyyy HH/MM/SS' format*", size=(42, 1),
                     font=(DEFAULT_FONT, 10), justification='c')],
            [subTitleText('From:', justify='left', textSize=(5, 1)),
            inputText('-fromDate-', default=dt_string[0:10]), inputText('-fromTime-', "00:00:00")],
            [subTitleText('To:', justify='left', textSize=(5, 1)),
            inputText('-toDate-', default=dt_string[0:10]), inputText('-toTime-', default=dt_string[10::])]]
    return time


def getTableValues():
    values = [("Withdrawal", "A123", "10/12/2021 08:20:11", "500HKD", "500HKD withdrawal"),
              ("Deposit", "A123", "10/12/2021 08:20:11", "500HKD", "500HKD deposit"),
              ("Deposit", "A124", "10/13/2021 09:21:12", "100HKD", "100HKD deposit"),
              ("Transfer", "A124", "10/13/2021 20:12:20", "120HKD", "120HKD transfer")]
    return values


def getTransactionLayout():
    searchFrame = [sg.Frame('FILTER', [[sg.Frame('', getSearchFrame()), sg.Frame('', getSearchTimeFrame())],
                                       [buttonElement("Search", "-search-", (100, 1))]])]

    table = sg.Table(values=getTableValues(),
                     headings=["Type", "Account No.",
                               "Time", "Amount", "Description"],
                     auto_size_columns=False,
                     col_widths=(9, 9, 17, 8, 25),
                     justification='left', key='-transactionTable-', size=(1000, 300), font=(DEFAULT_FONT, 15))

    frame = [searchFrame,
             [titleText("Transactions")], [table]]

    transactionsTab = [[sg.Column(frame)]]
    return transactionsTab
