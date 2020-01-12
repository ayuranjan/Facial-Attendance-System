from tkinter import *
import modify
import button3
import password
import modify2
root = Tk()
def function_exit():
    root.destroy()

root.title("COMPUTER VISION")
Label(root, text="COMPUTER VISION   ",font=("times new roman",20),fg="white",bg="maroon",height=3).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

 
#creating first button
Button(root,text="Authorization",font=("times new roman",30),fg="green",command=modify.main).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Logged History",font=("times new roman",30),fg="brown",command = button3.main).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
#creating third button


#creating attendance button
Button(root,text="Check Attendance",font=('times new roman',30),fg="blue",command = button3.find).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#Button(root,text="Search Attendance",font=("times new roman",30),fg="brown",command = button3.find).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
#creating forth button
#utton(root,text="Add person",font=('times new roman',30),fg="red",command =modify2.main).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',30),bg="red",fg="red",command = function_exit).grid(row=7,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)



root.mainloop()