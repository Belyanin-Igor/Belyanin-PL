import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Информация", "Кнопка нажата, но выбранный вариант не выбран.")

root = tk.Tk()
root.title("Белянин Игорь Александрович")

notebook = ttk.Notebook(root)
notebook.pack(expand=1, fill="both", padx=10, pady=10)

# Первая вкладка
frame1 = ttk.Frame(notebook)
notebook.add(frame1, text="Простой калькулятор для двух чисел")

tk.Label(frame1, text="Введите первое число:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(frame1)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame1, text="Введите второе число:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(frame1)
entry2.grid(row=1, column=1, padx=5, pady=5)

def calculate():
    try:
        result = int(entry1.get()) + int(entry2.get())
        messagebox.showinfo("Результат", f"Сумма: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")

tk.Button(frame1, text="Сложить", command=calculate).grid(row=2, column=0, columnspan=2, pady=10)

# Вторая вкладка
frame2 = ttk.Frame(notebook)
notebook.add(frame2, text="Чекбоксы")

tk.Label(frame2, text="Выберите варианты:").pack(pady=5)

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

tk.Checkbutton(frame2, text="Первый", variable=var1).pack(anchor='w', padx=10)
tk.Checkbutton(frame2, text="Второй", variable=var2).pack(anchor='w', padx=10)
tk.Checkbutton(frame2, text="Третий", variable=var3).pack(anchor='w', padx=10)

# Третья вкладка
frame3 = ttk.Frame(notebook)
notebook.add(frame3, text="Текстовое поле")

tk.Label(frame3, text="Введите текст:").pack(pady=5)
text = tk.Text(frame3, wrap="word", height=10, width=40)
text.pack(padx=10, pady=10)

tk.Button(frame3, text="Загрузить файл", command=on_button_click).pack(pady=5)

root.mainloop()