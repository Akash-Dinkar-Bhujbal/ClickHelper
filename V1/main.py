from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, Key
import time

# Initialize the mouse controller
mouse = Controller()

# Define the interval (in seconds)
INTERVAL = 90  # Change this to 30, 60, or any other value

# Global variables
running = True  # Flag to control the program
esc_press_count = 0  # Counter for Esc key presses
click_count = 0  # Counter for mouse clicks

# Function to handle key presses
def on_press(key):
    global running, esc_press_count
    if key == Key.esc:  # Increment counter on Esc key press
        esc_press_count += 1
        print(f"Esc key pressed {esc_press_count} time(s).")
        if esc_press_count >= 3:  # Exit after 3 presses
            running = False
            print("Esc key pressed 3 times. Exiting program...")
            return False  # Stop the listener

# Function to perform clicks with periodic checks
def perform_clicks():
    global running, click_count
    try:
        while running:
            # Increment and print the click counter
            click_count += 1
            mouse.click(Button.left, 1)
            # print(f"Click performed: {click_count}")  # Print click count
            print(click_count)  # Print click count
            
            # Wait for the specified interval
            for _ in range(INTERVAL):
                if not running:  # Check for exit signal
                    return
                time.sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Program exited. Listener stopped.")

# Main program loop
while True:
    running = True  # Reset the running flag
    print("Starting the program... Press Esc 3 times to exit.")
    
    # Start the keyboard listener
    with Listener(on_press=on_press) as listener:
        perform_clicks()  # Start the click loop
        listener.join()  # Ensure listener stops properly
    
    if not running:  # Break the loop if Esc was pressed 3 times
        print("Program terminated by user.")
        break
