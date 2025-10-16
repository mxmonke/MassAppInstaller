import sys
import tkinter as tk
import subprocess

browsers = ["Google.Chrome", "Mozilla.Firefox", "Brave.Brave", "Opera.Opera", "Microsoft.Edge"]

root = tk.Tk()
root.title("Installer")
root.minsize(600, 400)

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
    okButton = tk.Button(popup, text="OK", command=sys.exit)
    okButton.pack()

def download():
    for i in browserListbox.curselection():
        Selection = browsers[i]
        InstallingLabel = tk.Label(root, text="Installing... Please wait.") # TODO make this a popup
        InstallingLabel.pack()
        try: 
            subprocess.run("winget install " + Selection + " --silent --accept-package-agreements --accept-source-agreements", check=True)
        except:
            badPopup()
            InstallingLabel.destroy()
            return
        else:
            goodPopup() #TODO make this only show after all selected browsers are installed
            InstallingLabel.destroy()

browserListbox = tk.Listbox(root, selectmode=tk.MULTIPLE)

for browser in browsers:
    browserListbox.insert(tk.END, browser)
browserListbox.pack(pady=20)

button = tk.Button(root, text="Download", command=download)
button.pack(pady=20)

button2 = tk.Button(root, text="test", command=lambda: print(browserListbox.curselection())) #TODO remove
button2.pack(pady=20)

#TODO add an option to only download without installing

root.mainloop()
