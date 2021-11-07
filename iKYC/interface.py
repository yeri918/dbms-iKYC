from DEFINE import *
import PySimpleGUI as sg
from home import homeTabStuff
from datetime import datetime


class Session:
    def __init__(self, conn, userID):
        self.conn = conn
        self.userID = userID

    def getMainWindow(self):
        window = sg.Window(
            "iKYC Main Page", layout=self.getMainLayout(),
            size=DEFAULT_WINDOW_SIZE)
        return window

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
                                        self.getTransactionLayout(
                                        ), title_color='Black',
                                        background_color='White',
                                        key="-TRANSACTIONSTAB-"),
                                 sg.Tab('Profile', self.getProfileLayout(),
                                        title_color='Black',
                                        background_color='White'),
                                 sg.Tab('Sign Out', self.signOut(),
                                        title_color="Red",
                                        background_color='White',
                                        )],
                                ],
                               tab_location='topleft',
                               title_color='White',
                               tab_background_color='Black',
                               selected_title_color='White',
                               selected_background_color='Gray',
                               border_width=5, size=DEFAULT_WINDOW_SIZE,
                               font=("Helvetica", 15), key="-MAINTABGROUP-"),
                   sg.Button(
            'Close')],
                  ]
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
                                                              "%H:%M:%S").strftime("%d/%m/%Y %H:%M:%S"))

        currentLoginTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")



        homeTab = homeTabStuff(name=name, loginTime=currentLoginTime,
                               accounts=formattedAccounts,
                               transactions=formattedAccountsTransactions,
                               loginHistory=formattedLoginHistory)

        return homeTab

    def getAccountsLayout(self):
        myAccountsTab = [[titleText('Accounts')]
                         ]
        return myAccountsTab

    def getTransactionLayout(self):
        transactionsTab = [[sg.Text('Account', size=(8, 1), font=DEFAULT_FONT),
                            sg.Text('From', size=(10, 1), font=DEFAULT_FONT),
                            sg.Text('To', size=(10, 1), font=DEFAULT_FONT)],
                           [sg.Combo(['Account 1', 'Account 2'], size=(10, 5),
                                     key='account'), sg.Combo(
                               ['Jan', 'Feb', 'Mar'], size=(3, 1), key='month'),
                            sg.Combo([1, 2, 3], size=(3, 1), key='day')],
                           [sg.Text('Month', size=(5, 1), font=DEFAULT_FONT),
                            sg.Text('From', size=(5, 1), font=DEFAULT_FONT)],
                           [sg.Text('Day', size=(30, 1),
                                    font='Lucida', justification='left')],
                           [sg.Combo(
                               ['New York', 'Chicago', 'Washington', 'Colorado',
                                'Ohio', 'San Jose', 'Fresno', 'San Fransisco'],
                               key='dest')],
                           [sg.Text('Choose Account Types', size=(
                               30, 1), font='Lucida', justification='left')],
                           [sg.Listbox(values=['Saving', 'Current', 'HKD',
                                               'USD'], select_mode='extended',
                                       key='fac', size=(30, 4))],
                           [sg.Button('Search', font=('Lucida', 12),
                                      key='transaction_search'),
                            sg.Button('Reset', font=('Lucida', 12))]]

        return transactionsTab

    def getProfileLayout(self):
        profileTab = [[subTitleText('Name')]]
        return profileTab

    def signOut(self):
        signOut = [[titleText('Sign Out Page')]]
        #needs to end session and the take back to home screen

        return signOut
