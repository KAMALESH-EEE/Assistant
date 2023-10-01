from TextVoice import speech, voice
import webbrowser
import pyperclip
class MS:
    cont=[]    
    def text():
        try:
            t=voice()
            return t
        except:
            print('Re_Try')
            return MS.text()

    def details():
        speech('For Who?')
        print('For Who?')
        
        MS.cont.append("From:\n\tR KAMALESH\n")
        ta = voice()
        MS.cont.append("To:\n\t"+ta+'\n')
        MS.cont.append('Respected: Sir/Madam\n\t')
        speech("Subject")
        ta=voice()
        MS.cont.append('Sub:'+ta+'-reg.\n')

    def WriteMail():
        tex='\t'
        while True:
            
            ta=MS.text()
            
            if (ta.lower() =='end') or (ta.lower() =='e n d'):
                MS.cont.append(tex)
                break
            elif ta.lower()=='new line':
                tex+='\n'
                MS.cont.append(tex)
                tex='\t'
            elif ta.lower() == 'show':
                print(tex)
            else:
                tex+=ta
                tex+='. '
        MS.cont.append('\n\t\t\t Thank You.\n')
    def mailwrite():
        MS.details()
        MS.WriteMail()
        fil=open('email.txt','w')
        fil.writelines(MS.cont)
        fil.close()
        fil=open('email.txt','r')
        MS.cont=fil.readlines()
        mail=''
        for i in MS.cont:
            print(i)
            speech(i)
            mail+=i
        speech("opening mail")
        pyperclip.copy(mail)
        webbrowser.open_new_tab('https://mail.google.com/mail/u/0/?ogbl#inbox?compose=new')
