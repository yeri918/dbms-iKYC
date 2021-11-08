import PySimpleGUI as sg
from iKYC import face_capture, train


def signup():
    Left_Column = [[sg.Text('To Enable FaceID'), sg.Text(' '*10)],
                   [sg.Button('Train')]]

    Right_Column = [[sg.Button('Forgot email')],
                    [sg.Button('Forgot password')]]

    layout = [[sg.Text('Username: '), sg.InputText(key='username', do_not_clear=False)],
              [sg.Text('Password: '), sg.InputText(
                  key='password', do_not_clear=False, password_char='*')],
              [sg.Text('Email: '), sg.InputText(
                  key='email', do_not_clear=False)],
              [sg.Column(Left_Column), sg.VSeperator(), sg.Column(Right_Column)]]

    window = sg.Window('Sign Up', layout, margins=(20, 40))

    while True:
        event, values = window.Read()
        print('event')
        if(event == 'Train'):
            try:
                face_capture.faceCapture("Yeseo")
            except:
                sg.Popup("Unable to train your face. Please try again.")

            train.trainFace()

        if event == "EXIT" or event == sg.WIN_CLOSED:
            break
