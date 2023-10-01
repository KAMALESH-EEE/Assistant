from TextVoice import *
def get_file(getname):
    
    getname = 'Assistant/'+getname
    try:
        gotfile = open(getname,'r')
        contants = gotfile.readlines()
        for i in contants:
            print (i)
            speech(i)
    except:
        print('File illa !')
    
