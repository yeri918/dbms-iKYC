from DEFINE import *
import PySimpleGUI as sg


class Session:
    def __init__(self, conn, userID):
        self.conn = conn
        self.userID = userID

    def getMainWindow(self):
        window = sg.Window(
            "iKYC Main Page", layout=self.getMainLayout(), size=DEFAULT_WINDOW_SIZE)
        return window

    def getMainLayout(self):
        layout = [[sg.TabGroup([[sg.Tab('Home', self.getHomeLayout(), title_color='Black', border_width=10, background_color='White',
                                        tooltip='Personal details', element_justification='center'),
                                 sg.Tab('My Accounts', self.getAccountsLayout(), title_color='Black',
                                        background_color='White', ),
                                 sg.Tab('Transactions', self.getTransactionLayout(
                                 ), title_color='Black', background_color='White'),
                                 sg.Tab('Profile', self.getProfileLayout(), title_color='Black', background_color='White')]], tab_location='centertop',
                               title_color='White', tab_background_color='Black', selected_title_color='White',
                               selected_background_color='Gray', border_width=5, size=DEFAULT_WINDOW_SIZE, font=("Helvetica", 15)), sg.Button('Close')]]
        return layout

    def getHomeLayout(self):
        homeTab = [[titleText('Welcome')]]

        return homeTab

    def getAccountsLayout(self):
        myAccountsTab = [[titleText('Accounts')]
                         ]
        return myAccountsTab

    def getTransactionLayout(self):
        transactionsTab = [[sg.Text('Account', size=(8, 1), font=DEFAULT_FONT),
                            sg.Text('From', size=(10, 1), font=DEFAULT_FONT),
                            sg.Text('To', size=(10, 1), font=DEFAULT_FONT)],
                           [sg.Combo(['Account 1', 'Account 2'], size=(10, 5), key='account'), sg.Combo(
                               ['Jan', 'Feb', 'Mar'], size=(3, 1), key='month'),
                            sg.Combo([1, 2, 3], size=(3, 1), key='day')],
                           [sg.Text('Month', size=(5, 1), font=DEFAULT_FONT),
                            sg.Text('From', size=(5, 1), font=DEFAULT_FONT)],
                           [sg.Text('Day', size=(30, 1),
                                    font='Lucida', justification='left')],
                           [sg.Combo(['New York', 'Chicago', 'Washington', 'Colorado',
                                      'Ohio', 'San Jose', 'Fresno', 'San Fransisco'], key='dest')],
                           [sg.Text('Choose Account Types', size=(
                               30, 1), font='Lucida', justification='left')],
                           [sg.Listbox(values=['Saving', 'Current', 'HKD',
                                               'USD'], select_mode='extended', key='fac', size=(30, 4))],
                           [sg.Button('Search', font=('Lucida', 12), key='transaction_search'),
                            sg.Button('Reset', font=('Lucida', 12))]]

        return transactionsTab

    def getProfileLayout(self):
        profileTab = [[subTitleText('Name')]]
        return profileTab
