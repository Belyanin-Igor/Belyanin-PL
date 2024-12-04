import requests
from tkinter import Tk, Entry, Label, Button, messagebox
from tkinter import ttk
import json

# Функция для получения данных пользователя GitHub
def get_github_user_data():
    username = e.get()
    if not username:
        messagebox.showerror("Ошибка", "Пожалуйста, введите имя пользователя GitHub.")
        return

    url = f"https://api.github.com/users/{username}"
    try:
        user_data = requests.get(url).json()
        if 'message' in user_data:
            messagebox.showerror("Ошибка", user_data['message'])
            return

        # Выводим данные в консоль
        print(user_data)

        # Сохраняем данные в файл
        keys = ['company', 'created_at', 'email', 'id', 'name', 'url']
        data = {key: user_data.get(key, 'N/A') for key in keys}
        with open('data_file.json', 'w') as file:
            json.dump(data, file, indent=4)

        messagebox.showinfo("Успех", "Данные успешно сохранены в data_file.json")
    except requests.exceptions.RequestException as err:
        messagebox.showerror("Ошибка", f"Ошибка при запросе к API: {err}")

# Создаем главное окно
window = Tk()
window.title("Просмотр реальных примеры с GitHub")
window.geometry("400x200")

# Создаем и размещаем виджеты
Label(window, text="Введите имя пользователя:").pack(pady=5)
e = Entry(window, width=30)
e.pack(pady=5)

Button(window, text="Let's go", command=get_github_user_data, width=20).pack(pady=20)

# Запускаем главный цикл
window.mainloop()