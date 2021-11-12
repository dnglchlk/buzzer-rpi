from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import sys
import time
from pygame import mixer
from colorama import Fore
from colorama import Style
import visual
from multiprocessing import Process



def help_print():
    print(
        f''' {Fore.GREEN}
            ========================================
            |                                      |
            |              {Fore.WHITE}Buzzer Help{Fore.GREEN}             |
            |                 {Fore.WHITE}Flags:{Fore.GREEN}               |
            |                                      |
            |      --help        Displays Help     |
            |                                      |
            |                                      |
            |                                      |
            |                                      |
            ========================================
        {Fore.RESET}'''
        )
    exit(0)

sevLev = ["NOTICE", "WARNING", "MILD", "SEVERE"]
sevArg = ""


if (len(sys.argv) > 1):
    if (sys.argv[1] == "--help"):
        help_print()
    elif(sys.argv[1] == f"--severity"):
        if (len(sys.argv) > 2):
            if (sys.argv[2] in sevLev):
                sevArg = sys.argv[2]
            else:
                help_print()
        else:
            help_print()

mixer.init()

# Notice 3.22 Secs
def buzzer():
    sound = sevArg
    mixer.music.load(f"sounds/{sound}.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(0.5)


# https://cdn.discordapp.com/attachments/445796144753278986/907470687348879370/iu.png
# Link to PiGlow Diagram
def alarm_display():
    severity = sevArg
    if (severity in sevLev):
        visual.display_alert(severity)
    else: 
        print(
            f''' {Fore.GREEN}
            ========================================
            |                                      |
            |       {Fore.WHITE}Severity Level Incorrect{Fore.GREEN}       |
            |      {Fore.WHITE}Please ensure you pass one:{Fore.GREEN}     |
            |     {Fore.RED}SEVERE  {Fore.LIGHTRED_EX}WARNING  {Fore.LIGHTYELLOW_EX}MILD  {Fore.BLUE}NOTICE{Fore.GREEN}    |
            |                                      |
            ========================================
            {Fore.RESET}'''
            )

if __name__=='__main__':
    p1 = Process(target = buzzer)
    p1.start()
    p2 = Process(target = alarm_display)
    p2.start()



