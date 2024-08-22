import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Labels
        self.label_length = tk.Label(root, text="Password Length:")
        self.label_length.grid(row=0, column=0, padx=10, pady=10)

        self.label_characters = tk.Label(root, text="Include Characters:")
        self.label_characters.grid(row=1, column=0, padx=10, pady=10)

        # Entry for password length
        self.entry_length = tk.Entry(root, width=10)
        self.entry_length.grid(row=0, column=1, padx=10, pady=10)
        self.entry_length.insert(0, "12")  # Default length

        # Checkbuttons for character types
        self.var_upper = tk.BooleanVar(value=True)
        self.var_lower = tk.BooleanVar(value=True)
        self.var_digits = tk.BooleanVar(value=True)
        self.var_symbols = tk.BooleanVar(value=True)

        tk.Checkbutton(root, text="Uppercase Letters", variable=self.var_upper).grid(row=1, column=1, padx=10, pady=5, sticky="w")
        tk.Checkbutton(root, text="Lowercase Letters", variable=self.var_lower).grid(row=2, column=1, padx=10, pady=5, sticky="w")
        tk.Checkbutton(root, text="Digits", variable=self.var_digits).grid(row=3, column=1, padx=10, pady=5, sticky="w")
        tk.Checkbutton(root, text="Symbols", variable=self.var_symbols).grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Generate button
        self.button_generate = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.button_generate.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Entry for generated password
        self.entry_password = tk.Entry(root, width=30)
        self.entry_password.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        length = self.entry_length.get()
        try:
            length = int(length)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid length.")
            return

        if length <= 0:
            messagebox.showerror("Error", "Length must be greater than 0.")
            return

        chars = ""
        if self.var_upper.get():
            chars += string.ascii_uppercase
        if self.var_lower.get():
            chars += string.ascii_lowercase
        if self.var_digits.get():
            chars += string.digits
        if self.var_symbols.get():
            chars += string.punctuation

        if not chars:
            messagebox.showerror("Error", "At least one character type must be selected.")
            return

        password = ''.join(random.choice(chars) for _ in range(length))
        self.entry_password.delete(0, tk.END)
        self.entry_password.insert(0, password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
