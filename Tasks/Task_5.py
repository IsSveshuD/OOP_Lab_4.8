import tkinter as tk

"""
Решите задачу: в данной программе создается анимация круга, который
движется от левой границы холста до правой:
Выражение c.coords(ball) возвращает список текущих координат объекта
(в данном случае это ball). Третий элемент списка соответствует его
второй координате x. Метод after вызывает функцию, переданную вторым
аргументом, через количество миллисекунд, указанных первым аргументом.
Изучите приведенную программу и самостоятельно запрограммируйте постепенное
движение фигуры в ту точку холста, где пользователь кликает левой кнопкой мыши.
Координаты события хранятся в его атрибутах x и y ( event.x , event.y ).
"""


def move_towards_point(target_x, target_y):
    current_x, current_y, _, _ = c.coords(ball)

    delta_x = target_x - current_x
    delta_y = target_y - current_y

    distance = (delta_x ** 2 + delta_y ** 2) ** 0.5

    normalized_delta_x = delta_x / distance
    normalized_delta_y = delta_y / distance

    step = 2

    if distance > step:
        c.move(ball, normalized_delta_x * step, normalized_delta_y * step)

        root.after(10, lambda: move_towards_point(target_x, target_y))


root = tk.Tk()
c = tk.Canvas(root, width=300, height=200, bg="white")
c.pack()

ball = c.create_oval(0, 100, 40, 140, fill='green')


def on_click(event):
    move_towards_point(event.x, event.y)


c.bind("<Button-1>", on_click)

root.mainloop()
