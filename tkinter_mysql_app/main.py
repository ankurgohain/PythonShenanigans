# main.py
import tkinter as tk
from tkinter import messagebox, simpledialog
import database

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Labels
        self.label_name = tk.Label(self, text="Name:")
        self.label_name.grid(row=0, column=0, padx=5, pady=5)
        self.label_email = tk.Label(self, text="Email:")
        self.label_email.grid(row=1, column=0, padx=5, pady=5)

        # Entry fields
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        self.add_button = tk.Button(self, text="Add User", command=self.add_user)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(self, text="View Users", command=self.view_users)
        self.view_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.update_button = tk.Button(self, text="Update User", command=self.update_user)
        self.update_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.delete_button = tk.Button(self, text="Delete User", command=self.delete_user)
        self.delete_button.grid(row=5, column=0, columnspan=2, pady=5)

        # User List (Text Widget)
        self.user_list_label = tk.Label(self, text="Users:")
        self.user_list_label.grid(row=6, column=0, columnspan=2, pady=5)
        self.user_list_text = tk.Text(self, height=10, width=40)
        self.user_list_text.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    def add_user(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        if name and email:
            database.add_user(name, email)
            messagebox.showinfo("Success", "User added successfully!")
            self.clear_entries()
            self.view_users()
        else:
            messagebox.showerror("Error", "Please enter both name and email.")

    def view_users(self):
        self.user_list_text.delete(1.0, tk.END)  # Clear previous list
        users = database.get_all_users()
        if users:
            for user in users:
                self.user_list_text.insert(tk.END, f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}\n")
        else:
            self.user_list_text.insert(tk.END, "No users found.")

    def update_user(self):
        # For simplicity, let's assume update by ID from input, or select from list
        # In a real app, you'd likely have a way to select a user to update
        user_id = tk.simpledialog.askinteger("Update User", "Enter User ID to update:")
        if user_id:
            name = self.name_entry.get()
            email = self.email_entry.get()
            if name or email:
                database.update_user(user_id, name, email)
                messagebox.showinfo("Success", f"User {user_id} updated successfully!")
                self.clear_entries()
                self.view_users()
            else:
                messagebox.showerror("Error", "Please enter name or email to update.")
        else:
            messagebox.showinfo("Info", "Update cancelled.")

    def delete_user(self):
        user_id = tk.simpledialog.askinteger("Delete User", "Enter User ID to delete:")
        if user_id:
            database.delete_user(user_id)
            messagebox.showinfo("Success", f"User {user_id} deleted successfully!")
            self.clear_entries()
            self.view_users()
        else:
            messagebox.showinfo("Info", "Delete cancelled.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tkinter MySQL CRUD App")
    app = Application(master=root)
    app.mainloop()
