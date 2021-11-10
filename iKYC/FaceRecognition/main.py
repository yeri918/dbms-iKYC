from interface import *
import PySimpleGUI as sg
from openexchangerates import OpenExchangeRatesClient
from decimal import *
import loginWithFaceID
import hashlib
import database as db


def main():
    # 1 Create database connection
    try:
        myconn = db.connect()
        print("database connection successful")
    except:
        print("connection unsuccessful")

    cursor = myconn.cursor()

    ############# EXAMPLE ###################
    name = cursor.execute("SELECT * FROM Customer")
    result = cursor.fetchall()
    print(type(result))
    print(result)
    ########################################

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
        [sg.Text('Login With Email',
                 justification='right', font='Helvetica 20')],
        [sg.Text('Email ', justification='center', size=(7, 1), font=(
            DEFAULT_FONT,
            15)),
         sg.InputText(key='-email-', do_not_clear=True, size=(25, 1))],
        [sg.Text('Password ', justification='center', size=(7, 1),
                 font=(
            DEFAULT_FONT,
            15)),
         sg.InputText(
            key='-password-', do_not_clear=True, size=(25, 1),
             password_char='*')],
        [sg.Button(key='-login-', button_text='Log In',
                   size=(10, 1), font='Helvetica 14')],
        [subTitleText(
            "Please sign up if you do not have an account.", textSize=(35, 1))],
        [buttonElement("Sign Up", "-signup-")]]

    # 3 Create the window
    window = sg.Window('Log In', layout, size=DEFAULT_WINDOW_SIZE,
                       element_padding=None,
                       margins=(None, None), element_justification='center')

    login_Success = False
    login_ID = None

    while True:
        event, values = window.read(timeout=20)
        if event == 'Close' or event == sg.WIN_CLOSED:
            break
        if event == '-login-':
            # check the email, password verification
            # db check
            ################## DB QUERY CHECK TO GET checkEmail ###############
            if values['-email-'] != "" and values['-password-'] != "":
                # temporary values, need ot get these from the db based on the
                # email entered
                email = "p"
                password = hashlib.sha256(b"p").hexdigest()

                checkEmail = False
                bytePassword = values['-password-'].encode()

                if values['-email-'] == email and hashlib.sha256(
                        bytePassword).hexdigest() == password:
                    checkEmail = True

                if checkEmail:
                    print("successful")
                    login_Success = loginWithFaceID.loginFaceID()
                    window.Close()

                    # while True:
                    #     event, values = win.Read()
                    # win.Close()
                else:
                    sg.Popup("Login Failed. Please retry.")

            else:
                sg.popup("Please enter correct values.")

        # if event == '-signup-':

            # window = sg.Window("Sign Up",)

    if login_Success:
        # conn = db.connect()
        conn = True
        userID = login_ID

        session = Session(conn, userID)
        # session.login()

        win = session.getMainWindow()

        while True:
            event, values = win.Read()
            # win['-transactionTable-'].expand(True, True)

            if event is None or event == 'Cancel':
                break
            if event == '-search-':
                print("search pressed")
                print(values)

            # event if more details on accounts text clicked, take to
            # accounts tab
            if event == "-MOREDETAILSACCOUNTS-":
                win.Element("-ACCOUNTTAB-").select()

            # event if more details on transactions text clicked, take to
            # transactions tab
            if event == '-MOREDETAILSTRANSACTIONS-':
                win.Element("-TRANSACTIONSTAB-").select()

            # currency convert button event
            if event == "Convert":
                client = OpenExchangeRatesClient(
                    'b959b3966492436dba1b623fbfee1849')
                inputCurrencyAmt = values['-INPUTCURRENCYAMOUNT-']
                inputCurrency = values['-INPUTCURRENCY-']
                outputCurrency = values['-OUTPUTCURRENCY-']

                fromInputCurrencyToUSD = Decimal(inputCurrencyAmt) / \
                    client.latest()["rates"][inputCurrency]
                fromUSDToOutputCurrency = round(fromInputCurrencyToUSD *
                                                client.latest()["rates"][
                                                    outputCurrency], 2)
                win['-OUTPUTCURRENCYAMOUNT-'].update(fromUSDToOutputCurrency)

            if event == '-search-':
                print("TRANSACTION_SEARCH - values for queries")
                print(values['-account-'], values['-fromAmount-'], values['-toAmount-'],
                      values['-fromDate-'], values['-fromTime-'],
                      values['-toDate-'], values['-toTime-'])
        win.Close()
        session.logout()


main()
