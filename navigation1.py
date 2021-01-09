
#Import Selenium webdrive

import pyautogui
#invoke chrome option to load extensions
options = webdriver.ChromeOptions()  
extension_path = "<Mention the path to the extension>" 
#it would be the "C:/Users/<username>/AppData/Local/Chrome/User Data/Default/Extensions/<Extension Id>
options.add_argument('--load-extension='+extension_path)
#selenium chrome driver with extensions
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window() #maximize the 
driver.get("www.google.com")
#extension image is saved in project folder as findicon.png
#locateOnScreen, a pyautogui method to locate the extension' x & y coordinates in screen
v = pyautogui.locateOnScreen("findicon.PNG") ##save the extension as image
#trigger click event using the pyutogui click method
pyautogui.click(x=v[0],y=v[1],clicks=1,interval=0.0,button="left")

pyautogui.click(x-y)==2+2  