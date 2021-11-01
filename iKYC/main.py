import PySimpleGUI as sg
from layouts import layout1, layout2, layout3


# Define Layout with Tabs
tabgrp = [[sg.TabGroup([[sg.Tab('Personal Details', layout1.first, title_color='Black', border_width=10, background_color='White',
                                tooltip='Personal details', element_justification='center'),
                         sg.Tab('Account Information', layout2.second, title_color='Black',
                                background_color='White'),
                         sg.Tab('Search', layout3.layout3, title_color='Black', background_color='White',
                                tooltip='Enter  your Last job experience')]], tab_location='centertop',
                       title_color='White', tab_background_color='Black', selected_title_color='White',
                       selected_background_color='Gray', border_width=5), sg.Button('Close')]]

# Define Window
sg.theme('Dark Red')
window = sg.Window("Tabs", tabgrp)

while True:
    event, values = window.read()

    if event == "EXIT" or event == sg.WIN_CLOSED:
        break

    # window['-OUT-'].update(values['-IN-'])

window.close()
