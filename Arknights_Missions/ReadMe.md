# About:
Arknights has an autodeploy feauture in supply missions. Click "Start", click "Mission Start", wait for the battle to end then click anywhere to go back to "Start" button. To make these steps automated, the script "game.py" will control the mouse to repeatedly do the missions without having me to watch and wait for the whole battle to end. Click "Enter" for 2 to 3 seconds to close the script.

The python script will use PIL to grab the part of the screen where the texts "Start","MISSION START", and "Results"(after battle) can be found. These images will be saved and used by pytesseract to recognize the texts on it. If either of the texts are recognized, it will use pyautogui to click on the part of the screen where that text can be found.

# Sequence:
![start](https://user-images.githubusercontent.com/87559347/131210329-8b7d46a2-577d-45e1-ba59-9e4ec9e0f91f.png)
![mission](https://user-images.githubusercontent.com/87559347/131210333-e40f5317-4fd2-4a37-862c-7095ed347b6d.png)
![result](https://user-images.githubusercontent.com/87559347/131210337-b91b7e92-8e2d-4077-93a3-47ad9fe6702b.png)

# Configure [default is for 1920x1080 Screen]:  
* start_coord = location of the "Start" button (left_x,top_y,right_x,down_y)  
* mission_coord = location of the "MISSION START" button (left_x,top_y,right_x,down_y)  
* result_coord = location of the "Results" text (left_x,top_y,right_x,down_y)  
* start_click = center coordinate of "Start" button (x,y)  
* mission_click = center coordinate of "MISSION START" button (x,y)  
* result_click = any coordinates (x,y)  
* abs_path = directory where grabbed images can be safely saved  

# Install: 
* Download and install [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
* Open cmd prompt at the same directory as *requirements.txt* then run:  
`pip install -r requirements.txt`
* To start the script, open cmd prompt at the same directory as *game.py* then run:  
`python game.py`
