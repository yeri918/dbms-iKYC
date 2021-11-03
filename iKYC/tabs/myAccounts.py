import PySimpleGUI as sg

myAccountsTab = [[sg.Text('Highest Qualfication', size=(15, 1)), sg.Input('', key='eQual')],
                 [sg.Text('Year of Qualifying', size=(15, 1)),
                  sg.Input('', key='eYoq')],
                 [sg.Text('Grade', size=(15, 1)), sg.Input('', key='eGrade')],
                 [sg.Text('University/College', size=(15, 1)),
                  sg.Input('', key='eQUniv')],
                 [sg.Listbox(values=['Listbox 1', 'Listbox 2',
                                     'Listbox 3'], size=(30, 6))]
                 ]
