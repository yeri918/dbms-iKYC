import PySimpleGUI as sg
import DEFINE


def getAccountsList():
    return ['Account 1', 'Account 2', 'Account 3']


def getMonthList():
    return ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def getDayList():
    dayList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
               16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    return dayList
    # if ( == 'Jan' or 'Mar' or 'May' or 'Jul' or 'Aug' or 'Oct' or 'Dec'):
    # dayList.append(31)


transactionsTab = [[sg.Text('Account', size=(8, 1), font=DEFINE.DEFAULT_FONT),
                    sg.Text('From', size=(10, 1), font=DEFINE.DEFAULT_FONT),
                    sg.Text('To', size=(10, 1), font=DEFINE.DEFAULT_FONT)],
                   [sg.Combo(getAccountsList(), size=(10, 5), key='account'), sg.Combo(
                       getMonthList(), size=(3, 1), key='month'),
                       sg.Combo(getDayList(), size=(3, 1), key='day')],
                   [sg.Text('Month', size=(5, 1), font=DEFINE.DEFAULT_FONT),
                    sg.Text('From', size=(5, 1), font=DEFINE.DEFAULT_FONT)],
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
