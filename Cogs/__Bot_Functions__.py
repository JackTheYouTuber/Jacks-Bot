from Cogs import __Functions__

Logger_Addon = __Functions__.append_file
Current_Time = __Functions__.get_time

def Log(Log_Text:str="Test"):
    Log_Message = f"\n[{Current_Time()}]\n{Log_Text}"
    Logger_Addon("Discord Log.txt", Log_Message, True)

if __name__ == "__main__":
    Log()
