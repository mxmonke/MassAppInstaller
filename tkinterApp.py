import sys
import tkinter as tk
import subprocess

root = tk.Tk()
root.title("Installer")
root.focus_force()
root.minsize(300, 200)

def badPopup():
    popup = tk.Tk()
    popup.wm_title("!")
    popup.minsize(200, 100)
    tk.Message(popup, text="Installation failed. Please try again.").pack()
    okButton = tk.Button(popup, text="OK", command=popup.destroy)
    retryButton = tk.Button(popup, text="Retry", command=lambda: [popup.destroy(), download()])
    retryButton.pack()
    okButton.pack()

def goodPopup():
    popup = tk.Tk()
    popup.wm_title("!")
    popup.minsize(200, 100)
    tk.Message(popup, text="Installation successful!").pack()
    okButton = tk.Button(popup, text="OK", command=popup.destroy)
    okButton.pack()

def download():
    InstallingLabel = tk.Label(root, text="Installing... Please wait.")
    InstallingLabel.pack()
    root.update()
    try: subprocess.run("winget install Brave.Brave --silent --accept-package-agreements --accept-source-agreements", check=True)
    except:
        badPopup()
        InstallingLabel.destroy()
        return
    else:
        goodPopup()
        InstallingLabel.destroy()
        root.destroy()

button = tk.Button(root, text="Download", command=download)
button.pack(pady=20)

root.mainloop()
