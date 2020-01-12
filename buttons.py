import tkinter as tk
import fggg
root =tk.Tk()

label2 = tk.Label(root,text = "Enter Date in YYYY-MM-DD Format")
label2.pack(side="top", fill="x", pady=10)

entry1 = tk.Entry(root)
entry1.pack()


entry2 = tk.Entry(root)
entry2.pack()



button = tk.Button(root, text="Search", command=fggg.storevaluessubroutine)
button.pack()

root.mainloop()