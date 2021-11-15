from DEFINE import *
import PySimpleGUI as sg
from home import homeTabStuff
from datetime import datetime
import database as db


import transactionPage
import accounts1
import transactionPage
import accounts1
import transferPage
import profile


class Session:
    def __init__(self, conn, userID):
        self.conn = conn
        self.userID = userID
        # if transaction =="":
        #     transaction = self.getTransactionsFromDB()
        # self.transaction = transaction
        # sg.theme('DarkTanBlue')
        self.transaction = self.getTransactionsFromDB()

    def getMainWindow(self):
        window = sg.Window(
            "iKYC Main Page", layout=self.getMainLayout(),
            size=DEFAULT_WINDOW_SIZE)
        return window

    def updateTransactions(self, transactions):
        self.getMainWindow(transactions)

    ################################## LAYOUTS #########################################

    def getTransactionsFromDB(self):
        transaction = db.getTransactionHistory(self.conn, self.userID)
        print("From getTransactionsFromDB", transaction)
        values = []
        for i in transaction:
            date_time = i['transaction_time'].strftime("%m/%d/%Y %H:%M:%S")
            temp = (i['transaction_type'], i['account_number'], date_time,
                    str(i['transaction_amount'])+"HKD", i['transaction_description'])
            values.append(temp)
        return values

    def getMainLayout(self):
        layout = [[sg.TabGroup([[sg.Tab('Home', self.getHomeLayout(),
                                        title_color='Black', border_width=10,
                                        background_color='White',
                                        tooltip='Personal details',
                                        element_justification='center'),
                                 sg.Tab('My Accounts',
                                        accounts1.accountsFrame(),
                                        title_color='Black',
                                        background_color='White',
                                        key="-ACCOUNTTAB-"),
                                 sg.Tab('Transactions',
                                        transactionPage.getTransactionLayout(
                                            self.conn, self.userID, self.getTransactionsFromDB()),
                                        title_color='Black',
                                        background_color='White',
                                        key="-TRANSACTIONSTAB-"),
                                 sg.Tab('Transfer',
                                        transferPage.getTransferLayout(
                                            self.conn, self.userID),
                                        title_color='Black',
                                        background_color='White',
                                        key='-TRANSFERTAB-'),
                                 sg.Tab('Profile', self.getProfileLayout(),
                                        title_color='Black',
                                        background_color='White'),
                                 sg.Tab('Sign Out', self.signOut(),
                                        title_color="Red",
                                        background_color='White',
                                        element_justification="right",
                                        expand_x="right"
                                        )],
                                ],
                               tab_location='topleft',
                               title_color='White',
                               tab_background_color='Black',
                               selected_title_color='White',
                               selected_background_color='Gray',
                               border_width=5, size=DEFAULT_WINDOW_SIZE,
                               font=("Helvetica", 15), key="-MAINTABGROUP-",
                               expand_x=True),




                   # [sg.Column([sg.Button("Close")],
                   #           element_justification="right")]],
                   ]]
        return layout

    def getHomeLayout(self):
        name = "Jane Doe"
        accounts = [("Savings", "903838203", 830323), ("Current Account (HKD)",
                                                       "3280223", 11000),
                    ("Current Account (USD)", "82324803", 12801.3)]

        transactions = [("Withdrawal", "2021-10-10 23:18:24", "123.83"),
                        ("Withdrawal", "2021-10-10 23:18:24", "111.0"),
                        ("Deposit", "2021-10-10 23:18:24", "10000.0"),
                        ("Deposit", "2021-10-10 23:18:24", "2000.0")
                        ]
        loginHistory = ["2021-10-09 19:20:19", "2021-10-09 19:20:19",
                        "2021-10-09 19:20:19"]

        formattedAccounts = []
        for i in accounts:
            formattedAccounts.append([i[0], i[1], i[2]])

        formattedAccountsTransactions = []
        for transaction in transactions:
            formattedAccountsTransactions.append([transaction[0],
                                                  transaction[1].split(" ")[0],
                                                  transaction[2]])

        formattedLoginHistory = []
        for i in loginHistory:
            formattedLoginHistory.append(datetime.strptime(i, "%Y-%m-%d "
                                                              "%H:%M:%S").strftime(
                "%d/%m/%Y %H:%M:%S"))

        currentLoginTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        homeTab = homeTabStuff(name=name, loginTime=currentLoginTime,
                               accounts=formattedAccounts,
                               transactions=formattedAccountsTransactions,
                               loginHistory=formattedLoginHistory)

        return homeTab

    def getProfileLayout(self):
        name = "Jane Doe"
        dob = "2021-10-10"
        address = "9 lung wah st"
        email = "thisisemail@email.com"
        phoneNumber = "456789123"
        myProfileTab = profile.frameRight(name, dob, phoneNumber, email,
                                          address)

        return myProfileTab

    def getAccountsLayout(self):
        myAccountsTab = [[titleText('Accounts')]
                         ]
        return myAccountsTab

    # def getTransactionListFrame(self):
    #     # get the account info from db
    #     accounts = {1: {'Title': 'Savings', 'amount': 1235, 'currency': 'HKD'}}
    #     frame_layout = []
    #     for account in accounts:
    #         accountInfo = []
    #         for info in account:
    #             if info == 'Title':
    #                 accountInfo.append[titleText(account[info])]
    #             else:
    #                 accountInfo.append[subTitleText(
    #                     info), subTitleText(account[info])]
    #         frame_layout.append(accountInfo)

    #     frame = sg.Frame('Accounts', frame_layout)
    #     return frame

    def getTransactionLayout(self):
        transactionsTab = [
            [subTitleText('Account'), subTitleText(
                'From'), subTitleText('Min. Amount')],
            [comboElement(['Account 1', 'Account2'], '-account-'),
             subTitleText('To'), subTitleText('Max. Amount')],
            [buttonElement('Search', '-search-')]]

        return transactionsTab

    # def getProfileLayout(self):
    #     profileTab = [[subTitleText('Name')]]
    #     return profileTab

    def signOut(self):
        signOut = [[titleText('Sign Out Page')]]
        # needs to end session and the take back to home screen

        return signOut
    ################################## Get From DB #########################################
