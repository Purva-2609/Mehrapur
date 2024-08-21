import tkinter as tk

# Function to update expression in the text entry box
def press(key):
    expression_field.insert(tk.END, key)

# Function to evaluate the final expression
def equalpress():
    try:
        total = str(eval(expression_field.get()))
        expression_field.delete(0, tk.END)
        expression_field.insert(tk.END, total)
    except:
        expression_field.delete(0, tk.END)
        expression_field.insert(tk.END, "Error")

# Function to clear the text entry box
def clear():
    expression_field.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Calculator")

expression_field = tk.Entry(root, font=('arial', 18), bd=10, insertwidth=2, width=14, borderwidth=4)
expression_field.grid(row=0, column=0, columnspan=4)

# Defining buttons
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

# Adding buttons to the grid
for button in buttons:
    action = lambda x=button: press(x) if x != "=" else equalpress()
    tk.Button(root, text=button, padx=20, pady=20, font=('arial', 18), command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(root, text='C', padx=20, pady=20, font=('arial', 18), command=clear).grid(row=row_val, column=0, columnspan=4)

root.mainloop()
