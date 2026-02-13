import pynput.keyboard

def process_key_press(key):
    print(key)

keyboard_listner = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listner:
    keyboard_listner.join()