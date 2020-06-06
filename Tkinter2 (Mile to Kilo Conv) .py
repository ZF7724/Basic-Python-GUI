from tkinter import *

window=Tk()

def MiletoKiloConverter():
    KiloConvV=1.60934
    print(userVariable.get())
    print(t1.insert(END,format(int(userVariable.get())*KiloConvV,',.4f')))
    
b1=Button(window,text="Calculate!",command=MiletoKiloConverter)
b1.grid(row=3,column=0)

userVariable=StringVar()

e1=Entry(window,textvariable=userVariable)
e1.grid(row=1,column=0)

t1=Text(window,height=2,width=25)
t1.grid(row=2,column=0)




window.mainloop()











