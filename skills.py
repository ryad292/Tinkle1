import os
import subprocess
import platform

def execute_command(command, speak_func):
    command = command.lower()
    
    # أوامر التحكم بالبرامج والنظام
    if "open notepad" in command or "افتح المفكرة" in command:
        speak_func("Opening Notepad, doctor.")
        if platform.system() == "Windows":
            os.system("notepad")
        else:
            speak_func("Notepad is only available on Windows.")
            
    elif "open browser" in command or "افتح المتصفح" in command:
        speak_func("Opening browser, doctor.")
        if platform.system() == "Windows":
            os.system("start chrome")
        elif platform.system() == "Darwin":
            os.system("open -a 'Google Chrome'")
        else:
            os.system("google-chrome")
            
    elif "shutdown system" in command or "إيقاف التشغيل" in command:
        speak_func("Shutting down the system, doctor.")
        if platform.system() == "Windows":
            os.system("shutdown /s /t 1")
        else:
            os.system("sudo shutdown now")
            
    elif "change color red" in command:
        speak_func("Changing interface color to red.")
        return "#ff0033"
        
    elif "change color blue" in command:
        speak_func("Changing interface color to blue.")
        return "#00ffcc"
        
    else:
        speak_func("Command executed, doctor.")
    
    return None
