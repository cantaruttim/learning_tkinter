import tkinter
import tkinter as tk


janela = tk.Tk()
var_class = tk.StringVar(value='Economic Class') # it's a string value not a int


def submitt():
    print(var_class.get())



button_economicClass = tkinter.Radiobutton(text='Economic Class', variable=var_class, value="Economic Class", command=submitt)
button_economicClass.grid(row=0, column=0)
button_executiveClass = tkinter.Radiobutton(text='Executive Class', variable=var_class, value="Executive Class", command=submitt)
button_executiveClass.grid(row=0, column=1)
button_firstClass = tkinter.Radiobutton(text='First Class', variable=var_class, value="First Class", command=submitt)
button_firstClass.grid(row=0, column=2)


# button = tk.Button(text='Submitt', command=submitt)
# button.grid(row=1,column=0)

janela.mainloop()