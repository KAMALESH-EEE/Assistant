from datetime import datetime,date,timedelta
from TextVoice import *

def put(name,Time):
    fil = open('rem.txt','r')
    things = fil.readlines()
    fil.close()
    ti=things[0]
    ti=ti[0:len(ti)-1]+ name+',\n'
    things[0]=ti
    ti=name+'_'+Time+'_\n'
    things.append(ti)
    fil = open('rem.txt','w')
    fil.writelines(things)
    fil.close()
    return 'I catch,'
    
def get(i):
    f=[]
    fil = open('rem.txt','r')
    things = fil.readlines()
    fil.close()
    return things[i+1].split('_')

def Set(name,d):
    t=datetime.now().date()+timedelta(days=d)
    return put(name,t.strftime("on %Y-%m-%d at %H:%M"))

def when(name):
    fil = open('rem.txt','r')
    things = fil.readline().split(',')
    fil.close()
    
    if name in things:
        t=get(things.index(name))
        info=t[0]+', '+t[1]
        info=info.strip()
        print(info)
        speech(info)
    else :
        print('No thing found')
        speech('No thing found')

def get_Date():
    
    speech('When')
    date_string=voice()
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    words = date_string.split(' ')
    if date_string == 'today':
        return datetime.now().date().strftime("on %Y-%m-%d")
    elif date_string == 'tomorrow':
        return (datetime.now().date()+ timedelta(days=1)).strftime("on %Y-%m-%d at %H:%M")
    elif 'after' in date_string:
        if 'days' in date_string:
            t=date_string.split(' ')
            k=int(t[1])
            return (datetime.now().date()+ timedelta(days=k)).strftime("on %Y-%m-%d at %H:%M")
        
        elif 'weeks' in date_string:
            t=date_string.split(' ')
            k=int(t[1])
            return (datetime.now().date()+ timedelta(weeks=k)).strftime("on %Y-%m-%d at %H:%M")
    try:
        if 'at' in words:
            t=words[4].split(':')
            h=t[0]
            m=t[1]
        h='6'
        m='0'
        day = words[0]
        month = words[1]
        year = words[2]
        month_number = months.index(month) + 1
        formatted_date = datetime(int(year), month_number, int(day),int(h),int(m)).strftime("on %Y-%m-%d at %H:%M")
        return formatted_date
    except:
        print('re Try')
        return get_Date()

def ADD():
    print('Name')
    speech('Item name')
    t=voice()
    if 'I ' in t:
        t='You '+t[1::]
    speech(put(t,get_Date()))
    when(t)

def check_Date():
    t=get_Date().split(' ')
    d=t[1]
    fil = open('rem.txt','r')
    things = fil.readlines()
    fil.close()
    th=[]
    for i in things:
        if '_on ' in i:
            t=i.split('_on ')
            c=t[1]
            cd=c.split(' ')
            if(cd[0]==d):
                th.append(t[0])
    if len(th) ==0:
        speech("You are a busy sleeping engineer")
    else:
        speech(str(len(th))+',Works you have')
        for i in th:
            print(i)
            speech(i)
        speech("That all, sir")

def showAll():
    fil = open('rem.txt','r')
    things = fil.readline().split(',')
    fil.close()
    for i in things:
        try:
            when(i)
        except:
            speech('That All, Sir.')
