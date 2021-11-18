import PySimpleGUI as sg


def userInfo(name, dob, phoneNumber, email, address):
    welcomeLayout = [[], [sg.Text('Name: ' + name, font=("Lucida", 15))],
                     [sg.Text('Date of Birth: ' + dob, font=("Lucida", 15))],
                     [sg.Text('Contact Number: ' + phoneNumber,
                              font=("Lucida", 15))],
                     [sg.Text('Email Address: ' + email, font=("Lucida", 15))],
                     [sg.Text('Correspondence Address: ' +
                              address, font=("Lucida", 15))]
                     ]
    return welcomeLayout


def tncPage():
    text1 = [sg.Multiline("By using this Site, you agree to be bound by, and to comply with, these Terms and Conditions."
                          " If you do not agree to these Terms and Conditions, please do not use this site."
                          "THE USER UNDERSTANDS THAT ALL TRANSACTIONS AND TRANSFERS MADE ON THIS APPLICATION HOLD NO REAL MONETARY VALUE"
                          " AND ARE FOR THE PRACTICAL PURPOSE OF THE PROJECT ONLY"
                          "these Terms and Conditions at any time. Unless otherwise indicated, amendments will become "
                          "effective immediately. Please review these Terms and Conditions periodically. "
                          "Your continued use of the Site following the posting of changes and/or modifications will "
                          "constitute your acceptance of the revised Terms and Conditions and the reasonableness "
                          "of these standards for notice of changes."
                          "Any person logging on to or using the Website (even when such person does not avail of any "
                          "services provided in the Website (SERVICES)) (hereinafter referred to as a USER, SELLER, "
                          "YOU or CLIENT) shall be presumed to have read these Terms of Use (which includes the Privacy Policy)"
                          "For the purpose of these Terms of Use, wherever the context so requires, the term User"
                          " shall mean and include any natural or legal person who has agreed to these Terms of Use on "
                          "behalf of itself or any other legal entity.", disabled=True, font=("Lucida", 12), size=(650, 175), key="ml")],

    layout = [[sg.Frame('TERMS AND CONDITIONS', text1, font=("Lucida", 14), size=(700, 250))]
              ]
    return layout


def frame1(name, dob, phoneNumber, email, address):

    yes = [[sg.Frame('USER DETAILS', userInfo(
        name, dob, phoneNumber, email, address), font=("Lucida", 14), size=(700, 200))]]

    return yes


def frameRight(name, dob, phoneNumber, email, address):
    layout = [[sg.Frame('', frame1(name, dob, phoneNumber, email, address), size=(700, 200))],
              [sg.Frame('', tncPage(), size=(700, 230))],
              [sg.Button('Sign Out', font=("Lucida", 18), size=(90, 1), key='Sign out')]]
    return layout
