import tkinter as tk

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ShellOS Paint")

        self.canvas = tk.Canvas(self.root, bg='white', width=800, height=600)
        self.canvas.pack()

        self.color = 'black'
        self.brush_size = 5

        self.canvas.bind("<B1-Motion>", self.paint)
        
        self.setup_tools()

    def setup_tools(self):
        color_frame = tk.Frame(self.root)
        color_frame.pack(side=tk.LEFT, padx=10)

        colors = ['black', 'red', 'green', 'blue', 'yellow', 'purple', 'orange']
        for color in colors:
            btn = tk.Button(color_frame, bg=color, width=2, command=lambda c=color: self.change_color(c))
            btn.pack(pady=2)

        size_frame = tk.Frame(self.root)
        size_frame.pack(side=tk.LEFT, padx=10)

        sizes = [1, 2, 5, 10, 20]
        for size in sizes:
            btn = tk.Button(size_frame, text=str(size), command=lambda s=size: self.change_brush_size(s))
            btn.pack(pady=2)

        clear_btn = tk.Button(self.root, text="Clear", command=self.clear_canvas)
        clear_btn.pack(pady=10)

    def change_color(self, new_color):
        self.color = new_color

    def change_brush_size(self, new_size):
        self.brush_size = new_size

    def clear_canvas(self):
        self.canvas.delete("all")

    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
