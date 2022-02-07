import keyboard
import time
import win32api, win32con
from pyautogui import *
import pyautogui

#X:  635 Y:  400 RGB: (  0,   0,   0)  	tiles 1
#X:  535 Y:  400 RGB: (  0,   0,   0)	tiles 2
#X:  735 Y:  400 RGB: (  0,   0,   0)	tiles 3
#X:  810 Y:  400 RGB: (  0,   0,   0)	tiles 4
def click(a):
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	if a < 12:
		time.sleep(0.03)
	elif a < 30 and a >=12:
		time.sleep(0.8)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	print(a)

a = 0
while True:
	if pyautogui.pixelMatchesColor(635, 400, (  0,   0,   0)): 
		pyautogui.moveTo(635, 400)
		click(a)
		a+=1
	elif pyautogui.pixelMatchesColor(535, 400, (  0,   0,   0)):
		pyautogui.moveTo(535, 400)
		click(a)
		a+=1
	elif pyautogui.pixelMatchesColor(735, 400, (  0,   0,   0)):
		pyautogui.moveTo(735, 400)
		click(a)
		a+=1
	elif pyautogui.pixelMatchesColor(810, 400, (  0,   0,   0)):
		pyautogui.moveTo(810, 400)
		click(a)
		a+=1
	elif keyboard.is_pressed('q'):  # if key 'q' is pressed 
		break