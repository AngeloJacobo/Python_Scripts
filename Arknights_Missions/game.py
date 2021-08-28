import pytesseract
import pyautogui
from PIL import Image, ImageGrab
import re
import time
import keyboard

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pyautogui.FAILSAFE=False

#CONFIGURE
start_coord=(1627,900,1737,948)
mission_coord=(1470,700,1644,811)
result_coord=(148,825,519,940)
start_click=(1693,931)
mission_click=(1555,774)
result_click=(1692,677)

abs_path='E:/Desktop/images/'


#Start of Script
print('Start script for automating game.......\n')
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print(0,'\n')

count=1
while True: 
    if keyboard.is_pressed('enter'):
        print('\n\nClosing script.....')
        exit()

    #screenshot and save a part of the screen
    im_start=ImageGrab.grab(bbox=start_coord)
    im_mission=ImageGrab.grab(bbox=mission_coord)
    im_result=ImageGrab.grab(bbox=result_coord)
    im_start.save(abs_path+'im_start.png')
    im_mission.save(abs_path+'im_mission.png')
    im_result.save(abs_path+'im_result.png')

    #OCR the save the images
    text_start = pytesseract.image_to_string(Image.open(abs_path+'im_start.png'))
    text_mission = pytesseract.image_to_string(Image.open(abs_path+'im_mission.png'))
    text_result = pytesseract.image_to_string(Image.open(abs_path+'im_result.png'))
    text_start=text_start.lower()
    text_start=re.findall('.*start.*',text_start)
    text_mission=text_mission.lower()
    text_mission=re.findall('.*mission.*',text_mission)
    text_result=text_result.lower()
    text_result=re.findall('.*result.*',text_result)

    #condition for left-clicking the mouse
    if len(text_start)!=0: 
        print('round'+str(count)+': START')
        pyautogui.click(start_click)
    elif len(text_mission)!=0:
        print('round'+str(count)+': MISSION START')
        pyautogui.click(mission_click)
    elif len(text_result)!=0:
        print('round'+str(count)+': RESULTS')
        count=count+1
        pyautogui.click(result_click)
        time.sleep(1)

