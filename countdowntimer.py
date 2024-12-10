import time
from tkinter import Tk, Label, Entry, Button

def start_countdown():
    try:
        # Get the input time in seconds
        total_seconds = int(entry.get())
        while total_seconds >= 0:
            # Calculate minutes and seconds
            mins, secs = divmod(total_seconds, 60)
            # Format the time as MM:SS
            timer = f"{mins:02d}:{secs:02d}"
            # Update the label with the timer
            label.config(text=timer)
            root.update()
            time.sleep(1)
            total_seconds -= 1
        label.config(text="Time's up!")
    except ValueError:
        label.config(text="Invalid input! Please enter an integer.")

# Create the GUI window
root = Tk()
root.title("Countdown Timer")
root.geometry("300x150")

# Create and position widgets
label = Label(root, text="Enter time in seconds:", font=("Helvetica", 14))
label.pack(pady=10)

entry = Entry(root, width=10, font=("Helvetica", 14), justify="center")
entry.pack(pady=10)

start_button = Button(root, text="Start Countdown", command=start_countdown, font=("Helvetica", 14))
start_button.pack(pady=10)

# Run the application
root.mainloop()

