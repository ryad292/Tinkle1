import os
import subprocess
import platform
import pyautogui
import requests
import psutil

class TinkleSkills:
    @staticmethod
    def execute(command, speak_func):
        command = command.lower()
        
        # نظام التحكم بالجهاز
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
                
        # نظام الرؤية ولقطات الشاشة
        elif "take screenshot" in command or "خذ لقطة للشاشة" in command:
            speak_func("Capturing screen, doctor.")
            screenshot = pyautogui.screenshot()
            screenshot.save("tinkle_screen.png")
            speak_func("Screenshot saved successfully.")
            
        # نظام الأداء ومعلومات الجهاز
        elif "system status" in command or "حالة النظام" in command:
            cpu = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory().percent
            speak_func(f"CPU usage is at {cpu} percent, and Memory usage is at {memory} percent.")
            
        # تخصيص الواجهة والألوان
        elif "change color red" in command:
            speak_func("Changing interface color to red.")
            return "#ff0033"
        elif "change color blue" in command:
            speak_func("Changing interface color to blue.")
            return "#00ffcc"
        elif "change color gold" in command:
            speak_func("Changing interface color to gold.")
            return "#ffcc00"
            
        else:
            speak_func("Executing command, doctor.")
            
        return None
