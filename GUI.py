import PySimpleGUI as sg
from zip_extractor import extract_archive

sg.theme('Black')

label1 = sg.Text('Select Archive: ')
input1 = sg.Input()
choose_button1 = sg.FileBrowse('Choose', key='archive')

label2 = sg.Text('Select Destination: ')
input2 = sg.Input()
choose_button2 = sg.FolderBrowse('Choose', key='folder')

extract_button = sg.Button('Extract')
output_label = sg.Text(key='output', text_color='green')

space = sg.Text('')
space2 = sg.Text('')

col1 = sg.Column([[label1], [label2], [extract_button]])
col2 = sg.Column([[input1], [input2], [space]])
col3 = sg.Column([[choose_button1], [choose_button2], [space2]])

window = sg.Window('Archive Extractor', layout=[[col1, col2, col3]])

#                                               [[label1, input1, choose_button1],
#                                               [label2, input2, choose_button2],
#                                               [extract_button, output_label]])



while True:
    event, values = window.read()
    match event:
        case sg.WIN_CLOSED:
            break
    try:
        archivepath = values['archive']
        dest_dir = values['folder']
        extract_archive(archivepath, dest_dir)
        window['output'].update('Extraction completed!')
    except FileNotFoundError:
        sg.popup('Please select a valid archive and destination folder.',
                 font='Helvetica')

window.close()


