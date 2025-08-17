from tkinter import *

from tkinter.filedialog import askopenfilename,asksaveasfilename

win = Tk()

win.title('Edit text here')

win.geometry("600x500")

win.rowconfigure(0,minsize=800,weight=1)

win.columnconfigure(1,minsize=800,weight=1)

def open_file():

filepath = askopenfilename(filetypes=[("Text files",""

"*.txt"),("All files","*.*")])

if not filepath:

return

txt_edit.delete(1.0,END)

with open(filepath,"r") as input_file:

text = input_file.read()

txt_edit.insert(END,text)

input_file.close()

win.title(f"Text editor {filepath}")

def save_file():

filepath = asksaveasfilename(

defaulttexttension="txt",

filetypes=[("Text files","*.txt"), ("All files","*.*")],

)

if not filepath:

return

with open(filepath, "w") as output_file:

text = txt_edit.get(1.0,END)

output_file.write(text)

win.title(f"TEEEEXT {filepath}")

txt_edit = Text(win)

f1 = Frame(win,relief=RAISED,bd = 2)

bo = Button(f1,text="Open",command=open_file)

bs = Button(f1,text="save as",command=save_file)

bo.grid(row=0,column=0,sticky="ew",padx=5,pady=5)

bs.grid(row=1,column=0,sticky="ew",padx=5)

f1.grid(row=0,column=0,sticky="ns")

txt_edit.grid(row=0,column=1,sticky="nsew")

win.mainloop()