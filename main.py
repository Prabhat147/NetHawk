import tkinter as tk
from tkinter import ttk  # Import ttk for modern widgets
import speedtest  # Install using `pip install speedtest-cli`
import threading

def perform_speed_test():
    """Executes a speed test and returns results as a dictionary."""
    try:
        s = speedtest.Speedtest()
        s.download()
        s.upload()
        return {
            "download": round(s.results.download / 10**6, 2),  # Mbps
            "upload": round(s.results.upload / 10**6, 2),  # Mbps
            "ping": s.results.ping
        }
    except Exception as e:
        print(f"Error: {e}")
        return None

def update_results(results):
    """Updates the UI with the latest speed test results."""
    if results:
        download_label.config(text=f"Download: {results['download']} Mbps")
        upload_label.config(text=f"Upload: {results['upload']} Mbps")
        ping_label.config(text=f"Ping: {results['ping']} ms")
    else:
        download_label.config(text="Download: -")
        upload_label.config(text="Upload: -")
        ping_label.config(text="Ping: -")

def run_speed_test_in_thread():
    """Runs the speed test in a separate thread and updates the UI."""
    results = perform_speed_test()
    # Update UI with results in the main thread
    root.after(0, update_results, results)  # Schedule update on main thread

# Create the main window
root = tk.Tk()
root.title("Wi-Fi Speed Monitor")

# Beige:  #d9c0a3
# Earth brown:  #593c22
# Dark tan:  #a67b56
# Light grey:   #f2f2f2
# Almost black:  #0d0d0d

# Configure background color for a modern look
root.configure(bg="#d9c0a3")  # Light blue background

# Create a frame to hold the labels and button
content_frame = ttk.Frame(root, padding=20)  # Use ttk.Frame for padding
content_frame.pack()

# Create download speed label (using ttk.Label)
download_label = ttk.Label(content_frame, text="Download: - Mbps",
                           foreground="#593c22", font=("Arial", 18, "bold"))
download_label.pack(pady=10)

# Create upload speed label
upload_label = ttk.Label(content_frame, text="Upload: - Mbps",
                         foreground="#593c22", font=("Arial", 18, "bold"))
upload_label.pack(pady=10)

# Create ping label
ping_label = ttk.Label(content_frame, text="Ping: - ms",
                       foreground="#593c22", font=("Arial", 18, "bold"))
ping_label.pack(pady=10)

# Create a stylish button with rounded corners (ttk.Button)
# Custom style is defined in a separate styles.tcl file (optional)
# See https://wiki.tcl.tk/39144 for creating styles.tcl

# Start speed test in a separate thread when the button is clicked
run_button = ttk.Button(content_frame, text="Run Speed Test",  # Use content_frame here
                       command=run_speed_test_in_thread, style="my.TButton")
run_button.pack(pady=20)


# Run the speed test and display results immediately (commented out)
# This is replaced by threaded approach for live updates
# initial_results = perform_speed_test()
# display_results(initial_results)

# Run the main event loop
root.mainloop()
