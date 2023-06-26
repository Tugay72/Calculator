import tkinter as tk

window = tk.Tk()
window.geometry("435x630")
window.maxsize(435, 630)
window.minsize(435, 630)

exp = ""
text = tk.StringVar()

frame = tk.Frame(window)
frame.grid(row=4, column=2)


def button(number):
    global exp
    exp += str(number)
    text.set(exp)


def clear():
    global exp
    exp = ''
    text.set(exp)


def equal():
    global exp
    total = str(eval(exp))
    text.set(total)


results = tk.Entry(window, font="Calibri 48", width=13, justify="right", textvariable=text)
results.grid(row=0, column=0, columnspan=4)

# FIRST ROW ↓

seven = tk.Button(window, text="7", font="Calibri 48", width=3, bg="white", fg="black", relief="flat",
                  command=lambda: button(7))
seven.grid(row=1, column=0)

eight = tk.Button(text="8", font="Calibri 48", width=3, bg="white", fg="black", relief="flat",
                  command=lambda: button(8))
eight.grid(row=1, column=1)

nine = tk.Button(text="9", font="Calibri 48", width=3, bg="white", fg="black", relief="flat",
                 command=lambda: button(9))
nine.grid(row=1, column=2)

slash = tk.Button(text="/", font="Calibri 48", width=3, bg="#0FF3A7", fg="white", relief="flat",
                  command=lambda: button('/'))
slash.grid(row=1, column=3)

# SECOND ROW ↓

four = tk.Button(text="4", font="Calibri 48", width=3, bg="White", fg="black", relief="flat",
                 command=lambda: button(4))
four.grid(row=2, column=0)

five = tk.Button(text="5", font="Calibri 48", width=3, bg="White", fg="black", relief="flat",
                 command=lambda: button(5))
five.grid(row=2, column=1)

six = tk.Button(text="6", font="Calibri 48", width=3, bg="White", fg="black", relief="flat",
                command=lambda: button(6))
six.grid(row=2, column=2)

x = tk.Button(text="x", font="Calibri 48", width=3, bg="#0FF3A7", fg="White", relief="flat",
              command=lambda: button('*'))
x.grid(row=2, column=3)

# THIRD ROW ↓

one = tk.Button(text="1", font="Calibri 48", width=3, bg="White", fg="Black", relief="flat",
                command=lambda: button(1))
one.grid(row=3, column=0)

two = tk.Button(text="2", font="Calibri 48", width=3, bg="White", fg="Black", relief="flat",
                command=lambda: button(2))
two.grid(row=3, column=1)

three = tk.Button(text="3", font="Calibri 48", width=3, bg="White", fg="Black", relief="flat",
                  command=lambda: button(3))
three.grid(row=3, column=2)

minus = tk.Button(text="-", font="Calibri 48", width=3, bg="#0FF3A7", fg="White", relief="flat",
                  command=lambda: button('-'))
minus.grid(row=3, column=3)

# FOURTH ROW ↓

zero = tk.Button(text="0", font="Calibri 48", width=3, bg="White", fg="Black", relief="flat",
                 command=lambda: button(0))
zero.grid(row=4, column=0)

dot = tk.Button(text=".", font="Calibri 48", width=3, bg="White", fg="Black", relief="flat",
                command=lambda: button("."))
dot.grid(row=4, column=1)

equals = tk.Button(frame, text="=", font="Calibri 24", width=6, height=1, bg="#FF4545", fg="Black", relief="flat",
                   command=lambda: equal())
equals.grid(row=1, column=2)

plus = tk.Button(text="+", font="Calibri 48", width=3, bg="#0FF3A7", fg="White", relief="flat",
                 command=lambda: button('+'))
plus.grid(row=4, column=3)

ce = tk.Button(frame, text="C", font="Calibri 24", width=6, height=1, bg="#FF4545", fg="Black", relief="flat",
               command=lambda: clear())
ce.grid(row=4, column=2)

window.mainloop()
