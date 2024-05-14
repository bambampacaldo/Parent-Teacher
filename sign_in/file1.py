import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox

def commd():
    window.destroy()
    import sign_up
window = tk.Tk()
window.state('zoomed')
window.title('Entry Widget Example')


e = tk.Entry(master=window, )
e.pack()
l = tk.Label(master=window,text='Thank you..!!!' ,fg='blue', font=('orbitron', 40, 'bold'))
l.pack()

bot = tk.Button(master=window, text='Go back to sign up', command=commd)
bot.pack()

window.mainloop()
