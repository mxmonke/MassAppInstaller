import tkinter as tk
import subprocess

root = tk.Tk()
root.title("Installer")
root.focus_force()
root.minsize(300, 200)

def download():
    try: subprocess.run("winget install Brave.Brave --silent", check=True)
    except:
        print("Error during installation")

button = tk.Button(root, text="Download", command=download)
button.pack(pady=20)

root.mainloop()
