from DEFINE import *
import PySimpleGUI as sg
from tabs import accountsPage


class Session:
    def __init__(self, conn, userID):
        self.conn = conn
        self.userID = userID
        # sg.theme('DarkTanBlue')

    def getMainWindow(self):
        window = sg.Window(
            "iKYC Main Page", layout=self.getMainLayout(), size=DEFAULT_WINDOW_SIZE, element_justification='center')
        return window

    ################################## LAYOUTS #########################################

    def getMainLayout(self):
        layout = [[sg.TabGroup([[sg.Tab('Home', self.getHomeLayout(), title_color='Black', border_width=10, background_color='White',
                                        tooltip='Personal details', element_justification='center'),
                                 sg.Tab('My Accounts', self.getAccountsLayout(), title_color='Black',
                                        background_color='White', ),
                                 sg.Tab('Transactions', accountsPage.getTransactionLayout(
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

    def getProfileLayout(self):
        profileTab = [[subTitleText('Name')]]
        return profileTab

    ################################## Get From DB #########################################
