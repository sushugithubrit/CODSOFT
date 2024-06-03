import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("300x400")
        self.root.configure(bg="#282a36") 

        self.title_label = tk.Label(root, text="To-Do List", bg="#282a36", fg="#f8f8f2", font=("Helvetica", 16, "bold"))  # Dracula theme text color
        self.title_label.pack(pady=10)

        self.entry = tk.Entry(root, width=30, font=("Helvetica", 12))
        self.entry.pack(pady=10)

        # Button to add a new task
        self.add_button = tk.Button(root, text="Add task", command=self.add_task, bg="#50fa7b", fg="#282a36", font=("Helvetica", 10, "bold"), width=20)  # Dracula theme green color
        self.add_button.pack(pady=5)

        # Button to edit an existing task
        self.edit_button = tk.Button(root, text="Edit task", command=self.edit_task, bg="#ff79c6", fg="#282a36", font=("Helvetica", 10, "bold"), width=20)  # Dracula theme pink color
        self.edit_button.pack(pady=5)

        # Button to delete a task
        self.delete_button = tk.Button(root, text="Delete task", command=self.delete_task, bg="#ff5555", fg="#f8f8f2", font=("Helvetica", 10, "bold"), width=20)  # Dracula theme red color
        self.delete_button.pack(pady=5)

        # Button to mark a task as complete
        self.complete_button = tk.Button(root, text="Mark as complete", command=self.complete_task, bg="#f1fa8c", fg="#282a36", font=("Helvetica", 10, "bold"), width=20)  # Dracula theme yellow color
        self.complete_button.pack(pady=5)

        # Frame to hold the listbox and scrollbar
        self.listbox_frame = tk.Frame(root)
        self.listbox_frame.pack(pady=10)

        # Listbox to display the tasks
        self.listbox = tk.Listbox(self.listbox_frame, width=50, height=10, bg="#44475a", fg="#f8f8f2", font=("Helvetica", 10))  # Dracula theme selection color
        self.listbox.pack(side="left", fill="y")

        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.listbox_frame, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")

        # Configure the listbox and scrollbar to work together
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

    def add_task(self):
        """
        Adds a new task to the tasks list and updates the listbox. If the entry field is empty, 
        shows a warning message. After adding the task, clears the entry field.
        """
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_listbox()
        else:
            messagebox.showinfo("Warning", "Please enter a task.")
        self.entry.delete(0, "end")
    
    def edit_task(self):
        """
        Edits the selected task. If no task is selected, shows a warning message.
        """
        try:
            task_index = self.listbox.curselection()[0]
            task_to_edit = self.tasks[task_index]
            if task_to_edit.startswith("[Completed] "):
                task_to_edit = task_to_edit.replace("[Completed] ", "", 1)
            self.entry.delete(0, "end")
            self.entry.insert(0, task_to_edit)
            self.add_button.config(text="Update task", command=lambda: self.update_task(task_index))
        except:
            messagebox.showinfo("Warning", "Please select a task to edit.")
    
    def update_task(self, task_index):
        """
        Updates the selected task with the new task text. If the entry field is empty, shows a warning message.
        After updating the task, clears the entry field and changes the add button back to its original state.
        """
        new_task = self.entry.get()
        if new_task != "":
            self.tasks[task_index] = new_task
            self.update_listbox()
            self.add_button.config(text="Add task", command=self.add_task)
            self.entry.delete(0, "end")
        else:
            messagebox.showinfo("Warning", "Please enter a task.")

    def delete_task(self):
        '''
        Deletes the selected task. If no task is selected, shows a warning message.
        '''
        try:
            task_index = self.listbox.curselection()[0]
            del self.tasks[task_index]
            self.update_listbox()
        except:
            messagebox.showinfo("Warning", "Please select a task to delete.")

    def complete_task(self):
        """
        Marks the selected task as complete. If no task is selected or the task is already marked as complete,
        shows a warning message.
        """
        try:
            task_index = self.listbox.curselection()[0]
            if not self.tasks[task_index].startswith("[Completed] "):
                self.tasks[task_index] = "[Completed] " + self.tasks[task_index]
                self.update_listbox()
            else:
                messagebox.showinfo("Warning", "This task is already marked as complete.")
        except:
            messagebox.showinfo("Warning", "Please select a task to mark as complete.")

    def update_listbox(self):
        """
        Updates the listbox with the current tasks list.
        """
        self.listbox.delete(0, "end")
        for task in self.tasks:
            self.listbox.insert("end", task)

def main():
    root = tk.Tk()
    todo_list = ToDoList(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    
