import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk # type: ignore

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []
        self.images = []

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.listbox = tk.Listbox(self.frame, height=15, width=50)
        self.listbox.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.add_image_button = tk.Button(root, text="Add Image", command=self.add_image)
        self.add_image_button.pack()

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def add_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            img = Image.open(file_path)
            img.thumbnail((100, 100))
            img = ImageTk.PhotoImage(img)
            self.images.append(img)
            self.listbox.insert(tk.END, "Image added")
        else:
            messagebox.showwarning("Warning", "You must select an image.")

    def remove_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_task_index)
            del self.tasks[selected_task_index]
            if selected_task_index < len(self.images):
                del self.images[selected_task_index]
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
