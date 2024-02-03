import tkinter as tk


def draw_house(canvas):
    canvas.create_rectangle(50, 150, 250, 300, fill="lightblue",
                            outline="lightblue")
    canvas.create_polygon(25, 150, 150, 50, 275, 150, fill="lightblue")


def draw_sun(canvas):
    canvas.create_oval(230, 20, 280, 70, fill="orange", outline="yellow")


def draw_grass(canvas, num_lines=20, incline=10):
    x_start = 10
    y_start = 300
    y_end = 275
    color = "green"

    for _ in range(num_lines):
        x_end = x_start + incline
        canvas.create_line(x_start, y_start, x_end, y_end, fill=color)
        x_start += incline + 5


def main():
    root = tk.Tk()
    root.title("Домик")

    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()

    draw_house(canvas)
    draw_sun(canvas)
    draw_grass(canvas)

    root.mainloop()


if __name__ == "__main__":
    main()
