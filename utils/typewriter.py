import sys
import time
import msvcrt

def typewriter(text, delay=0.035):
    """Print text one character at a time. Press Enter to skip."""
    i = 0
    length = len(text)
    
    while i < length:
        # If a key is pressed
        if msvcrt.kbhit():
            key = msvcrt.getch()
            # If it's Enter (b'\r'), print the rest immediately
            if key == b'\r':
                sys.stdout.write(text[i:])
                sys.stdout.flush()
                break

        sys.stdout.write(text[i])
        sys.stdout.flush()
        time.sleep(delay)
        i += 1

    print()  # newline at the end