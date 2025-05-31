import tkinter as tk

def press(num):
    current = entry_var.get()
    entry_var.set(current + str(num))


def equalpress():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)

    except Exception as e:
        entry_var.set("Error")


def clear():
    entry_var.set("")


root = tk.Tk()
root.title("Basic Calculator App")
root.geometry("400x200")

entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var, font=("Arial",20), bd=10,bg="white", insertwidth=2, width=15,borderwidth=4)
entry.grid(row=0,column=0,columnspan=4)

buttons = [
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('+',3,3),
    ('0',4,0),('.',4,1),('-',4,2),('=',4,3),
    ('c',5,0)

]

for (text,row,col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20,pady=20,bg="lightpink",font=('Arial',18), command=equalpress)

    elif text == 'c':
        btn = tk.Button(root, text=text, padx=64,pady=20,bg="lavender",font=('Arial',16), command=clear)
        btn.grid(row=row,column=col,columnspan=3)
        continue

    else:
        btn = tk.Button(root, text=text, padx=20,pady=20,bg="skyblue",font=('Arial',18), command=lambda t=text: press(t))
    btn.grid(row=row,column=col)


root.mainloop()