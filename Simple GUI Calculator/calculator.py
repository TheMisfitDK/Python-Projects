import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Calculator")

# Expression and input text
expression = ""
input_text = tk.StringVar()

# Functions
def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def equalpress():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Entry box
entry = tk.Entry(root, textvariable=input_text, width=20, font=('Arial', 16), bd=5, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

# Create buttons
for i, row in enumerate(buttons):
    for j, btn in enumerate(row):
        cmd = equalpress if btn == '=' else lambda x=btn: press(x)
        tk.Button(root, text=btn, width=5, height=2, command=cmd).grid(row=i+1, column=j)

# Clear button
tk.Button(root, text='C', width=22, height=2, command=clear).grid(row=5, column=0, columnspan=4)

# Run the app
root.mainloop()