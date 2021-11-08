from interface import *
import PySimpleGUI as sg
from openexchangerates import OpenExchangeRatesClient
from decimal import *
import loginWithFaceID


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
        [sg.Text('Login With Email',
                 justification='right', font='Helvetica 20')],
        [sg.Text('Email ', justification='center', size=(7,1),font=(
        DEFAULT_FONT,
        15)),
         sg.InputText(key='-email-', do_not_clear=True,size=(25,1))],
        [sg.Text('Password ', justification='center',size=(7,1),
                                                           font=(
                                                               DEFAULT_FONT,
                                                               15)),
         sg.InputText(
            key='-password-',do_not_clear=True, size=(25,1),
             password_char='*')],
        [sg.Button(key='-login-', button_text='Log In',
                   size=(10, 1), font='Helvetica 14')]]

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
        elif event == '-login-':
            # check the email, password verification
            print(values['-email-'],values['-password-'])
            # db check
            ################## DB QUERY CHECK TO GET checkEmail ###############
            checkEmail = True
            if checkEmail:
                print("successful")
                loginWithFaceID.loginFaceID()
                # while True:
                #     event, values = win.Read()
                # win.Close()
            else:
                sg.Popup("Login Failed. Please retry.")
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
        # session.logout()


main()
