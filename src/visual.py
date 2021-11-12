from colorama.ansi import clear_screen
import piglow
import os
from colorama import Fore

led_All = piglow.all
led_Set = piglow.set
redL = [1, 7, 13]
orangeL = [2, 8, 14]
yellowL = [3, 9, 15]
blueL = [5, 11, 17]
whiteL = [6, 12, 18]
terminalCol = os.get_terminal_size().columns
terminalLin = os.get_terminal_size().lines

def print_term_size():
    print(f"{terminalLin} lines, {terminalCol} cols")
    
def display_alert(severity):
    match severity:
        case "SEVERE":
            col1 = Fore.RED
            col2 = Fore.LIGHTRED_EX
        case "WARNING":
            col1 = Fore.LIGHTRED_EX
            col2 = Fore.LIGHTYELLOW_EX
        case "MILD":
            col1 = Fore.LIGHTYELLOW_EX
            col2 = Fore.BLUE
        case "NOTICE":
            col1 = Fore.BLUE
            col2 = Fore.WHITE
        case _:
            print("something isn't right, fix it NOW.") 
    print(
        f'''
        {col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█{col1}▚{col2}█
        {col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓{col2}▞{col1}▓
        '''
        )
    