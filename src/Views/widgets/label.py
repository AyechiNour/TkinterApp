import tkinter as tk

class Label(tk.Frame):
    def __init__(self, master=None, label_text="Label:", size = 0, style ="normal", color ="black", sticky="w"):
        super().__init__(master)
        self.configure(bg="white")
        self.label = tk.Label(self, text=label_text,bg="white", fg=color, font=('roboto',size,style))
        self.label.grid(row=0, column=0)

    def get_value(self):
        return self
    
    def set_value(self, label):
        self= label