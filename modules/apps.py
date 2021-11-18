import subprocess

applications = [{"name" : "steam",  "filepath" : "C:\Program Files (x86)\Steam\steam.exe"},
                {"name" : "calculator",  "filepath" : "calc.exe"}]

def OpenApp(text):
    
    for index in applications:
        if index["name"] in text:
            try:
                subprocess.call(index["filepath"])
                return "opening" + index["name"]
            except:
                return "There has been a problem opening that application."

    return "I''m sorry. I do no know of that application"