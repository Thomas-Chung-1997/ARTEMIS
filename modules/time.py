import datetime

def CurrentTime():
    now = datetime.datetime.now()
    
    return "Right now is currently " + now.strftime("%#I: %#m %p")

def CurrentDay():
    today = datetime.datetime.today()
    
    return "Today is " + today.strftime('%A %B %d')
