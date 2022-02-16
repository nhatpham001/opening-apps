from distutils import command
import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

#to restart, delete the save file

#getting rid of whitespace when not opening apps
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


#add function opening files to openfile button
def addApp():
    #delete outdated apps
    for widget in frame.winfo_children():
        widget.destroy()

    filename= filedialog.askopenfilename(initialdir="/", title="Select File", 
    filetypes= (("executables","*.exe"),("all files", "*.*")))
    apps.append(filename)
    print(filename)
    #showing apps on monitor
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

#function for running apps
def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

#white background in the middle
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx = 0.1, rely=0.1)

#open button
openfile = tk.Button(root, text="open File", padx=10, pady=5, fg="white", bg="#263D42", command= addApp)
openfile.pack()
#run button
runApps = tk.Button(root, text="run apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

#have the save folders show up after re-opening
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()
root.mainloop()

#save recently opened files as save.txt
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
