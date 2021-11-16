from interface import *
import PySimpleGUI as sg
from openexchangerates import OpenExchangeRatesClient
from decimal import *
import loginWithFaceID
import signup
import hashlib
import database as db


def main():
    # 1 Create database connection
    try:
        myconn = db.connect()
        print("database connection successful")
    except:
        print("connection unsuccessful")

    ###################### DEFINE THE START WINDOW LAYOUT ######################
    sg.theme('DarkGrey2')
    layout = [
        [titleText("")],
        [sg.Text('Login With Email',
                 justification='right', font='Helvetica 25')],
        [sg.Text('Email ', justification='center', size=(7, 1), font=(
            DEFAULT_FONT,
            20)),
         sg.InputText(key='-email-', do_not_clear=True, size=(25, 1), font=(DEFAULT_FONT, 15))],
        [sg.Text('Password ', justification='center', size=(7, 1),
                 font=(
            DEFAULT_FONT,
            20)),
         sg.InputText(
            key='-password-', do_not_clear=True, size=(25, 1),
             password_char='*', font=(DEFAULT_FONT, 15))],
        [sg.Button(key='-login-', button_text='Log In',
                   size=(10, 1), font='Helvetica 14')],
        [titleText("")],
        [sg.Text('Sign Up',
                 justification='right', font='Helvetica 25')],
        [subTitleText(
            "Please sign up if you do not have an account.", textSize=(35, 1))],
        [sg.Button(key='-signup-', button_text='Sign up',
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
        if event == '-login-':
            # check the email, password verification
            # db check
            ################## DB QUERY CHECK TO GET checkEmail ###############

            if values['-email-'] != "" and values['-password-'] != "":

                ####################################
                ############# DO NOT DELETE################
                dbpw = db.getLoginInfo(myconn, values['-email-'])
                userpw = hashlib.sha1(
                    values['-password-'].encode('utf-8')).hexdigest()
                userpw = bytearray(userpw.encode())

                checkEmail = False
                if dbpw[0] == userpw:
                    checkEmail = True
                    print("passwords check")
                    customerID = db.getCustomerID(myconn, values['-email-'])
                #######################################
                if checkEmail:
                    print("successful")
                    # folder name is based on email id so need to send email id
                    login_Success = loginWithFaceID.loginFaceID(values['-email-'])

                    window.Close()

                    # while True:
                    #     event, values = win.Read()
                    # win.Close()
                else:
                    sg.Popup("Login Failed. Please retry.")

            else:
                sg.popup("Please enter correct values.")

        if event == '-signup-':

            signup.signup()

            # window = sg.Window("Sign Up",)

    if login_Success:
        # conn = db.connect()
        conn = True
        # userID = login_ID
        db.updateLoginHistory(myconn, customerID)
        session = Session(myconn, customerID)
        # session.login()

        win = session.getMainWindow()

        while True:
            event, values = win.Read()
            # win['-transactionTable-'].expand(True, True)

            if event is None or event == 'Cancel':
                break
            if event == '-search-':
                print("search pressed")
                fromTime = datetime.strptime(
                    values['-fromDate-'] + " "+values['-fromTime-'], '%d/%m/%Y %H:%M:%S')
                toTime = datetime.strptime(
                    values['-toDate-'] + " "+values['-toTime-'], '%d/%m/%Y %H:%M:%S')

                transactions = db.filterTransactionWithType(
                    myconn, values['-account-'], fromTime, toTime, values['-fromAmount-'], values['-toAmount-'])
                updateTrans = transactionPage.getTableValues(transactions)
                win.Element('-transactionTable-').Update(values=updateTrans)
                win['-TRANSACTIONSTAB-'].Update(visible=True)

            if event == '-transferButton-':
                if (values['-accountTransfer-'] == "" or values['-transferTo-'] == "" or
                        values['-amountTransfer-'] == "" or values['-currencyTransfer-'] == ""):
                    sg.Popup("Please enter all values.")
                else:
                    amount = transferPage.convertToHKD(
                        values['-amountTransfer-'], values['-currencyTransfer-'])
                    success = db.addTransactionSuccess(
                        myconn, values['-accountTransfer-'][-11:], amount, "transfer", values['-remarksTransfer-'])
                    if not success:
                        sg.Popup("Transaction unsuccessful.")
                    else:
                        sg.Popup("Transaction successful!")
                        win['-amountTransfer-'].update("")
                        win['-transferTo-'].update("")
                        win['-remarksTransfer-'].update("")

            # event if more details on accounts text clicked, take to
            # accounts tab
            if event == "-MOREDETAILSACCOUNTS-":
                win.Element("-ACCOUNTTAB-").select()

            # event if more details on transactions text clicked, take to
            # transactions tab
            if event == '-MOREDETAILSTRANSACTIONS-':
                win.Element("-TRANSACTIONSTAB-").select()
            # event if more details on transactions text clicked, take to
            # transactions tab
            if event == '-transcationPageDetails-':
                win.Element("-TRANSACTIONSTAB-").select()
            if event == '-transcationPageDetails1-':
                win.Element("-TRANSACTIONSTAB-").select()

            # currency convert button event
            if event == "Convert":
                client = OpenExchangeRatesClient(
                    'b959b3966492436dba1b623fbfee1849')
                inputCurrencyAmt = values['-INPUTCURRENCYAMOUNT-']
                inputCurrency = values['-INPUTCURRENCY-']
                outputCurrency = values['-OUTPUTCURRENCY-']

                fromInputCurrencyToUSD = Decimal(inputCurrencyAmt)
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

            if event == '-search1-':
                print("ACCOUNTS_SEARCH - values for queries")
                print(values['-account1-'])

            if event == sg.WIN_CLOSED or event == 'Sign Out':  # if user closes window or clicks cancel
                break

        win.Close()
        session.logout()


main()
