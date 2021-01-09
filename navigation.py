## Opening Google
import webbrowser
a = input()
b = input()
if a == "Open Google":
    openchrome= 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(openchrome).open(b)