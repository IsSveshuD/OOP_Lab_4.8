import tkinter as tk

"""
Решите задачу: напишите программу по описанию. Размеры многострочного
текстового поля определяются значениями, введенными в однострочные
текстовые поля. Изменение размера происходит при нажатии мышью на кнопку,
а также при нажатии клавиши Enter. Цвет фона экземпляра Text светлосерый
( lightgrey ), когда поле не в фокусе, и белый, когда имеет фокус.
Событие получения фокуса обозначается как <FocusIn> , потери – как <FocusOut> .
Для справки: фокус перемещается по виджетам при нажатии Tab, Ctrl+Tab,
Shift+Tab, а также при клике по ним мышью (к кнопкам последнее не относится).
"""


def change_text_size(event=None):
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
        text.config(width=width, height=height)
    except ValueError:
        pass


def on_focus_in(event):
    text.config(bg='white')


def on_focus_out(event):
    text.config(bg='lightgrey')


root = tk.Tk()
root.title("Resizable Text Field")

width_entry = tk.Entry(root)
width_entry.grid(row=0, column=0, padx=5, pady=5)

height_entry = tk.Entry(root)
height_entry.grid(row=1, column=0, padx=5, pady=5)

text = tk.Text(root, wrap='word', bg='lightgrey', relief='solid')
text.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

resize_button = tk.Button(root, text="Изменить", command=change_text_size)
resize_button.grid(row=0, column=2, rowspan=2, padx=5, pady=5, sticky='nsew')

text.bind("<FocusIn>", on_focus_in)
text.bind("<FocusOut>", on_focus_out)

root.bind("<Tab>", lambda e: root.focus_get().event_generate("<FocusOut>"))
root.bind("<Shift-Tab>", lambda e: root.focus_get().event_generate(
    "<FocusOut>"))

root.bind("<Return>", change_text_size)

root.columnconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

root.mainloop()
