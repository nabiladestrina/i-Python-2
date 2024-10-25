import PySimpleGUI as sg
sg.theme("DarkGreen")
sg.theme_text_color("#E3CF57")
window = sg.Window(title="Profile",
                 layout=[[sg.Text("FTI UNISKA",font=("Helvetica",24))],
                         [sg.Text("FAKULTAS TEKNOLOGI INFORMASI ")],
                         [sg.Text("UNISKA MAB BANJARMASIN")]],
                    size=(430,200),
                    font=("Arial", 18))
window()
window.close()