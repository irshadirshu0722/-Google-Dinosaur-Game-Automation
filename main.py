import pyautogui
import time
import keyboard

while True:
    im = pyautogui.screenshot()
    screen = im.getpixel((1080,350))
    b1 = im.getpixel((480, 710))
    b2 = im.getpixel((503, 710))
    b3 = im.getpixel((523, 710))
    b4 = im.getpixel((543, 710))
    b5 = im.getpixel((663, 710))
    b6 = im.getpixel((583, 710))






    m1 = im.getpixel((480, 608))
    m2 = im.getpixel((503, 608))
    m3 = im.getpixel((523,608))
    m4 = im.getpixel((583, 608))

    if screen[0]==255:
        if b1[0]!=255 or b2[0]!=255 or b3[0]!=255 or b4[0]!=255 or  b5[0]!=255 or b6[0]!=255 or  m1[0]!=255 or m2[0]!=255 or m3[0]!=255 or m4[0]!=255 :
            pyautogui.press("space")
            time.sleep(0.00001)
    else:
        if b1[0]>=40 or b2[0]>=40 or b3[0]>=40 or b4[0]>=40 or  b5[0]>=40  or b6[0]>=40 or m1[0]>=40 or m2[0]>=40 or m3[0]>=40or m4[0]>=40   :
            pyautogui.press("space")
            time.sleep(0.00001)
    if keyboard.is_pressed("s"):
        break




