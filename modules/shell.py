from ppadb.client import Client as adbClient
from colorama import *
import time
import os

def shellclient():
    try:
        serial = input(f"{Fore.MAGENTA}Insert Device Serial: {Fore.RESET}")
        client = adbClient(host="127.0.0.1", port=5037)
        device = client.device(serial)

        if device is None:
            print(f"{Fore.LIGHTRED_EX}Error: Device 'emulator-5554' not found. Please check the device connection.{Fore.RESET}")
            time.sleep(2)
            os.system("python main.py")
        while True:
            try:
                query = input(f"{Fore.MAGENTA}Nebula> {Fore.RESET}")

                if query.lower() == "help":
                    print(f"""
{Fore.YELLOW}[+] Here are some preset commands [+]
{Fore.LIGHTBLACK_EX}shutdown - to turn off the device
recovery - to reboot the device into recovery{Fore.RESET}""")


                elif query.lower() == "exit":
                    print(f"{Fore.YELLOW}[+] You are logged out [+]{Fore.RESET}")
                    time.sleep(2)
                    os.system("python main.py")

                
                elif query.lower() == "shutdown":
                    device.shell("reboot -p")

                elif query.lower() == "recovery":
                    device.shell("reboot recovery")
                    print(f"{Fore.LIGHTBLACK_EX}Device restarting in recovery mode.{Fore.RESET}")
                
                else:
                    output = device.shell(query)
                    print(f"{Fore.LIGHTBLACK_EX}{output}{Fore.RESET}")

            except Exception as shell:
                print(f"{Fore.LIGHTRED_EX}ERROR: {shell}{Fore.RESET}")
                time.sleep(2)
                os.system("python main.py")
            
    except Exception as a:
        print(f"{Fore.LIGHTRED_EX}ERROR: {a}{Fore.RESET}")       