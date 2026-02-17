import tkinter as tk
from tkinter import messagebox

x=1
root=tk.Tk()

frame=tk.Frame(root)
frame.pack(fill="x")

btn_1=tk.Button(frame,text="open").pack(side="left",pady=10)
btn_2=tk.Button(frame,text="new").pack(side="left",pady=10)
btn_3=tk.Button(frame,text="language").pack(side="left",pady=10)
btn_4=tk.Button(frame,text="run").pack(side="left",pady=10)
btn_5=tk.Button(frame,text="save").pack(side="left",pady=10)
btn_6=tk.Button(frame,text="plugin").pack(side="left",pady=10)
btn_7=tk.Button(frame,text="setting").pack(side="left",pady=10)
btn_8=tk.Button(frame,text="setting").pack(side="left",pady=10)
btn_9=tk.Button(frame,text="terminal").pack(side="left",pady=10)
btn_10=tk.Button(frame,text="git").pack(side="left",pady=10)
btn_11=tk.Button(frame,text="go to the github").pack(side="left",pady=10)
btn_12=tk.Button(frame,text="themes").pack(side="left",pady=10)
up=tk.Button(root,width=1,text="↑").place(x=0,y=100)
middle=tk.Button(root,height=30,width=1).place(x=0,y=170)
down=tk.Button(root,width=1,text="↓").place(x=0,y=1320)
text=tk.Text(root,width=115,height=60).place(x=140,y=100)

def enter(event):
	global x
	tk.Label(root,text=x).place(x=100,y=60+x*35)
	x+=1		
root.bind("<Return>",enter)
root.mainloop()

