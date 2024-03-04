from tkinter import *
import tkinter as tk


from PIL import Image ,ImageTk

from tkinter.ttk import *


root=tk.Tk()

root.title("Human Activity Recognition")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

bg = Image.open(r"y9.jpg")
bg.resize((1366,500),Image.ANTIALIAS)
print(w,h)
bg_img = ImageTk.PhotoImage(bg)
bg_lbl = tk.Label(root,image=bg_img)
bg_lbl.place(x=0,y=93)
#, relwidth=1, relheight=1)

# w = tk.Label(root, text="Human Activity Recognition",width=40,background="skyblue",height=2,font=("Times new roman",19,"bold"))
# w.place(x=0,y=15)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="skyblue")


from tkinter import messagebox as ms


def Login():
    from subprocess import call
    call(["python","login.py"])
def Register():
    from subprocess import call
    call(["python","registration.py"])


wlcm=tk.Label(root,text="_______Welcome to Human Activity Recognition ________",width=85,height=2,background="skyblue",foreground="black",font=("Times new roman",22,"bold"))
wlcm.place(x=0,y=0)




d2=tk.Button(root,text="Login",command=Login,width=9,height=2,bd=5,background="pink",foreground="black",font=("times new roman",14,"bold"))
d2.place(x=100,y=300)


d3=tk.Button(root,text="Register",command=Register,width=9,height=2,bd=5,background="pink",foreground="black",font=("times new roman",14,"bold"))
d3.place(x=100,y=400)



root.mainloop()
