import tkinter as tk

win = tk.Tk()

def button():

    win.destroy()

func = tk.Button(master=win, text='Click me to proceed', command=button)
func.pack()
    
win.mainloop()