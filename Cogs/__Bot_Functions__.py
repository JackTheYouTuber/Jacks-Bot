import random
from Cogs import __Functions__

Command_Prefix = "!"

Logger_Addon = __Functions__.append_file
Current_Time = __Functions__.get_time


def Log(Log_Text:str="Test"):
    Log_Message = f"\n[{Current_Time()}]\n{Log_Text}"
    Logger_Addon("Discord Log.txt", Log_Message, True)

def Command(Message_Text:str, Message_Author:str, Message_Channel:str):
    if Message_Text[0] == Command_Prefix:
        if Message_Text == Command_Prefix + "random":
            return random.randint(1, 9999)
    else:
        return
