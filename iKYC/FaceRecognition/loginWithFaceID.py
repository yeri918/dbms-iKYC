from DEFINE import *
import face_capture
import train
from faces import checkFaceID


def loginFaceID(email):
    layoutForFaceID = [[sg.Text('2 Factor Authentication', justification='center', font='Helvetica 22')],
                       [sg.Text('Log In With Face ID',
                                justification='center', font='Helvetica 20')],
                       [sg.Image(
                           filename='image/faceidimage.png',
                           key='-faceid-')],
                       [sg.Button(key='-loginFaceID-', button_text='Face ID', size=(10, 1), font='Helvetica 14')]]

    window = sg.Window('Login with Face ID', layoutForFaceID,
                       size=DEFAULT_WINDOW_SIZE,
                       margins=(
                           20, 40), element_justification="c")

    while True:
        event, values = window.Read()
        print(event)
        if (event == '-trainFace-'):
            try:
                face_capture.faceCapture(email)
                train.trainFace()
            except:
                sg.Popup("Unable to train your face. Please try again.")

        if event == '-loginFaceID-':
            try:
                return checkFaceID()
            except Exception as e:
                sg.popup("Something went wrong with opening the camera.")
                print(e)
        if event == "EXIT" or event == sg.WIN_CLOSED:
            break

    return True
