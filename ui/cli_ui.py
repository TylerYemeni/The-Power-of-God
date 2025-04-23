import time
import sys

def show_banner():
    banner = """
    ██████╗  ██████╗ ██╗    ██╗███████╗ ██████╗ ██████╗ 
    ██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔═══██╗██╔══██╗
    ██████╔╝██║   ██║██║ █╗ ██║█████╗  ██║   ██║██████╔╝
    ██╔═══╝ ██║   ██║██║███╗██║██╔══╝  ██║   ██║██╔═══╝ 
    ██║     ╚██████╔╝╚███╔███╔╝███████╗╚██████╔╝██║     
    ╚═╝      ╚═════╝  ╚══╝╚══╝ ╚══════╝ ╚═════╝ ╚═╝     
        The Power of God - WhatsApp Destroyer
    """
    print(banner)

def loading_animation(text):
    print(text, end='', flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print('.', end='', flush=True)
    print('')
