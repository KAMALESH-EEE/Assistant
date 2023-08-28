from datetime import datetime,date
def tooday():
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    print("Innaki date:", d1)

def tiime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Ippa Time ", current_time)
    print('Ippa nalla neram')