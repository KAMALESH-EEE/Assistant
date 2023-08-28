def get_file():
    getname = input()
    getname = 'Assistant/'+getname
    try:
        gotfile = open(getname,'r')
        contants = gotfile.readlines()
        for i in contants:
            print (i)
    except:
        print('File illa !')
get_file()