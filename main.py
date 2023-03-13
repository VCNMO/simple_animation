import tkinter as tk
v = 10
def move_image():
    global x, y, image, canvas1, v
    x += v # увеличение позиции на оси "x" на 10
    canvas1.coords(image, x, y) # обновление координат изображения на новую позицию
    canvas1.after(20, move_image) # задержка в 50 миллисекунд и повторение цикла
    if x > 500:
        v = -v
    if x < 0:
        v = -v

root = tk.Tk()
canvas1 = tk.Canvas(root, width=500, height=500)
canvas1.pack()

pic = tk.PhotoImage(file="limon.png")
image = canvas1.create_image(100, 100, anchor=tk.NW, image=pic) # "image_file" - это переменная с загруженной картинкой
x, y = 100, 100 # начальные координаты изображения

move_image() # вызываем функцию для запуска анимации
root.mainloop()
