import tkinter as tk

root = tk.Tk()
root.title("Calcolatrice")
root.geometry("400x600")
root.resizable(0, 0)

expression = ""

def update_display(value):
    global expression
    expression += str(value)
    display_var.set(expression)

def calculate():
    global expression
    try:
        result = str(eval(expression))
        display_var.set(result)
        expression = result
    except:
        display_var.set("Errore")
        expression = ""

def clear():
    global expression
    expression = ""
    display_var.set("")

display_var = tk.StringVar()

display = tk.Entry(root, textvariable=display_var, font=("Arial", 30), bd=0, bg="black", fg="white", justify="right")
display.grid(row=0, column=0, columnspan=4, sticky="nsew")
display.insert(0, "0")

button_specs = [
    ('C', 1, 0, 'white', clear),  ('±', 1, 1, 'white', lambda: update_display("-")),
    ('%', 1, 2, 'white', lambda: update_display("%")), ('÷', 1, 3, 'white', lambda: update_display("/")),
    ('7', 2, 0, 'white', lambda: update_display("7")), ('8', 2, 1, 'white', lambda: update_display("8")),
    ('9', 2, 2, 'white', lambda: update_display("9")), ('×', 2, 3, 'white', lambda: update_display("*")),
    ('4', 3, 0, 'white', lambda: update_display("4")), ('5', 3, 1, 'white', lambda: update_display("5")),
    ('6', 3, 2, 'white', lambda: update_display("6")), ('-', 3, 3, 'white', lambda: update_display("-")),
    ('1', 4, 0, 'white', lambda: update_display("1")), ('2', 4, 1, 'white', lambda: update_display("2")),
    ('3', 4, 2, 'white', lambda: update_display("3")), ('+', 4, 3, 'white', lambda: update_display("+")),
    ('0', 5, 0, 'white', lambda: update_display("0")), ('.', 5, 2, 'white', lambda: update_display(".")),
    ('=', 5, 3, 'white', calculate),
]

for (text, row, col, color, command) in button_specs:
    if text == '0':
        btn = tk.Button(root, text=text, font=("Arial", 18), bg=color, fg="black", command=command)
        btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=1, pady=1)
    else:
        btn = tk.Button(root, text=text, font=("Arial", 18), bg=color, fg="black", command=command)
        btn.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
