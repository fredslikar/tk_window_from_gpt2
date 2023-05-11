import tkinter as tk

root = tk.Tk()
root.geometry("500x400")
root.title("Выберите даты и названия")
"""Hi"""
# Добавляем текстовое поле с инструкциями
tk.Label(root, text="Введите начальную и конечную даты:").pack(pady=10)

# Добавляем поля ввода дат
start_date = tk.Entry(root, width=15)
start_date.pack(pady=5)
end_date = tk.Entry(root, width=15)
end_date.pack(pady=5)

# Добавляем флажки с названиями
options_frame = tk.Frame(root)
options_frame.pack(pady=10)


names = ["Название {}".format(i) for i in range(30)]
options = []
for name in names:
    var = tk.BooleanVar()
    chk = tk.Checkbutton(options_frame, text=name, variable=var)
    chk.pack(side="left", anchor="w")
    options.append(var)

# Добавляем кнопки "старт" и "отмена"
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Старт")
start_button.pack(side="left", padx=5)
cancel_button = tk.Button(button_frame, text="Отмена", command=root.destroy)
cancel_button.pack(side="left", padx=5)

root.mainloop()
