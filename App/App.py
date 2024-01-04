# Resolution
from ctypes import windll

import customtkinter as ctk

import SignIn as si

windll.shcore.SetProcessDpiAwareness(1)

app_width = 1200
app_height = 600
x = 80
y = 80

# Creating desktop window and setting parameters
ctk.set_appearance_mode("light")
root = ctk.CTk()
root.update()
root.title("GINF2")
root.iconbitmap("./Images/applogo.ico")

# Set the window size to the screen size
root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")  # Place the window at (0,0)
root.resizable(False, False)

si.SignIn(root)
root.mainloop()
