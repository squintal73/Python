from tkinter import *


app=Tk()
app.title("Sidnei Quintal")
app.geometry("500x300")
app.configure(background="#008")
txt1=Label(app,text="Curso",background="#008",foreground="#fff")
txt1.place(x=10,y=10,width=100,height=20)
vtxt="Módulo Tkinder"
vbg="#ff0"
vfg="#000"
txt2=Label(app,text=vtxt,bg=vbg,fg=vfg)
txt2.pack(ipadx=20,ipady=20,padx=5,pady=5,side="top",fill=Y,expand=True)



app.mainloop()