import PySimpleGUI as sg
import signup


Left_Column = [[sg.Text('No account yet?'), sg.Text(' '*10)],
               [sg.Button('Sign Up')]]

Right_Column = [[sg.Text(' '*10), sg.Button('Forgot email')],
                [sg.Text(' '*10), sg.Button('Forgot password')]]

layout = [[sg.Text('Email : '), sg.InputText(key='in1', do_not_clear=False)],
          [sg.Text('Password : '), sg.InputText(
              key='in2', do_not_clear=False, password_char='*')],
          [sg.Button('Log In')],
          [sg.Text('_' * 60)],
          [sg.Column(Left_Column), sg.VSeperator(), sg.Column(Right_Column)]]

window = sg.Window('Log In', layout, margins=(20, 40))

while True:
    event, values = window.read()
    if(event == "Sign Up"):
        signup.signup()

    if event == "EXIT" or event == sg.WIN_CLOSED:
        break
