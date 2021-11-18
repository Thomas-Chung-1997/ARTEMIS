import pywhatkit as whatKit

def GoogleSearch(text):
    try:
        whatKit.search(text)
    except:
        return ("Sorry. I was unable to do that.")

    return "Searching " + text