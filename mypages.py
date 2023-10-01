import webbrowser
from TextVoice import voice,speech

def goto(url):
    webbrowser.open_new_tab(url)
    input()

def page():
    speech('What page')
    a=voice()
    if 'mail' in a:
        t='https://mail.google.com/mail/u/0/?ogbl#inbox'
    elif 'GitHub'in a:
        t='https://github.com/KAMALESH-EEE'
    elif 'drive' in a:
        t = 'https://drive.google.com/drive/u/0/my-drive'
    elif 'YouTube' in a:
        t = 'https://www.youtube.com/'

    goto(t)
