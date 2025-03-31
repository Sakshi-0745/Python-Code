import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""

        # Input field
        self.input_field = tk.Entry(root, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.input_field.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0),
        ]

        for (text, row, col) in buttons:
            if text == '=':
                button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), bg="lightgreen", command=self.calculate)
            elif text == 'C':
                button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), bg="red", command=self.clear)
            else:
                button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda t=text: self.on_button_click(t))

            button.grid(row=row, column=col, sticky="nsew")

        # Configure grid weights
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.root.grid_columnconfigure(j, weight=1)

    def on_button_click(self, char):
        """Handle button clicks."""
        self.expression += char
        self.input_field.delete(0, tk.END)
        self.input_field.insert(tk.END, self.expression)

    def calculate(self):
        """Evaluate the expression."""
        try:
            result = eval(self.expression)
            self.input_field.delete(0, tk.END)
            self.input_field.insert(tk.END, str(result))
            self.expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            self.clear()

    def clear(self):
        """Clear the input field and expression."""
        self.expression = ""
        self.input_field.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()