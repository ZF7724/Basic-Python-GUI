from tkinter import *


Window=Tk()

def Converter():
    UserInput=userVariable.get()
    
    Gram=float(UserInput)*1000
    print(t1.insert(END,format(Gram,',.2f')))
    
    Pounds=float(UserInput)*2.20462
    print(t2.insert(END,format(Pounds,',.2f')))
    
    Ounces=float(UserInput)*35.274
    print(t3.insert(END,format(Ounces,',.2f')))
    


label=Label(Window,text="Enter KG Here: ")
label.grid(row=0,column=0)

b1=Button(Window,text="Convert",command=Converter)
b1.grid(row=0,column=2)

userVariable=StringVar()

e1=Entry(Window,textvariable=userVariable)
e1.grid(row=0,column=1)

t1=Text(Window,height=1,width=20)
t1.grid(row=1,column=0)

t2=Text(Window,height=1,width=20)
t2.grid(row=1,column=1)

t3=Text(Window,height=1,width=20)
t3.grid(row=1,column=2)




Window.mainloop()