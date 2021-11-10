import textwrap

import PySimpleGUI as sg

# profileTab = [[sg.Text('Welcome!', font=("Helvetica", 25), key='-profile1-')],
#               [sg.Text('Name', size=(10, 1), key='name'),
#                sg.Input('', key='eName')],
#               [sg.Text('Login Time:', size=(10, 1)), sg.Input('', key='eDob')],
#               [sg.Text('Login History:', size=(10, 1)), sg.Input('', key='ePhone')]]

def userInfo(name, dob, phoneNumber, email, address):
    welcomeLayout = [[],[sg.Text('Name: ' + name,font=("Lucida", 13) )],
                     [sg.Text('Date of Birth: ' + dob,font=("Lucida", 13) )],
                     [sg.Text('Contact Number: ' + phoneNumber,font=("Lucida", 13) )],
                     [sg.Text('Email Address: ' + email,font=("Lucida", 13))],
                     [sg.Text('Correspondence Address: ' + address, font=("Lucida", 13))]

                     ]
    return welcomeLayout

def tncPage():
    text1 = [[sg.Text("A Terms and Conditions agreement is the agreement that includes the terms, ",font=("Lucida", 13))]]
    layout = [[sg.Frame('TERMS AND CONDITIONS',text1,font=("Lucida", 14),size=(700, 250) )]
              ]
    return layout


def frame1(name, dob, phoneNumber, email, address):

    yes= [[sg.Frame('USER DETAILS', userInfo(name, dob, phoneNumber, email, address),font=("Lucida", 14),size=(700, 200) )] ]


    return yes

def frameRight(name, dob, phoneNumber, email, address):
    layout = [[sg.Frame('', frame1(name, dob, phoneNumber, email, address), size=(700, 200))],
               [sg.Frame('', tncPage(), size=(700, 200))],
              [sg.Button('Sign Out',font=("Lucida", 10), size=(25,2))]]
    return layout

