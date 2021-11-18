import wikipedia

def WikipediaSearch(text):
    try:
        search = wikipedia.search(text)
        
        summary = wikipedia.summary(title = search[0], auto_suggest= "false")
        
        return summary.split("\n")[0]
    except Exception as e:
        return (f"sorry I was unable to find the wikipedia page for {text}")