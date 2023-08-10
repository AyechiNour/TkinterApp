import tkinter as tk

class CustomButton:
    def __init__(self, master=None, row=0, column=0, text="Button", bg_color="blue", fg_color="white", borderwidth=0, padding=(10, 5), font=None, active_bg_color="lightblue", **kwargs):
        self.master = master
        self.row = row
        self.column = column
        self.text = text
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.borderwidth = borderwidth
        self.padding = padding
        self.font = font
        self.active_bg_color = active_bg_color
        self.button = tk.Button(self.master, text=self.text, command=self.button_click, **kwargs)
        self.button.configure(bg=self.bg_color, fg=self.fg_color, borderwidth=self.borderwidth, padx=self.padding[0], pady=self.padding[1], activebackground=self.active_bg_color)
        if self.font:
            self.button.configure(font=self.font)
        self.button.bind("<Enter>", self.on_enter)
        self.button.bind("<Leave>", self.on_leave)

    def grid(self, sticky="", **kwargs):
        self.button.grid(row=self.row, column=self.column, sticky=sticky, **kwargs)

    def button_click(self):
        print("Button clicked!")

    def on_enter(self, event):
        self.button.config(bg=self.active_bg_color)

    def on_leave(self, event):
        self.button.config(bg=self.bg_color)