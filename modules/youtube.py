import pywhatkit as whatKit

def YoutubeSearch(text):
    try:
        whatKit.playonyt(text)
    except:
        return ("Sorry. I was unable to do that.")

    return "Playing " + text