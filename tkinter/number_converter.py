from tkinter import *
from tkinter import messagebox

bgColor, fgColor, accColor = "#fffaeb", "#130e01", "#cf4307"
root = Tk()
root.geometry('480x360')
root.minsize(410,300)
root.maxsize(720,480)
root.configure(bg=bgColor)


def convert():
    try:
        num = int(input_label.get().strip())
        if num < 0:
            messagebox.showerror("negative input", "currently negative numbers are not supported")
        output_ans.set("0" if num ==0 else make_binary(num))
    except ValueError as e:
        # output_ans.set("Invalid input, please enter an integer")
        messagebox.showerror("ValueError", "Invalid input, please enter an positive integer")

def make_binary(num):
    if num == 0:
        return ''
    return make_binary(num//2) + str(num % 2)


input_label = Entry(root, width=40)
input_label.pack(pady=70, ipady=7)

binary_btn = Button(root, text="binary", command=convert, bg=accColor, fg=bgColor, width=10)
binary_btn.pack()

output_ans = StringVar()
output_label = Label(root, textvariable=output_ans, font=("Arial", 12), fg=fgColor, bg=bgColor)
output_label.pack(pady=20)


root.mainloop()