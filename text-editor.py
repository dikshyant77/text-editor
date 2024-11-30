from tkinter import *
from tkinter.filedialog import askopenfilename , asksaveasfilename

window=Tk()
window.title("Text editor")
window.geometry("600x500")
window.rowconfigure(0,minsize=800, weight=1)
window.columnconfigure(1, minsize=800 , weight=1)
 
def open_file():
    """open a file for editing"""
    file_path=askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file_path:
        return 
    text_edit.delete(1.0,END)
    with open(file_path, "r")as input_file:
        text=input_file.read()
        text_edit.insert(END ,text)
        input_file.close()
    window.title("Text editor ", file_path)

def save_file():
    file_path = asksaveasfilename(defaultextension="txt",filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file_path:
        return
    with open(file_path, "w") as output_file:
        text= text_edit.get(1.0, END)
        output_file.write(text)
    window.title("Text editor ", file_path)
text_edit= Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons , text="open", command=open_file)
btn_save = Button(fr_buttons, text="Save As....",command=save_file)
btn_open.grid(row=0, column= 0, sticky="ew",padx=5 ,pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0 , column=0, sticky="ns")
text_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()