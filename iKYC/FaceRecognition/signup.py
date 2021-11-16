from time import sleep
import PySimpleGUI as sg
import face_capture
import train
import base64
import hashlib


def signup():
    # Left_Column = [[sg.Text('To Enable FaceID'), sg.Text(' '*10)],
    #                [sg.Button('Train')]]
    #
    # Right_Column = [[sg.Button('Forgot email')],
    #                 [sg.Button('Forgot password')]]

    trainLayout = [

        [sg.Text("Train your face for facial recognition\n to secure your "
                 "account")],
        [sg.Button("Train", key="-TRAINFACEBUTTON-")],
        [sg.Text("", key="-DONETRAININGTEXT-", text_color="red")]

    ]

    addressLayout = [[sg.Text('Line 1: '), sg.InputText(
        key='-LINE1ADDRESS-', )],
        [sg.Text('Line 2: '), sg.InputText(
            key='-LINE2ADDRESS-', )],
        [sg.Text('City: '), sg.InputText(
            key='-CITY-', )],
        [sg.Text('Country: '), sg.InputText(
            key='-COUNTRY-', )]]

    layout = [[sg.Text('Last Name: '), sg.InputText(key='-LASTNAME-',
                                                    )],
              [sg.Text('Given Name(s): '), sg.InputText(
                  key='-GIVENNAME-')],
              [sg.Text('Email: '), sg.InputText(
                  key='-EMAIL-', )],
              [sg.Text('Password: '), sg.InputText(
                  key='-PASSWORD-', password_char="*")],
              [sg.Text("Date of Birth:"),
               sg.Input("DD / MM / YYYY", key="-DOB-", enable_events=True),
               sg.CalendarButton(
                  "Select",
                  target="-DOB-", format=('%d/ %m/ '
                                          '%Y'))],

              [sg.Frame('Address', addressLayout, pad=(0, 10))],
              [sg.Text("Types of accounts you would like to open (Must "
                       "choose at least 1):")],
              [sg.Checkbox("Savings Account", key="-CHECKBOX_SAVING-"),
               sg.Checkbox("Checking Account (HKD)",
                           key="-CHECKBOX_CHECKING_HKD-"),
               sg.Checkbox(
                   "Checking "
                   "Account ("
                   "USD)", key="-CHECKBOX_CHECKING_USD-")],
              [sg.HorizontalSeparator()],
              [sg.Text("Add a form of address proof (Bank statement, driver "
                       "license)"
                       ":")],
              [sg.FileBrowse(key="-ADDRESSPROOF-"), sg.Input()],
              [sg.Text("Add a form of identity proof (HKID, Passport):")],
              [sg.FileBrowse(key="-IDENTITYPROOF-"), sg.Input()],
              [sg.Column([[sg.Button("Sign Up", key="-SUBMITSIGNUP-")]],
                         element_justification="right", expand_x=True)]
              ]

    window = sg.Window('Sign Up', layout, margins=(20, 40))

    while True:
        event, values = window.read()
        print('event')
        if (event == 'Train'):
            try:
                face_capture.faceCapture("Yeseo")
            except:
                sg.Popup("Unable to train your face. Please try again.")

            train.trainFace()

        if event == "EXIT" or event == sg.WIN_CLOSED:
            break
        if event == "-DOB-":
            window.force_focus()

        if event == "-SUBMITSIGNUP-":
            print("submit signup button pressed")
            try:
                # need to collect all the input fields
                dob = values["-DOB-"]
                firstName = values["-GIVENNAME-"]
                lastName = values["-LASTNAME-"]
                email = values["-EMAIL-"]
                userpw = hashlib.sha1(
                    values['-PASSWORD-'].encode('utf-8')).hexdigest()
                userpw = bytearray(userpw.encode())
                print("check 1")
                # address details
                line1 = values["-LINE1ADDRESS-"]
                line2 = values["-LINE2ADDRESS-"]
                city = values["-CITY-"]
                country = values["-COUNTRY-"]
                print("check 2")
                # boolean values of check boxes
                savings_account = values["-CHECKBOX_SAVING-"]
                checking_account_hkd = values["-CHECKBOX_CHECKING_HKD-"]
                checking_account_usd = values["-CHECKBOX_CHECKING_USD-"]

                # converting address proof file to blob
                if values["-ADDRESSPROOF-"] != "":
                    with open(values["-ADDRESSPROOF-"], 'rb') as f:
                        addressProof = base64.b64encode(f.read())

                if values["-IDENTITYPROOF-"] != "":
                    # converting identity proof file to blob
                    with open(values["-IDENTITYPROOF-"], 'rb') as f:
                        identityProof = base64.b64encode(f.read())

                print(firstName, lastName, dob, email, userpw, line1, line2,
                      city, country, savings_account, checking_account_usd,
                      checking_account_hkd)

                # if all data is entered
                if firstName != "" and lastName != "" and email != "" and \
                        userpw != "" \
                        and line1 != "" and city != "" and country != "" and (
                            checking_account_usd or checking_account_hkd
                                or savings_account) and identityProof != None \
                        and addressProof != None:
                    print("data entered")
                    # you can upload data here
                    print("before train window opens")
                    # then to image recognitino screen
                    window.close()
                    trainFaceWindow = sg.Window('Train face', trainLayout, margins=(
                        20, 40))
                    event, values = trainFaceWindow.read()
                    if event == "-TRAINFACEBUTTON-":
                        try:
                            face_capture.faceCapture(firstName)
                            train.trainFace()
                            trainFaceWindow["-DONETRAININGTEXT-"].update(
                                "Training done! You may close the window "
                                "and sign in or\n "
                                "train again if you wish.")

                        except:
                            sg.Popup(
                                "Unable to train your face. Please try again.")

                    if event == "EXIT" or event == sg.WIN_CLOSED:
                        break
                else:
                    sg.popup("Not all fields were filled in. Please check.")
            except Exception as e:
                print(e)
                sg.popup("Issue with file upload. Please try again.")
