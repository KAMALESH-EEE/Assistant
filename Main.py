from TextVoice import voice,speech
import myfiles, myweb,Rem,mypages
from speech_mail import MS
print ('Staring')
speech('I am ARC, I am ready, sir')

poss = ['bye','thank you','I will catch you later']

while True:
    print('M')
    a=''
    try:
        a=voice()
        if 'wait' in a:
            print("Waiting....... for your comand")
            speech("Okay sir, I am Waiting")
            input()

        elif 'time' in a:
            import mytime
            i=mytime.tiime()
            print(i)
            speech(i)

        elif 'date' in a:
            import mytime
            i=mytime.tooday()
            print(i)
            speech(i)

        

        elif 'file' in a:
            print("Name")
            speech("name")
            myfiles.get_file(voice())
        
        elif 'search' in a:
            myweb.get_data(voice())
        
        elif 'link' in a:
            myweb.find_url()
        
        elif 'planner' in a:
            if 'add' in a:
                Rem.ADD()
            if 'any work' in a:
                Rem.check_Date()
            elif 'all my work' in a:
                Rem.showAll()
                
        elif 'mail' in a:
            MS.mailwrite()
            input()
        
        elif 'page' in a:
            mypages.page()

        elif 'task' in a or 'code' in a:
            print("Task ennanu sollu da......")
            import writecode
            del writecode
            
        elif ('good' in a) or ('amazing'in a):
            speech("thank you, Sir.")
        elif ('who are you' in a):
            speech('I am, ARC,( Assistant for Reconizing the Commands)\n Mr Kamalesh was found me')
    except:
        print('Can\'t Access')
        speech("Can't Access")
    if (a in poss):
        break
    
speech("okay, bye sir, Have a nice day")