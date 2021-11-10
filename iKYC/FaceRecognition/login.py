import PySimpleGUI as sg
import signup
import main_page


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

# authentication for log in
authentication = True

while True:
    event, values = window.read()
    if(event == "Sign Up"):
        signup.signup()

    if(event == "Log In"):

        if(authentication):
            main_page.mainPage()
        else:
            sg.Popup("Log in failed.")
        break

    if event == "EXIT" or event == sg.WIN_CLOSED:
        break

# import PySimpleGUI as sg
#
# sg.theme('DarkAmber')   # Add a touch of color
# # All the stuff inside your window.
# layout = [  [sg.Text('Some text on Row 1')],
#             [sg.Text('Enter something on Row 2'), sg.InputText()],
#             [sg.Button('Ok'), sg.Button('Cancel')] ]
#
# # Create the Window
# window = sg.Window('Window Title', layout)
# # Event Loop to process "events" and get the "values" of the inputs
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
#         break
#     print('You entered ', values[0])
#
# window.close()