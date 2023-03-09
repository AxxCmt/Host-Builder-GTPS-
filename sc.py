import PySimpleGUI as sg
import requests
import os

sg.theme('DarkAmber')  # please make your windows colorful

layout = [
    [sg.Text('GTPS Host Builder | Axx Community')],
    [sg.Text('IP Address:'), sg.InputText(key='ip_address')],
    [sg.Text('Name Host:'), sg.InputText(key='name_host')],
    [sg.Text('Extension (txt):'), sg.InputText(key='file_type')],
    [sg.Text('Source for Folders', size=(15, 1)), sg.InputText(key='source_folder'), sg.FolderBrowse()],
    [sg.Text('Dont be annoying!, Credit > OpenAi, PySimpleGui')],
    [sg.Submit(), sg.Cancel()]
]

# Create the Window
window = sg.Window('Axx Community | V1.0 | Host Builder', layout, enable_close_attempted_event=True)

# Event Loop to process "events"
while True:
    event, values = window.read()
    print(event, values)
    if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Cancel') and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
        break
    elif event == 'Submit':
        name_host = values['name_host']
        ip_address = values['ip_address']
        file_type = values['file_type']
        source_folder = values['source_folder']
        if not name_host or not ip_address or not source_folder or not file_type:
            sg.popup_error("Axx | Warning", "Please fill in all the fields!")
        else:
            filename = f"{name_host}.{file_type}"
            filepath = os.path.join(source_folder, filename)
            with open(filepath, 'w') as file:
                file.write(f"{ip_address} www.growtopia1.com\n{ip_address} www.growtopia2.com\n{ip_address} growtopia1.com\n{ip_address} growtopia2.com")
            sg.popup(f"File {filename} has been created with IP Address {ip_address} in {source_folder}")

window.close()