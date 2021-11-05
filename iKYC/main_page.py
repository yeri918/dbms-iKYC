import PySimpleGUI as sg
from tabs import home, myAccounts, transactions, profile


def mainPage():
    # Define Layout with Tabs
    tabgrp = [[sg.TabGroup([[sg.Tab('Home', home.homeTab, title_color='Black', border_width=10, background_color='White',
                                    tooltip='Personal details', element_justification='center'),
                            sg.Tab('My Accounts', myAccounts.myAccountsTab, title_color='Black',
                                   background_color='White'),
                            sg.Tab('Transactions', transactions.transactionsTab, title_color='Black', background_color='White'
                                   ),
                            sg.Tab('Profile', profile.profileTab, title_color='Black', background_color='White')]], tab_location='centertop',
                           title_color='White', tab_background_color='Black', selected_title_color='White',
                           selected_background_color='Gray', border_width=5), sg.Button('Close')]]

    # Define Window
    sg.theme('Dark Red')
    window = sg.Window("Tabs", tabgrp)

    while True:
        event, values = window.read()
        print(event)

        if event == "EXIT" or event == sg.WIN_CLOSED:
            break

        if event == "transaction_search":
            print('pressed')
            transactions.search()
        # window['-OUT-'].update(values['-IN-'])
        print("Month: ", window['month'])

    window.close()
