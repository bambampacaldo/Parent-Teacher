
import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox

def func():
    window.destroy()
    import sign_up
def check():
    if User_Entry.get() == 'Admin' and my_password.get() == 'UserAdmin':
        window.destroy()
        from resources.main import app
        root = app()
        root.state('zoomed')
        root.mainloop()
    elif User_Entry.get() == '' or my_password.get() == '':
        messagebox.showinfo('Information', 'Please enter a Email and Password')
    else:
        messagebox.showerror(title='Something wrong', message='Invalid Email or Password')
        
window = tk.Tk()
window.geometry('500x500')
window.state('zoomed')
window.winfo_geometry()
window.title('Login Page')


frame_top = tk.Frame(master=window,background='#80ccff')
frame_top.pack(fill=tk.BOTH, expand=True, side='top')

title_label = tk.Label(master=frame_top, text='Parent Teacher Communication', font=('arial',  30, 'bold'), bg='#80ccff')
title_label.place(x=400, y=30)

bg_img = ImageTk.PhotoImage(file='Parent.jpg')
bg_label = tk.Label(master=frame_top, image=bg_img)
bg_label.pack(fill=tk.X,  side=tk.RIGHT)

User_label = tk.Label(master=frame_top, text='Username', bg='#80ccff', font=('arial', 11, 'bold'))
User_label.place(x=200, y=275)

User_Entry = tk.Entry(master=frame_top, borderwidth=5, relief=tk.FLAT, width=35, bd=0)
User_Entry.place(x=200, y=300, height=35)

password_label = tk.Label(master=frame_top, text='Password',bg='#80ccff',font=('arial', 11, 'bold'))
password_label.place(x=200, y=350)

my_password = tk.StringVar()

User_Password = tk.Entry(master=frame_top, borderwidth=5, relief=tk.FLAT,textvariable=my_password ,show='*', width=35, bd=0)
User_Password.place(x=200, y=375, height=35)

button = tk.Button(master=frame_top,text='Log in' ,borderwidth=5, relief=tk.RAISED,cursor='hand2' ,command=check)
button.place(x=363, y=427)

reg = tk.Label(master=frame_top, text='Do you have an account?',font=('arial', 10) ,bg='#80ccff')
reg.place(x=195, y=469)

sign_button = tk.Button(master=frame_top, text='Sign up',cursor='hand2' ,font=('arial', 10, 'underline'),bd=0,relief=tk.FLAT,activebackground='#80ccff' ,bg='#80ccff', command=func)
sign_button.place(x=345, y=468)
window.mainloop()