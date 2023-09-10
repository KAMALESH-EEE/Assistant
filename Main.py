print ('enna venum?')

poss = ['No','vena','no','nope']

while True:
    a = input('M: ')

    try:
        if 'time' in a:
            import mytime
            mytime.tiime()
            

        elif 'date' in a:
            import mytime
            mytime.tooday()

        elif 'task' in a or 'code' in a:
            print("Task ennanu sollu da......")
            import writecode
            writecode.w_code()

        elif 'file' in a:
            print("Irru paakuren.......")
            import myfiles
            myfiles.get_file()
        
        elif 'web' in a:
            import myweb
            myweb.web()
    except:
        print('Can\'t Access')

    a = input('Vera ethavathu venuma?')
    if (a in poss):
        break
