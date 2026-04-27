import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import json
def create_ui():
    root = tk.Tk()
    root.title("Random Password Generator")

    # Длина пароля
    tk.Label(root, text="Длина пароля:").grid(row=0, column=0, padx=10, pady=5)
    length_slider = tk.Scale(root, from_=4, to=32, orient=tk.HORIZONTAL)
    length_slider.set(12)
    length_slider.grid(row=0, column=1, padx=10, pady=5)

    # Чекбоксы
    use_digits = tk.BooleanVar(value=True)
    use_letters = tk.BooleanVar(value=True)
    use_special = tk.BooleanVar(value=True)

    tk.Checkbutton(root, text="Цифры", variable=use_digits).grid(row=1, column=0, sticky='w', padx=10)
    tk.Checkbutton(root, text="Буквы", variable=use_letters).grid(row=2, column=0, sticky='w', padx=10)
    tk.Checkbutton(root, text="Спецсимволы", variable=use_special).grid(row=3, column=0, sticky='w', padx=10)

    # Кнопка генерации
    tk.Button(root, text="Сгенерировать", command=lambda: generate_password(
        length_slider.get(), use_digits.get(), use_letters.get(), use_special.get(), root)).grid(row=4, column=0, columnspan=2, pady=10)

    # Поле для вывода пароля
    password_entry = tk.Entry(root, width=40)
    password_entry.grid(row=5, column=0, columnspan=2, pady=5)

    # Таблица истории
    history_tree = ttk.Treeview(root, columns=("password",), show="headings")
    history_tree.heading("password", text="Сгенерированные пароли")
    history_tree.grid(row=6, column=0, columnspan=2, pady=10)

    # Кнопки управления историей
    tk.Button(root, text="Сохранить историю", command=lambda: save_history(history_tree)).grid(row=7, column=0, pady=5)
    tk.Button(root, text="Загрузить историю", command=lambda: load_history(history_tree)).grid(row=7, column=1, pady=5)

    return root, password_entry, history_tree


def generate_password(length, use_digits, use_letters, use_special, root):
    if not (use_digits or use_letters or use_special):
        messagebox.showerror("Ошибка", "Выберите хотя бы один тип символов!")
        return

    chars = ''
    if use_digits: chars += string.digits
    if use_letters: chars += string.ascii_letters
    if use_special: chars += string.punctuation

    password = ''.join(random.choices(chars, k=length))

    # Вывод в интерфейс и добавление в историю
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    history_tree.insert('', 'end', values=(password,))

    def save_history(tree):
        passwords = [tree.item(i)['values'][0] for i in tree.get_children()]
        with open('history.json', 'w') as f:
            json.dump(passwords, f)

    def load_history(tree):
        try:
            with open('history.json', 'r') as f:
                passwords = json.load(f)
            for pwd in passwords:
                tree.insert('', 'end', values=(pwd,))
        except FileNotFoundError:
            messagebox.showinfo("Информация", "Файл истории не найден.")
