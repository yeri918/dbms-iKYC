import PySimpleGUI as sg
import DEFINE


def getAccountsList():
    return ['Account 1', 'Account 2', 'Account 3']


transactionsTab = [[sg.Text('Month', size=(5, 1), font=DEFINE.font),
                    sg.Text('From', size=(10, 1), font='Lucida')],
                   [sg.Combo(getAccountsList(), key='month')],
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


def search():
    print('hi from search function')
    sg.Popup("hi")
