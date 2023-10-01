from datetime import datetime,date
def tooday():
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    return "todate:"+ d1

def tiime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return "Time is, "+current_time

