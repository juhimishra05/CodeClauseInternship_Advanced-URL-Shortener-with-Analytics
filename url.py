import pyperclip
import pyshorteners
from tkinter import *

# Initialize the Tkinter GUI
gui = Tk()
gui.geometry("400x200")
gui.title("URL Shortener")
gui.configure(bg="#49A")

# Create StringVar to hold the URL values
url = StringVar()
url_address = StringVar()

def urlshortener():
    try:
        urladdress = url.get().strip()  # Get the URL from the input field and strip extra spaces
        if urladdress == "":  # Check if the URL is empty
            url_address.set("Please enter a valid URL!")
        else:
            # Create a Shortener instance and shorten the URL
            shortener = pyshorteners.Shortener()
            url_short = shortener.tinyurl.short(urladdress)
            url_address.set(url_short)  # Set the shortened URL in the output field
    except Exception as e:
        url_address.set(f"Error: {str(e)}")  # Show error message in the output field

def copyurl():
    url_short = url_address.get()  # Get the shortened URL
    if url_short:  # Check if the URL is not empty
        pyperclip.copy(url_short)  # Copy the shortened URL to the clipboard

# Label at the top of the window
Label(gui, text="My URL Shortener", font="poppins").pack(pady=10)

# Entry widget for URL input
Entry(gui, textvariable=url).pack(pady=5)

# Button to generate shortened URL
Button(gui, text="Generate Short URL", command=urlshortener).pack(pady=7)

# Entry widget to show the shortened URL
Entry(gui, textvariable=url_address).pack(pady=5)

# Button to copy the shortened URL to clipboard
Button(gui, text="Copy URL", command=copyurl).pack(pady=5)

# Run the GUI loop
gui.mainloop()
