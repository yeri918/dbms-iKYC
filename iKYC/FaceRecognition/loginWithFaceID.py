from DEFINE import *
import face_capture
import train
from faces import checkFaceID


def loginFaceID():
    # need the user's name (db query)
    layoutForFaceID = [[sg.Text('Log In With Face ID', justification='center', font='Helvetica 20')],
                       [sg.Image(
                           filename='FaceRecognition/image/faceidimage.png',
                           key='-faceid-')],
                       [sg.Button(key='-trainFace-', button_text='Train',
                                  size=(10, 1), font='Helvetica 14')],
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
                face_capture.faceCapture("Pranay")
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
