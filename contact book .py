import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Initialize contact list
        self.contacts = {}

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Contact Form
        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.root, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self.root, text="Email:").grid(row=2, column=0, padx=10, pady=5)

        self.entry_name = tk.Entry(self.root, width=30)
        self.entry_phone = tk.Entry(self.root, width=30)
        self.entry_email = tk.Entry(self.root, width=30)

        self.entry_name.grid(row=0, column=1, padx=10, pady=5)
        self.entry_phone.grid(row=1, column=1, padx=10, pady=5)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        self.button_add = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.button_add.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Contact List
        self.contact_listbox = tk.Listbox(self.root, width=50, height=10)
        self.contact_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.button_delete = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.button_delete.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def add_contact(self):
        name = self.entry_name.get().strip()
        phone = self.entry_phone.get().strip()
        email = self.entry_email.get().strip()

        if not name or not phone or not email:
            messagebox.showwarning("Input Error", "All fields must be filled out.")
            return

        if name in self.contacts:
            messagebox.showwarning("Duplicate Contact", "A contact with this name already exists.")
            return

        self.contacts[name] = (phone, email)
        self.update_contact_list()
        self.clear_form()

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Selection Error", "Select a contact to delete.")
            return

        name = self.contact_listbox.get(selected_index).split(" | ")[0]
        del self.contacts[name]
        self.update_contact_list()

    def update_contact_list(self):
        self.contact_listbox.delete(0, tk.END)
        for name, (phone, email) in self.contacts.items():
            self.contact_listbox.insert(tk.END, f"{name} | {phone} | {email}")

    def clear_form(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
