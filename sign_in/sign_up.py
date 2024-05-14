import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox
def con():
    label2.config(text='Fill out all the form', )
def agree():
    win.destroy()
    import file1
def equal():
    if password.get () == '' or entry_confirm.get() == '':
        label2.config(text="Fill out all the form", fg='red', font=('arial', 15))
    elif password.get () == entry_confirm.get():
        label2['text'] = ''
        msg = messagebox.askquestion("Created Successfully", "Proceed to home?")
        if msg == 'yes':
            win.destroy()
            import login_form
        else:
            win.destroy()
    else:
        label2.config(text='Password does not match', fg='red', font=('arial', 13))

win = tk.Tk()
win.title('Sign up')
win.state('zoomed')
frame = tk.Frame(master=win,bg='#80ccff')
frame.pack(fill='both', expand=True)

bold_label = tk.Label(master=frame, text='Welcome to our community', font=('arial', 30, 'bold'), bg='#80ccff')
bold_label.pack(ipady=30)

img = ImageTk.PhotoImage(file='Images.jpg')
img_label = tk.Label(master=frame, image=img)
img_label.pack(side='left', padx=55, ipady=45)

label_frame = tk.LabelFrame(master=frame, text='Sign up', font=('arial', 20, 'bold'), bg='#80ccff', bd=0)
label_frame.place(x=789, y=154, height=500, width=430)

label_name = tk.Label(master=label_frame, text='Name', bg='#80ccff')
label_name.grid(row=0, column=0)

F_Name = tk.Entry(master=label_frame, font=('arial', 10))
F_Name.grid(row=1, column=0, ipadx=25, ipady=10, padx=10, pady=10)

label_name = tk.Label(master=label_frame, text='Last name', bg='#80ccff')
label_name.grid(row=0, column=2, padx=30)

L_Name = tk.Entry(master=label_frame, font=('arial', 10))
#L_Name.insert(0, 'Email')
L_Name.grid(row=1, column=2,ipadx=25, ipady=10, padx=10, pady=10)

email_label = tk.Label(master=label_frame, text='Email', bg='#80ccff')
email_label.grid(row=2, column=0)

user_email = tk.Entry(master=label_frame, font=('arial', 10))
user_email.grid(row=3, column=0, ipadx=25, ipady=10, padx=10, pady=10)

pass_label = tk.Label(master=label_frame, text='Password', bg='#80ccff')
pass_label.grid(row=4, column=0)

password = tk.Entry(master=label_frame, show='*', font=('arial', 10))
password.grid(row=5, column=0, ipadx=25, ipady=10, padx=10, pady=10)

confirm = tk.Label(master=label_frame, text='Confirm password', bg='#80ccff')
confirm.grid(row=6, column=0)

entry_confirm = tk.Entry(master=label_frame, show='*', font=('arial', 10))
entry_confirm.grid(row=7, column=0, ipadx=25, ipady=10, padx=10, pady=10)

chker = tk.BooleanVar()
chk = tk.Checkbutton(master=frame, text="",activebackground='#80ccff' ,variable=chker, bg='#80ccff')
chk.place(x=798, y=510)

l = tk.Label(master=frame, text='I agree the', bg='#80ccff')
l.place(x=820, y=510)

button1 = tk.Button(master=frame, text='Terms and Conditions', font=('arial', 8, 'underline'),bd=0 ,activebackground='#80ccff',cursor='hand2' ,bg='#80ccff', command=agree)
button1.place(x=880, y=511)

sign_button = ImageTk.PhotoImage(file='Sign_up1.png')

blnk = tk.Label(master=label_frame, text='', bg='#80ccff')
blnk.grid(row=8, column=0)

button = tk.Button(master=label_frame, text='Sign up', font=('arial', 10, 'bold'),cursor='hand2' ,command=equal)
button.grid(row=9, column=0,pady=15, ipadx=10)


label2 = tk.Label(master=label_frame, text='',  bg='#80ccff')
label2.grid(row=10, column=0, pady=5)
win.mainloop()