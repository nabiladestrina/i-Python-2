import PySimpleGUI as sg
sg.theme("BlueMono")
sg.theme_text_color("#C1CDCD")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("FTI UNISKA ")],
                           [sg.Text("FAKULTAS TEKNOLOGI INFORMASI ")],
                           [sg.Text("UNISKA MAB BANJARMASIN")]],
                    size=(430,200),
                    font=("Arial",18))
window()
window.close()