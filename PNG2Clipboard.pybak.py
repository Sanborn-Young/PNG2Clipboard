import os
import base64
import tkinter as tk
from tkinter import messagebox
from PIL import Image
import pyperclip

# Function to find the latest PNG file in the specified Screenshots folder
def get_latest_screenshot():
    screenshots_folder = os.path.join(os.environ["USERPROFILE"], "OneDrive", "Pictures", "Screenshots")
    
    # Check if the Screenshots folder exists
    if not os.path.exists(screenshots_folder):
        raise FileNotFoundError(f"The folder at {screenshots_folder} does not exist. Please check the path and try again.")
    
    png_files = [f for f in os.listdir(screenshots_folder) if f.endswith(".png")]
    if not png_files:
        raise FileNotFoundError(f"No PNG files found in the Screenshots folder at {screenshots_folder}.")
    
    latest_file = max(png_files, key=lambda f: os.path.getctime(os.path.join(screenshots_folder, f)))
    return os.path.join(screenshots_folder, latest_file)

# Function to convert PNG to WebP
def convert_png_to_webp(png_file):
    try:
        webp_file = os.path.splitext(png_file)[0] + '.webp'
        image = Image.open(png_file)
        image.save(webp_file, 'webp', quality=20, method=6)
        return webp_file
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert {png_file} to WebP: {e}")
        return None

# Function to encode WebP to Base64 and copy to the clipboard
def encode_webp_to_base64(webp_file):
    if webp_file:
        with open(webp_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        clipboard_string = f"![image](data:image/webp;base64,{encoded_string})"
        pyperclip.copy(clipboard_string)
        messagebox.showinfo("Success", "Base64 encoded image saved to Windows Clipboard")
    else:
        messagebox.showerror("Error", "WebP file not found for Base64 encoding.")

# Create the GUI window
root = tk.Tk()
root.title("PNG2Clipboard")


# Add labels to instruct the user
instruction_label = tk.Label(root, text="Close this box to stop conversion to clipboard")
instruction_label.pack(pady=20)

message_label = tk.Label(root, text="Looking in Screenshot, then pasting to Clipboard")
message_label.pack(pady=20)



# Run the process when the GUI starts
def process_latest_screenshot():
    try:
        latest_png = get_latest_screenshot()
        webp_file = convert_png_to_webp(latest_png)
        encode_webp_to_base64(webp_file)
    except FileNotFoundError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", str(e))

process_latest_screenshot()

# Run the GUI loop
root.mainloop()
