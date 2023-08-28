print ('enna da venum?')

poss = ['yes','aama','kandippa','venum']

while True:
    a = input('Sollu da ')

    if 'time' in a:
        import mytime
        mytime.tiime()
        

    elif 'date' in a:
        import mytime
        mytime.tooday()

    elif 'task' in a or 'code' in a:
        print("Task ennanu sollu da......")
        try:
            import writecode
        except:
            print('Thappu pannitom pola !')
            

    elif 'file' in a:
        print("Irru paakuren.......")
        import myfiles
    print('control na eduthuten')
    a = input('Vera ethavathu venuma?')
    if not (a in poss):
        break
