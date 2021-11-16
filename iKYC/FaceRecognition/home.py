import PySimpleGUI as sg
import database as db
from datetime import datetime


def homeTabStuff(name, loginTime, accounts, transactions, loginHistory):
    welcomeLayout = [[sg.Text('Welcome ' + name + "!", font=("Helvetica",
                                                             25))],

                     [sg.Text('Current Session Login Time: ' + loginTime,
                              key="-currentSessionLoginTime-")],
                     ]

    yourAccountsLayout = [[sg.Text('Your Accounts:', size=(
        30, 1), font='Lucida', justification='left')],
        [

        sg.Table(values=accounts[:][:], headings=[
            "Type", "Number", "Balance"],
            max_col_width=12,

            # auto_size_columns=True,
            justification='l',
            num_rows=6,
            key='-TABLEOFACCOUNTS-',
            row_height=15,
            tooltip='This is a table of '
            'accounts')
    ],
        [sg.Text("More Details", font=("Lucida",
                                       11,
                                       "underline"),
                 enable_events=True,
                 key="-MOREDETAILSACCOUNTS-")]
    ]
    yourTransactionsLayout = [
        [sg.Text('Your Transactions:', size=(
            30, 1), font='Lucida', justification='left')],
        [
            sg.Table(values=transactions[:][:], headings=[
                "Type", "Date", "Amount (HKD)"],
                max_col_width=25,

                auto_size_columns=True,
                justification='c',
                num_rows=9,
                key='-TABLEOFTRANSACTIONS-',
                row_height=15,
                tooltip='This is a table of '
                'transactions')
        ], [
            sg.Text("More Details", font=("Lucida",
                                          11,
                                          "underline"),
                    enable_events=True,
                    key="-MOREDETAILSTRANSACTIONS-")]


    ]
    currencyCalcLayout = [[sg.Text("Input:", font='Lucida',
                                   justification='left')],
                          [sg.Input(size=(10, 4), key="-INPUTCURRENCYAMOUNT-",
                                    background_color="White",
                                    default_text=0.0),
                           sg.Combo(["HKD", "USD", "CAD", "KRW", "INR"],
                                    default_value="HKD", size=(6, 7),
                                    key="-INPUTCURRENCY-")],
                          [sg.Text("Output:", font='Lucida',
                                   justification='left')],
                          [sg.Input(size=(10, 4),
                                    key="-OUTPUTCURRENCYAMOUNT-",
                                    background_color="White",
                                    readonly=True),
                           sg.Combo(["HKD", "USD", "CAD", "KRW", "INR"],
                                    default_value="USD", size=(6, 7),
                                    key="-OUTPUTCURRENCY-")],
                          [sg.Button(button_text="Convert", pad=(5, 10))]
                          ]
    LoginHistoryLayout = [[sg.Text("Login History:", font='Lucida',
                                   justification='left')],
                          [sg.Listbox(values=loginHistory,
                                      key='-loginHistory-', size=(23, 6),
                                      pad=((0, 30), (0, 0))
                                      )]
                          ]

    rightPaneLayout = [[sg.Frame("Currency Converter", currencyCalcLayout,
                                 font="Lucida")],
                       [sg.Column(LoginHistoryLayout,
                                  element_justification="left")]]

    mainPanelLayout = [[
        sg.Column(yourAccountsLayout, pad=(0, 0), size=(220, 400)), sg.Column(
            yourTransactionsLayout, pad=(0, 0), size=(250, 400)),
        sg.Column(rightPaneLayout, pad=(7, 0), size=(170, 400))
    ]]
    layout = [[sg.Column(welcomeLayout, expand_x=True,
                         element_justification="c")], [sg.Column(
                             mainPanelLayout, expand_y=True)]]

    return layout


def getAccountsInfo(conn, userID):
    accounts = db.getCustomerAccount(conn, userID)
    accountsList = []
    for i in accounts:
        oneAccount = (i['account_type'], i['account_number'], i['balance'])
        accountsList.append(oneAccount)
    return accountsList


def getTransactionsInfo(conn, userID):
    transactions = db.getTransactionHome(conn, userID)
    print(transactions)
    transactionList = []
    print("TRANSACTIONS INFO")
    for i in transactions:
        date_time = i['transaction_time'].strftime("%m/%d/%Y %H:%M:%S")
        oneTransaction = (i['transaction_type'],
                          date_time, i['transaction_amount'])
        transactionList.append(oneTransaction)
    return transactionList


def getLoginHistory(conn, userID):
    logins = db.getLoginHistory(conn, userID)
    print(logins)
    loginsList = []
    for i in logins:
        print(i['login_time'])
        date_time = i['login_time'].strftime("%m/%d/%Y %H:%M:%S")
        loginsList.append(date_time)
    return loginsList
