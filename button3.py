def values(entry1,entry2):
    entry1value = entry1
    entry2value = entry2
    print(entry1value)
    print(entry2value)
from tkinter import *
import datetime
import modify
#from gtts import gTTS 
#from playsound import playsound
allow = False
def main(entry1):
        

        root = Tk()
        date1 = entry1.get()
        file = date1 +"_attendence.txt"
        with open(file, "r") as f:
                Label(root, text=f.read()).pack()

        root.mainloop()
def find(entry1):
        
        now = datetime.datetime.now()

        date1 = now.strftime("%Y-%m-%d")
        file = date1 +"_attendence.txt"
        #name = input("Enter the name : ")
        #name = employee.name
        name = entry1.get()
        name.upper()
        root = Tk()
        with open(file) as f:
                if name in f.read():
                        str1 =name +" is present "
                        Label(root, text=str1).pack()

                else:
                        str2 =name  + " is not present"
                        Label(root, text =str2).pack()


def yes(name_id):        
        now = datetime.datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

        def timeStamped(fname, fmt='%Y-%m-%d_{fname}'):
                    return datetime.datetime.now().strftime(fmt).format(fname=fname)

        with open(timeStamped('attendence.txt'),'a+') as outf:
                    outf.write(name_id +"   ")
                    outf.write(date_time)
                    outf.write("   \n")

         # to spell the name of the person remove the lower comment and remove the comments on imports            
        '''mytext = 'Welcome  ' + name_id
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("welcome.mp3") 
        playsound('welcome.mp3')'''
        
def no():
        
        root =Tk()
        root.title("SORRY !!")
        string = "Sorry for inconveniece."
        string2 =" Please wait and try again."
        l = Label(root, text=string)
        l2 = Label(root,text = string2)
        l.grid(row = 0,column = 1 )
        l2.grid(row =1 ,column = 1 )
        root.after(7000,lambda :root.destroy())
        root.mainloop()
        


def file(name_id):
        now = datetime.datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

        def timeStamped(fname, fmt='%Y-%m-%d_{fname}'):
                    return datetime.datetime.now().strftime(fmt).format(fname=fname)

        with open(timeStamped('attendence.txt'),'a+') as outf:
                    outf.write(name_id +"   ")
                    outf.write(date_time)
                    outf.write("   \n")
