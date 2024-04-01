import tkinter as tk
from tkinter import ttk

def run_calculator():
    def button_click(symbol):
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current + symbol)

    def clear():
        entry.delete(0, tk.END)

    def calculate():
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")

    def toggle_theme():
        current_theme = root.tk.call('ttk::style', 'theme', 'use')
        if current_theme == 'clam':
            root.tk.call('ttk::style', 'theme', 'use', 'alt')
            root.config(bg='#ffffff')  # Change background color to white for light mode
            entry.config(bg='#ffffff', fg='#000000')  # Change entry widget colors for light mode
        else:
            root.tk.call('ttk::style', 'theme', 'use', 'clam')
            root.config(bg='#2b2b2b')  # Change background color to dark gray for dark mode
            entry.config(bg='#2b2b2b', fg='#ffffff')  # Change entry widget colors for dark mode

    # Create the main window
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("300x400")
    root.config(bg='#2b2b2b')  # Set initial background color to dark gray

    # Create an entry widget to display the input and output
    entry = tk.Entry(root, font=('Helvetica', 20), width=15, borderwidth=5, bg='#2b2b2b', fg='#ffffff')
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=20, sticky="nsew")

    # Define button labels
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ('C', 5, 0), ('Dark/Light', 5, 3)
    ]

    # Calculate button width
    button_width = 75

    # Create dark mode style for buttons
    style_dark = ttk.Style()
    style_dark.theme_use('clam')
    style_dark.configure('TButton', background='#2b2b2b', foreground='white', font=('Helvetica', 16), width=button_width, padding=10)

    # Create light mode style for buttons
    style_light = ttk.Style()
    style_light.theme_use('alt')
    style_light.configure('TButton', background='white', foreground='black', font=('Helvetica', 16), width=button_width, padding=10)

    # Create buttons
    for (text, row, column) in buttons:
        if text == 'C':
            button = ttk.Button(root, text=text, command=clear)
        elif text == '=':
            button = ttk.Button(root, text=text, command=calculate)
        elif text == 'Dark/Light':
            button = ttk.Button(root, text=text, command=toggle_theme)

        else:
            button = ttk.Button(root, text=text, command=lambda symbol=text: button_click(symbol))
        button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

    # Configure row and column weights
    for i in range(6):
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()

if __name__ == "__main__":
    run_calculator()
