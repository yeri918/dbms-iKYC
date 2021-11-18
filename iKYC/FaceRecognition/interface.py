from DEFINE import *
import PySimpleGUI as sg
from home import homeTabStuff, getAccountsInfo, getTransactionsInfo, getLoginHistory
from datetime import datetime
import database as db
import home


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
                                 sg.Tab('My Accounts', self.getAccountsLayout(),
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
                                        background_color='White')
                                 ],
                                ],
                               tab_location='topcenter',
                               title_color='White',
                               tab_background_color='Black',
                               selected_title_color='White',
                               selected_background_color='Gray',
                               border_width=5, size=DEFAULT_WINDOW_SIZE,
                               font=("Helvetica", 15), key="-MAINTABGROUP-",
                               expand_x=True)
                   ]]
        return layout

    def getHomeLayout(self):
        name = db.getCustomerName(self.conn, self.userID)
        name = name['first_name']+" "+name['last_name']
        accounts = home.getAccountsInfo(self.conn, self.userID)
        transactions = getTransactionsInfo(self.conn, self.userID)
        loginHistory = getLoginHistory(self.conn, self.userID)

        formattedAccounts = []
        for i in accounts:
            formattedAccounts.append([i[0], i[1], i[2]])

        formattedAccountsTransactions = []
        for transaction in transactions:
            formattedAccountsTransactions.append([transaction[0],
                                                  transaction[1].split(" ")[0],
                                                  transaction[2]])

        currentLoginTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        homeTab = homeTabStuff(name=name, loginTime=currentLoginTime,
                               accounts=formattedAccounts,
                               transactions=formattedAccountsTransactions,
                               loginHistory=loginHistory)

        return homeTab

    def getProfileLayout(self):
        userInfo = db.getProfileInfo(self.conn, self.userID)
        name = userInfo['first_name']+" "+userInfo['last_name']
        dob = userInfo['date_of_birth'].strftime("%d/%m/%Y %H:%M:%S")
        address = userInfo['address']
        email = userInfo['email']
        phoneNumber = userInfo['phone_number']
        myProfileTab = profile.frameRight(
            name, dob, phoneNumber, email, address)

        return myProfileTab

    def getAccountsLayout(self):
        currentInfo = db.getCurrentAccountInfo(self.conn, self.userID)
        savingInfo = db.getSavingsAccountInfo(self.conn, self.userID)
        savingAccNum = savingInfo['account_number']
        currentAccNum = currentInfo['account_number']
        overdraft = currentInfo['overdraft']
        intRate = savingInfo['interest_rate']
        currentBalance = currentInfo['balance']
        savingBalance = savingInfo['balance']
        status = 'Active'
        myAccountsTab = accounts1.accountsFrame(savingAccNum, currentAccNum,
                                                overdraft, intRate, savingBalance, currentBalance, status)
        return myAccountsTab
