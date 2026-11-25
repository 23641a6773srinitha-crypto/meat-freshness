from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import tkinter
from tkinter import ttk
from tkinter import filedialog

main = Tk()

# Get the screen width and height
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

# Set the window size to the screen dimensions
main.geometry(f"{screen_width}x{screen_height}")


font = ('times', 15, 'bold')
title = Label(main, text='MEAT FRESHNESS')
title.config(bg='gold2', fg='thistle1')  
title.config(font=font)           
title.config(height=3, width=130)       
title.place(x=0,y=5)

font1 = ('times', 13, 'bold')
ff = ('times', 12, 'bold')


font1 = ('times', 12, 'bold')
text=Text(main,height=30,width=145)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=330,y=100)
text.config(font=font1)

main.config(bg='DarkSlateGray1')
main.mainloop()
