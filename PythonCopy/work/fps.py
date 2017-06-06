
# -*- coding:utf-8 -*-
#編集環境ををutf-8にする

#######################################################################################
# ProjectName   : fpsプログラム
# FileName      : fps.py
# Name          : 木村雅椰
# Year,month,day: 2017,02,21
#
#comment        :
#
#######################################################################################

#######################################################################################
# import
#######################################################################################
import os
import sys          #システムパラメータpackage
import time         #time
#from datetime import timedelta
import datetime
#######################################################################################

#######################################################################################
# define
#######################################################################################
#MAX_NUMBER = 5
#######################################################################################

#######################################################################################
# Class
#######################################################################################

#######################################################################################
# GlobalVariable
#######################################################################################
global g_fps
g_fps = 0.0


def Init():
    print("Init_phase")
    return None

def Uninit():
    print("Uninit_phase")
    return None

def Update():
    print("Update_phase")
    return None

def Draw():
    print("Draw_phase")
    return None
#######################################################################################
# 関数名 : main()
# 返り値 : なし
# 説明　 : main関数
#
#######################################################################################
def main():
    
    dwFrameCount = dwCurrentTime = 0.0

    dwExecLastTime = dwFPSLastTime = time.time()#time.clock()
    print(dwExecLastTime)
    Init()    

    while (True) :
        dwCurrentTime = time.time()#time.clock()#
        if ((dwCurrentTime - dwFPSLastTime) <= 500):
            #ナンヤカンヤ
            try :
                g_fps = (dwFrameCount * 1) / (dwCurrentTime - dwFPSLastTime) 
                dwFPSLastTime = dwCurrentTime
                dwFrameCount = 0
            except ZeroDivisionError:
                continue
                



        if ((dwCurrentTime - dwExecLastTime) <= (1000/60)):
            dwExecLastTime = dwCurrentTime 
            Update()
            Draw()
            print("FPS : " + str(g_fps))
            dwFrameCount += 1
            #os.system("cls")
            
            
    Uninit()

    
    time.sleep(10)

    return 0

#######################################################################################
if __name__ == "__main__":
        sys.exit(main())
