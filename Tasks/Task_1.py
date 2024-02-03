import tkinter as tk

"""
Решите задачу: напишите программу, состоящую из двух списков Listbox .
В первом будет, например, перечень товаров, заданный программно. Второй
изначально пуст, пусть это будет перечень покупок. При клике на одну
кнопку товар должен переходить из одного списка в другой. При клике на
вторую кнопку – возвращаться (человек передумал покупать).
Предусмотрите возможность множественного выбора элементов списка
и их перемещения.
"""


class ShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Список покупок")

        self.available_items = ["Мороженное", "Огурцы", "Помидоры",
                                "Масло", "Какао", "Кофе", "Чай", "Сахар"]

        self.shop_list = []

        self.available_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        for item in self.available_items:
            self.available_listbox.insert(tk.END, item)
        self.available_listbox.pack(padx=10, pady=10, side=tk.LEFT,
                                    fill=tk.BOTH, expand=True)

        self.shop_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.shop_listbox.pack(padx=10, pady=10, side=tk.RIGHT,
                               fill=tk.BOTH, expand=True)

        self.add_btn = tk.Button(root, text=">>>",
                                 command=self.add_shop_list)
        self.add_btn.pack(pady=(10, 0), fill=tk.X)

        self.remove_btn = tk.Button(root, text="<<<",
                                    command=self.remove_shop_list)
        self.remove_btn.pack(pady=(0, 10), fill=tk.X)

    def add_shop_list(self):
        selected_items = list(self.available_listbox.curselection())
        selected_items.reverse()
        for index in selected_items:
            item = self.available_items[index]
            if item not in self.shop_list:
                self.shop_list.append(item)
                self.shop_listbox.insert(tk.END, item)
        for index in selected_items:
            self.available_listbox.delete(index)

    def remove_shop_list(self):
        selected_items = list(self.shop_listbox.curselection())
        selected_items.reverse()
        for index in selected_items:
            item = self.shop_list[index]
            self.shop_list.remove(item)
            self.shop_listbox.delete(index)
            self.available_listbox.insert(tk.END, item)


if __name__ == "__main__":
    root = tk.Tk()
    app = ShopApp(root)
    root.mainloop()
