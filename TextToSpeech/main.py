import tkinter as tk
import time
import ttsmodule
import threading
from tkinter.constants import HORIZONTAL, LEFT, VERTICAL
#TODO A multiprocessing.Process can p.terminate()




root = tk.Tk()
root.title('Testing')
root.iconbitmap('C:/Windows/System32/notebook.ico')
root.geometry("700x400+800+050") # Set offset from top-left corner of screen as well as size
root.maxsize(1000,700)

root.wm_attributes("-topmost", False)
root.wm_attributes("-disabled", False)
#root.wm_attributes("-transparentcolor", "white")
root.wm_attributes("-alpha", 1) # opacity
Main = tk.Label(root,bg='gray55')
Main.place(x=0, y=0, width=700, height=700 )

# Global variables
text1 = 'This is a sentence, which is not meant to mean anything.'
checkbox_Debounce = tk.IntVar()
debounce_pause = True

# reading file // content()
f = open('Crime_and_Punishment.txt','r',encoding='utf8') # 'Discovery_of_India.txt'
lines = f.readlines()
index=0
Content = ''
count=0
def content(x=1): # default is moving forward, 0 moves backward
    global count
    global lines
    global index
    global Content
    Content = ''
    count = 0
    if not x: # if x is 0/False
        if (index - 6) >= 0: # for the initial 6 sentences.
            index = index - 6
        else:
            index = 0
    while True:
        if count < 4:
            Content = Content + lines[index]
            if len(lines[index]) > 10:
                count += 1
            index += 1
        else:
            return Content
        time.sleep(0.05)


def start_thread(event, val): # multi-threading so tkinter wont freeze
    global thread1
    thread1 = threading.Thread(target=val, daemon=True)
    thread1.start()



def pause_Button(): # button_pause.config(text=' ▶ ', font=('Courier',15))
    global button_pause
    button_pause['state'] = tk.DISABLED
    button_right['state'] = tk.DISABLED
    button_left['state'] = tk.DISABLED
    Main['bg']='orange'
    button_pause.config(text='| |', font=('Courier',15))
    ttsmodule.speak(text1,horizontal.get())
    Main['bg']='gray55'
    button_pause['state'] = tk.NORMAL
    button_right['state'] = tk.NORMAL
    button_left['state'] = tk.NORMAL


def left_Button():
    global checkbox_Debounce
    global button_left
    global text_Label
    global text1
    button_pause['state'] = tk.DISABLED
    button_right['state'] = tk.DISABLED
    button_left['state'] = tk.DISABLED
    text1 = content(0)
    text_Label.config(text=text1)
    if checkbox_Debounce.get() == 1:
        Main['bg']='orange'
        ttsmodule.speak(text1,horizontal.get())
        Main['bg']='gray55'
    button_pause['state'] = tk.NORMAL
    button_right['state'] = tk.NORMAL
    button_left['state'] = tk.NORMAL


def right_Button():
    global checkbox_Debounce
    global horizontal
    var = float(horizontal.get())/10
    global text_Label
    global text1
    button_pause['state'] = tk.DISABLED
    button_right['state'] = tk.DISABLED
    button_left['state'] = tk.DISABLED
    text1 = content(1)
    text_Label.config(text=text1)
    if checkbox_Debounce.get() == 1:
        Main['bg']='orange'
        ttsmodule.speak(text1,horizontal.get())
        Main['bg']='gray55'
    button_pause['state'] = tk.NORMAL
    button_right['state'] = tk.NORMAL
    button_left['state'] = tk.NORMAL


horizontal = tk.Scale(root, from_=10, to=0, orient=VERTICAL, tickinterval=1, length=375, bg='white', activebackground='cornsilk4')
horizontal.place(x=620, y=5)

text_Label = tk.Label(root, text=text1, fg='blue', bg='white', height=00, width=00, anchor=tk.NW, wraplength=500)
text_Label.config(font=("Courier", 15))
text_Label.grid(row=0,column=0,pady=10)

button_left= tk.Button(root,bg='white', activebackground='cornsilk4', text='<<<',font=('Courier',15), command=lambda:start_thread(None, left_Button))
button_left.place(x=530, y=100)

button_pause= tk.Button(root,bg='white', activebackground='cornsilk4', text='| |',font=('Courier',15),command=lambda:start_thread(None, pause_Button))
button_pause.place(x=530, y=175)

button_right= tk.Button(root,bg='white', activebackground='cornsilk4', text='>>>',font=('Courier',15),command=lambda:start_thread(None, right_Button))
button_right.place(x=530, y=250)

checkbox = tk.Checkbutton(root, text='Check to speak', variable=checkbox_Debounce)
checkbox.place(x=500, y=325)


root.mainloop()
print('done')

'''
print (root.winfo_geometry()) # 200x200+182+182

'''