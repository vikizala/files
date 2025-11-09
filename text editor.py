import tkinter as tk
from tkinter import filedialog, messagebox


class TextEditor:
    def __init__(self, root):
        self.root = root
        self.text_area = tk.Text(self.root)
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        filemenu = tk.Menu(menubar)
        menubar.add_cascade(label="Файл", menu=filemenu)
        filemenu.add_command(label="Открыть", command=self.open_file)
        filemenu.add_command(label="Сохранить", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Выход", command=self.root.quit)

        editmenu = tk.Menu(menubar)
        menubar.add_cascade(label="Правка", menu=editmenu)
        editmenu.add_command(label="Поиск и замена", command=self.find_replace)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Текстовые файлы", "*.txt")]
        )
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Текстовые файлы", "*.txt")]
        )
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

    def find_replace(self):
        find_window = tk.Toplevel(self.root)
        find_label = tk.Label(find_window, text="Найти:")
        find_label.pack()
        find_entry = tk.Entry(find_window)
        find_entry.pack()

        replace_label = tk.Label(find_window, text="Заменить на:")
        replace_label.pack()
        replace_entry = tk.Entry(find_window)
        replace_entry.pack()

        def replace_text():
            find_text = find_entry.get()
            replace_text = replace_entry.get()
            content = self.text_area.get(1.0, tk.END)
            new_content = content.replace(find_text, replace_text)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, new_content)

        replace_button = tk.Button(find_window, text="Заменить", command=replace_text)
        replace_button.pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Текстовый редактор")
    app = TextEditor(root)
    root.geometry("800x600")
    root.mainloop()
