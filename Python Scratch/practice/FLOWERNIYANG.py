# import tkinter as tk
# import time
# import random
# from tkinter import Canvas
#
# root = tk.Tk()
# root.title("Flower Ni Yang")
# root.geometry("600x600")
#
# canvas = Canvas(root, width=600, height=550, bg='lightcoral')
# canvas.pack()
#
# stem_height = 0
# petal_size = 0
# blooming = False
# clock_start = None
# petal_growth = [0] * 17
#
#
# def start_animation():
#     global clock_start
#     clock_start = time.time()
#     countdown()
#
#
# def countdown():
#     global blooming
#     elapsed_time = time.time() - clock_start
#     if elapsed_time <= 5:
#         canvas.delete("timer")
#         canvas.create_text(300, 275, text=f'{5 - int(elapsed_time)}', font=('Cambria', 30), fill='white', tags="timer")
#         root.after(1000, countdown)
#     else:
#         canvas.delete("timer")
#         blooming = True
#         grow_stem()
#
#
# def grow_stem():
#     global stem_height
#     if stem_height < 200:
#         stem_height += 2
#         canvas.delete("stem")
#         canvas.create_rectangle(297, 400 - stem_height, 303, 400, fill="green", tags="stem")
#         root.after(25, grow_stem)
#     else:
#         bloom_flower()
#
#
# def bloom_flower():
#     if all(size >= 30 for size in petal_growth):
#         display_message()
#         return
#
#     for i in range(len(petal_growth)):
#         if petal_growth[i] < 30:
#             petal_growth[i] += random.uniform(0.5, 1.5)
#
#     canvas.delete("flower")
#     draw_flower()
#     root.after(20, bloom_flower)
#
#
# def draw_flower():
#     colors = ["#FFC0CB", "#FF69B4", "#DB7093"]
#     petal_positions = [(random.randint(270, 330), random.randint(160, 240)) for _ in range(12)]
#
#     for i, (x, y) in enumerate(petal_positions):
#         size = petal_growth[i % len(petal_growth)]
#         canvas.create_oval(x - size, y - size, x + size, y + size, fill=colors[i % len(colors)], outline="red", width=2,
#                            tags="flower")
#
#     small_petal_positions = [(random.randint(280, 320), random.randint(180, 230)) for _ in range(5)]
#     for i, (x, y) in enumerate(small_petal_positions):
#         size = petal_growth[i % len(petal_growth)] // 1.8
#         canvas.create_oval(x - size, y - size, x + size, y + size, fill="lightpink", outline="red", width=2,
#                            tags="flower")
#
#     oblong_petal_positions = [(random.randint(280, 320), random.randint(160, 220)) for _ in range(4)]
#     for i, (x, y) in enumerate(oblong_petal_positions):
#         size = petal_growth[i % len(petal_growth)] * 1.1
#         canvas.create_oval(x - size, y - size / 2, x + size, y + size / 2, fill="pink", outline="red", width=2,
#                            tags="flower")
#
#     canvas.create_oval(300 - 15, 200 - 15, 300 + 15, 200 + 15, fill="yellow", outline="gold", width=2, tags="flower")
#
#     canvas.create_oval(280, 400, 320, 420, fill="green", outline="darkgreen", tags="leaves")
#     canvas.create_oval(260, 390, 300, 410, fill="green", outline="darkgreen", tags="leaves")
#     canvas.create_oval(300, 390, 340, 410, fill="green", outline="darkgreen", tags="leaves")
#
#
# def display_message():
#     canvas.create_text(120, 460, text="To my Rhea: ",
#                        font=('Cambria', 13), fill='white', tags="message")
#     canvas.create_text(300, 500, text='''"Paninindigan kita \nAnumang sabihin ng magulong mundo" ''',
#                        font=('Cambria', 17), fill='white', tags="message")
#
#
# start_button = tk.Button(root, text="Start", command=start_animation, font=('Cambria', 15))
# start_button.place(x=260, y=560)
#
# root.mainloop()