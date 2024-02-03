import tkinter as tk

"""
Решите задачу: напишите программу по следующему описанию. Нажатие
Enter в однострочном текстовом поле приводит к перемещению текста
из него в список (экземпляр Listbox ). При двойном клике
( <Double-Button-1> ) по элементу-строке списка, она должна
копироваться в текстовое поле.
"""


def add_to_listbox(event):
    text = entry.get()
    if text:
        listbox.insert(tk.END, text)
        entry.delete(0, tk.END)


def copy_to_entry(event):
    selected_text = listbox.get(tk.ACTIVE)
    entry.delete(0, tk.END)
    entry.insert(0, selected_text)


root = tk.Tk()
root.title("Пример программы")


entry = tk.Entry(root)
entry.pack(pady=10)
entry.bind("<Return>", add_to_listbox)

listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(expand=True, fill=tk.BOTH)
listbox.bind("<Double-Button-1>", copy_to_entry)

root.mainloop()
