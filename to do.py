import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Create and place widgets
        self.task_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.entry_task = tk.Entry(root, width=50)
        self.entry_task.pack(pady=5)

        self.button_add = tk.Button(root, text="Add Task", command=self.add_task)
        self.button_add.pack(pady=5)

        self.button_remove = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.button_remove.pack(pady=5)

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
