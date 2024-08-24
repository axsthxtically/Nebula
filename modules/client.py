from ppadb.client import Client as adbClient
from colorama import *


def clientinfo():
    try:
        client = adbClient(host="127.0.0.1", port=5037)
        devices = client.devices()
        if devices:
            print(f"{Fore.LIGHTGREEN_EX}[+] Connected Device [+]{Fore.RESET}")
        for device in devices:
            device_name = device.shell("getprop ro.product.model")
            if device_name:
                print(f"""{Fore.LIGHTBLACK_EX}Device: {Fore.MAGENTA}{device_name.strip()}{Fore.RESET} | {Fore.RESET}{Fore.LIGHTBLACK_EX}Serial: {Fore.MAGENTA}{device.serial}{Fore.RESET}""")
            else:
                print(f"{Fore.LIGHTBLACK_EX}Device: {Fore.MAGENTA}{None}{Fore.RESET} | {Fore.LIGHTBLACK_EX}Serial: {Fore.MAGENTA}{device.serial}{Fore.RESET}")
    except Exception as a:
        print(f"{Fore.LIGHTRED_EX}Error: Impossible Connection with Device {a}{Fore.RESET}")