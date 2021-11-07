import PySimpleGUI as sg


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
                                       background_color='pink',
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
                                   text_color="Blue",
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
                     background_color='light blue',
                     auto_size_columns=True,
                     justification='c',
                     num_rows=9,
                     key='-TABLEOFTRANSACTIONS-',
                     row_height=15,
                     tooltip='This is a table of '
                             'transactions')
        ],[
            sg.Text("More Details", font=("Lucida",
                                                       11,
                                                       "underline"),
                     text_color="Blue",
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
