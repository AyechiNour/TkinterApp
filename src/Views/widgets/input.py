import tkinter as tk

class InputField(tk.Frame):
    def __init__(self, master=None, label_text="Label:", initial_value="",show=""):
        super().__init__(master)
        self.configure(bg="white")
        self.label = tk.Label(self, text=label_text, bg="white", pady=5, font=('roboto',10,'bold'))
        self.label.grid(row=0, column=0, sticky="w")
        frame = tk.Frame(self, bg="white")
        frame.grid(row=1, column=0, sticky="w")
        emailInput = tk.Entry(frame,width=50,fg="black", border=0,bg="white", font=('roboto',8,'bold'), show=show)
        emailInput.grid(row=0, column=0)
        tk.Frame(frame,width=200,height=2,bg="black").grid(row=1, column=0,sticky="nsew")
                
    def get_value(self):
        return self
    
    def set_value(self, input):
        self= input