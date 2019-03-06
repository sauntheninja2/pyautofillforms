import webbrowser
import pyautogui
import os
webbrowser.open('') //the url of the form
pyautogui.moveTo(968,100)
for i in range(50,200): 
                   pyautogui.rel(None,1) 
                   pyautogui.write("") //Whatever you want to fill
                   pyautogui.click(button="left")
exit()
