import tkinter as tk

def create_calculator_window():
    window = tk.Tk()
    window.title("ShellOS Calculator")

    # Create a display area
    display = tk.Entry(window, font=("Arial", 20))
    display.grid(row=0, column=0, columnspan=4, sticky="nsew")  # Sticky option ensures resizing

    # Create buttons (you can add more)
    buttons = [
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "C", "0", "=", "+"
    ]

    row, col = 1, 0
    for btn_text in buttons:
        btn = tk.Button(window, text=btn_text, font=("Arial", 16), command=lambda t=btn_text: handle_button_click(t))
        btn.grid(row=row, column=col, sticky="nsew")  # Sticky option ensures resizing
        col = (col + 1) % 4
        if col == 0:
            row += 1

    def handle_button_click(button_text):
        if button_text == "=":
            try:
                result = eval(display.get())
                display.delete(0, tk.END)
                display.insert(0, str(result))
            except Exception:
                display.delete(0, tk.END)
                display.insert(0, "Error")
        elif button_text == "C":
            display.delete(0, tk.END)
        else:
            display.insert(tk.END, button_text)

    # Configure resizing behavior
    for i in range(5):
        window.grid_rowconfigure(i, weight=1)
        window.grid_columnconfigure(i, weight=1)

    window.mainloop()

create_calculator_window()
