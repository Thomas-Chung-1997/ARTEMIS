import threading
import re
import winsound

def Sleeper():
    winsound.Beep(1500, 400)

def Timer(text):
    regex = "(\d+ (?:second|hour|minute)| (?:second|hour|minute))"
    dic = {"hour": 0, "minute": 0,"second": 0}
    time = 0
    message = "Starting Timer for "
    
    for i in re.findall(regex,text):
        for key in dic.keys():
            if key in i:
                dic[key] = 1
                
                number = re.search("\d+",i)
                
                if number is not None:
                    dic[key] = int(number.group())
    
    time += dic["second"]
    time += dic["minute"] * 60
    time += dic["hour"] * 60 * 60
    
    if time == 0:
        return "Sorry I could not start a timer."
    
    for key in dic:
        if dic[key] > 1:
            message += f"{dic[key]} {key}s "
        elif dic[key] > 0:
            message += f"{dic[key]} {key} "
    
    timerThread = threading.Timer(time, Sleeper)
    timerThread.start()
    
    return message