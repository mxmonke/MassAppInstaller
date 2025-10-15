import tkinter as tk
import subprocess
import os

root = tk.Tk()
root.title("Installer")
root.focus_force()
root.minsize(300, 200)

def badPopup():
    popup = tk.Tk()
    popup.wm_title("!")
    popup.minsize(200, 100)
    tk.Message(popup, text="Installation failed. Please try again.").pack()

def goodPopup():
    popup = tk.Tk()
    popup.wm_title("!")
    popup.minsize(200, 100)
    tk.Message(popup, text="Installation successful!").pack()

def download():
    tk.Message(root, text="Installing... Please wait.").pack()
    root.update()
    try: subprocess.run("winget install Brave.Brave --silent --accept-package-agreements --accept-source-agreements", check=True)
    except:
        badPopup()
        return
    else:
        goodPopup()
        root.destroy()

button = tk.Button(root, text="Download", command=download)
button.pack(pady=20)

root.mainloop()
