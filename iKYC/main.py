from interface import *
import PySimpleGUI as sg


def main():

    # 1 Create database connection

    # myconn = db.connect()
    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # cursor = myconn.cursor()

    # 2 Load reconizer and read labels from model

    # recognizer = cv2.face.LBPHFaceRecognizer_create()
    # recognizer.read("train.yml")

    # labels = {"person_name": 1}
    # with open("labels.pickle", "rb") as f:
    #     labels = pickle.load(f)
    #     labels = {v: k for k, v in labels.items()}

    ###################### DEFINE THE START WINDOW LAYOUT ######################

    # layout = [[sg.Text('Face Recognition', justification='center', font='Helvetica 20')],
    #           [sg.Text('Email '), sg.InputText(
    #               key='-email-', do_not_clear=False)],
    #           [sg.Text('Password : '), sg.InputText(
    #               key='-password-', do_not_clear=False, password_char='*')]
    #           [sg.Button(key='-login-', button_text='Log In', size=(10, 1), font='Helvetica 14')]]

    layout = [
        [sg.Text('Log In With Email',
                 justification='center', font='Helvetica 20')],
        [sg.Text('Email ', justification='right'),
         sg.InputText(key='-email-', do_not_clear=False)],
        [sg.Text('Password ', justification='right'), sg.InputText(
            key='-password-', do_not_clear=False, password_char='*')],
        [sg.Button(key='-login-', button_text='Log In',
                   size=(10, 1), font='Helvetica 14')],
        [sg.Text('Log In With Face ID',
                 justification='center', font='Helvetica 20')],
        [sg.Image(filename='image/faceidimage.png', key='-faceid-')],
        [sg.Button(key='-loginFaceID-', button_text='Face ID', size=(10, 1), font='Helvetica 14')]]

    # 3 Create the window
    window = sg.Window('Log In', layout, size=DEFAULT_WINDOW_SIZE, element_padding=None,
                       margins=(None, None), element_justification='center')

    login_Success = False
    login_ID = None

    while True:
        event, values = window.read(timeout=20)
        if event == 'Close' or event == sg.WIN_CLOSED:
            break
        elif event == '-login-':
            print("log in pressed")
            login_Success = True
            window.Close()

    if login_Success:
        # conn = db.connect()
        conn = True
        userID = login_ID

        session = Session(conn, userID)
        # session.login()

        win = session.getMainWindow()

        while True:
            event, values = win.Read()
            if event is None or event == 'Cancel':
                break
            if event == '-search-':
                print("search pressed")
                print(values)

        win.Close()
        # session.logout()


main()
