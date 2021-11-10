import PySimpleGUI as sg

profileTab = [[sg.Text('Welcome!', font=("Helvetica", 25), key='profile1')],
              [sg.Text('Name', size=(10, 1), key='name'),
               sg.Input('', key='eName')],
              [sg.Text('Login Time:', size=(10, 1)), sg.Input('', key='eDob')],
              [sg.Text('Login History:', size=(10, 1)), sg.Input('', key='ePhone')]]
