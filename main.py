import json
import random
import string
import customtkinter as ctk

# --- Настройки ---
HISTORY_FILE = "history.json"
MIN_LENGTH = 4
MAX_LENGTH = 32

# --- Вспомогательные функции ---
def load_history():
    """Загружает историю из файла JSON."""
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_history(history):
    """Сохраняет историю в файл JSON."""
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def generate_password(length, use_digits, use_letters, use_symbols):
    """Генерирует пароль на основе выбранных параметров."""
    character_pool = ""
    
    if use_letters:
        character_pool += string.ascii_letters  # a-z, A-Z
    if use_digits:
        character_pool += string.digits         # 0-9
    if use_symbols:
        character_pool += string.punctuation    # Спецсимволы !"#$%&'()*+,-./:;<=>?@[$$^_`{|}~
    
    if not character_pool:
        return "Ошибка: выберите хотя бы один тип символов!"
    
    return ''.join(random.choices(character_pool, k=length))

# --- Главное окно приложения ---
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Генератор случайных паролей")
        self.geometry("500x550")
        
        self.history_data = load_history()
        
        self.create_widgets()
        self.update_history_table()

    def create_widgets(self):
        # --- Рамка настроек ---
        settings_frame = ctk.CTkFrame(self)
        settings_frame.pack(pady=20, padx=20, fill="x")
        
        # Длина пароля (Ползунок)
        ctk.CTkLabel(settings_frame, text="Длина пароля:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.length_slider = ctk.CTkSlider(settings_frame, from_=MIN_LENGTH, to=MAX_LENGTH, number_of_steps=10,
                                          command=self.update_length_label)
        self.length_slider.set(12)
        self.length_slider.grid(row=0, column=1, padx=10, pady=5)
        
        self.length_label = ctk.CTkLabel(settings_frame, text="12")
        self.length_label.grid(row=0, column=2, padx=10, pady=5)
        
        # Чекбоксы для символов
        options_frame = ctk.CTkFrame(settings_frame)
        options_frame.grid(row=1, column=0, columnspan=3, pady=15)
        
        self.use_digits_var = ctk.BooleanVar(value=True)
        self.use_letters_var = ctk.BooleanVar(value=True)
        self.use_symbols_var = ctk.BooleanVar(value=True)
        
        ctk.CTkCheckBox(options_frame, text="Цифры (0-9)", variable=self.use_digits_var).pack(anchor="w")
        ctk.CTkCheckBox(options_frame, text="Буквы (a-z, A-Z)", variable=self.use_letters_var).pack(anchor="w")
        ctk.CTkCheckBox(options_frame, text="Спецсимволы (!@#$)", variable=self.use_symbols_var).pack(anchor="w")
        
        # Кнопка генерации
        self.generate_btn = ctk.CTkButton(self, text="Сгенерировать пароль", command=self.on_generate_click)
        self.generate_btn.pack(pady=15)
        
        # Поле для вывода пароля
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Ваш новый пароль появится здесь", state="readonly")
        self.password_entry.pack(pady=10, fill="x", padx=20)
        
    def update_length_label(self, value):
        """Обновляет текстовое поле длины при движении ползунка."""
        self.length_label.configure(text=str(int(float(value))))

    def on_generate_click(self):
        """Обработчик нажатия кнопки 'Сгенерировать'."""
        
        length = int(self.length_slider.get())
        
        # Валидация длины
        if length < MIN_LENGTH or length > MAX_LENGTH:
            ctk.CTkMessagebox(title="Ошибка", message=f"Длина должна быть от {MIN_LENGTH} до {MAX_LENGTH} символов.",
                             icon="cancel")
            return
            
        use_digits = self.use_digits_var.get()
        use_letters = self.use_letters_var.get()
        use_symbols = self.use_symbols_var.get()
        
        # Проверка, что выбран хотя бы один тип символов
        if not (use_digits or use_letters or use_symbols):
            ctk.CTkMessagebox(title="Ошибка", message="Выберите хотя бы один тип символов для генерации.",
                             icon="cancel")
            return
            
        password = generate_password(length, use_digits, use_letters, use_symbols)
        
        # Сохранение в историю и обновление UI
        self.history_data.append(password)
        save_history(self.history_data)
        
        self.update_history_table()
        
        # Вставка пароля в поле и выделение его
        self.password_entry.configure(state="normal")
        self.password_entry.delete(0, "end")
        self.password_entry.insert(0, password)
        self.password_entry.configure(state="readonly")
        
    def update_history_table(self):
        """Обновляет таблицу истории в интерфейсе."""
         # Очистка старых виджетов в фрейме истории
         for widget in self.history_frame.winfo_children():
             widget.destroy()
             
         if not self.history_data:
             label = ctk.CTkLabel(self.history_frame, text="История пуста. Сгенерируйте пароль!")
             label.pack(pady=20)
             return

         # Создание Treeview (таблицы)
         columns = ("#1", "#2") # Используем системные имена колонок для простоты
         tree = ctk.CTkTreeview(self.history_frame, columns=columns, show="headings")
         tree.heading("#1", text="№")
         tree.heading("#2", text="Пароль")
         
         for idx, pwd in enumerate(self.Конечно, вот подробная инструкция и готовый код для выполнения задания «Random Password Generator».

Это задание не связано с конвертером валют, поэтому мы создадим новый проект.

### Структура проекта

Создайте новую папку для проекта, например, `password_generator`, и внутри неё следующую структуру:
