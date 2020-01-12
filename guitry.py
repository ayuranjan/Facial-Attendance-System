import tkinter as tk                
from tkinter import font  as tkfont 
import modify
import button3





class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="COMPUTER VISION ",bg = "red", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="LOGIN",
                            command=modify.main)

        button2 = tk.Button(self,text="LOGGED HISTORY",
                            command=lambda: controller.show_frame("PageOne"))
        button3 = tk.Button(self, text="CHECK ATTENDANCE",
                            command=lambda: controller.show_frame("PageTwo"))
        
        

        button1.pack()
        button2.pack()
        button3.pack()
       


class PageOne(tk.Frame):
    
    

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        

       
        
        label1 = tk.Label(self,text = "Enter Date in YYYY-MM-DD Format",font =controller.title_font)
        label1.pack(side="top", fill="x", pady=10)

        entry1 = tk.Entry(self)
        entry1.pack()
        
        

        button2 = tk.Button(self, text="Enter ",
                           command=lambda: button3.main(entry1))
        

                      

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button2.pack()
        
        button.pack()

   


class PageTwo(tk.Frame):
    
    


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label1 = tk.Label(self,text = "Enter Employee Name",font =controller.title_font)
        label1.pack(side="top", fill="x", pady=10)
        
        entry1 = tk.Entry(self)
        entry1.pack()

        
        button7 = tk.Button(self, text="Search ",
                           command=lambda: button3.find(entry1))
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        
        button7.pack()



        button.pack()
    


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()