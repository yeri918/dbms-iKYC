from DEFINE import *
import PySimpleGUI as sg
from datetime import datetime
import database as db


# def getAccountList():
#     # get the account info from db
#     accounts = {1: {'Title': 'Savings', 'amount': 1235, 'currency': 'HKD'}}
#     frame_layout = []
#     for account in accounts:
#         # print(accounts[account])
#         accountInfo = []
#         accountInfo.append(titleText(accounts[account]['Title']))
#         for info in accounts[account]:
#             print(info)
#             if info != 'Title':
#                 accountInfo.append(subTitleText(accounts[account][info]))
#         print(accountInfo)
#         frame_layout.append(accountInfo)

#     frame = sg.Frame('Accounts', frame_layout)
#     return frame


def getAccountList(conn, userID):
    accountList = db.getCustomerAccountList(conn, userID)
    account = ['All']
    for i in accountList:
        account.append(i['account_type'])
    return account


def getSearchFrame(conn, userID):
    maxAmount = db.getmaxtransaction(conn, userID)
    search = [
        [subTitleText('Select Account Type: ', textSize=(15, 1)), comboElement(
            getAccountList(conn, userID), '-account-')],
        [sg.Text('_'*50)],
        [subTitleText('Indicate the range of Amount (HKD):',
                      textSize=(25, 1))],
        [subTitleText('From:', textSize=(5, 1)), inputText(
            "-fromAmount-", default=0), subTitleText('To:', textSize=(3, 1)), inputText('-toAmount-', default=maxAmount)]]
    return search


def getSearchTimeFrame():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print(dt_string)
    time = [[subTitleText('Indicate the range of time frame: ', textSize=(30, 1))],
            [sg.Text("*Please type in 'dd/mm/yyyy HH/MM/SS' format*", size=(42, 1),
                     font=(DEFAULT_FONT, 10), justification='c')],
            [subTitleText('From:', justify='left', textSize=(5, 1)),
            inputText('-fromDate-', default=dt_string[0:10]), inputText('-fromTime-', "00:00:00")],
            [subTitleText('To:', justify='left', textSize=(5, 1)),
            inputText('-toDate-', default=dt_string[0:10]), inputText('-toTime-', default=dt_string[10::])]]
    return time


def getTableValues(transactions):
    # transaction = db.getTransactionHistory(conn, customer_id)
    values = []
    for i in transactions:
        date_time = i['transaction_time'].strftime("%m/%d/%Y %H:%M:%S")
        temp = (i['transaction_type'], i['account_number'], date_time,
                str(i['transaction_amount'])+"HKD", i['transaction_description'])
        values.append(temp)
    return values


def getTransactionLayout(conn, userID, transactionsList):
    # print("\n")
    # print(transactionsList)
    # print("\n")
    searchFrame = [sg.Frame('FILTER', [[sg.Frame('', getSearchFrame(conn, userID)), sg.Frame('', getSearchTimeFrame())],
                                       [buttonElement("Search", "-search-", (100, 1))]])]

    table = sg.Table(values=transactionsList,
                     headings=["Type", "Account No.",
                               "Time", "Amount", "Description"],
                     auto_size_columns=False,
                     col_widths=(7, 12, 16, 8, 25),
                     justification='left', key='-transactionTable-', size=(1000, 300), font=(DEFAULT_FONT, 15))

    frame = [searchFrame,
             [titleText("Transactions")], [table]]

    transactionsTab = [[sg.Column(frame)]]
    return transactionsTab
