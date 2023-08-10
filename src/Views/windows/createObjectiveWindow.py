import tkinter as tk
from tkinter import ttk
import sys
sys.path.append('C:\\Users\\Dell Pc\\Documents\\projects\\projetTkinter')
from src.Views.widgets.input import InputField
from src.Views.widgets.label import Label
from src.Views.widgets.boutton import CustomButton

def update_frame_size(event):
    frame_width = root.winfo_width()
    frame_height = root.winfo_height()
    frame1.config(width=frame_width, height=frame_height)
    frame1.config(width=frame_width, height=frame_height)

# Fonction pour centrer un frame dans un parent
def center_frame(parent, child):
    child.grid(row=1, column=1)
    parent.grid_rowconfigure(0, weight=1)
    parent.grid_rowconfigure(2, weight=1)
    parent.grid_columnconfigure(0, weight=1)
    parent.grid_columnconfigure(2, weight=1)

root = tk.Tk()
root.title("Add Objective")
root.geometry("1200x600")
root.configure(bg="white")
root.minsize(700, 500)

# Création de deux frames
frame1 = tk.Frame(root, bg="white")

# Placement initial des frames dans la grille
frame1.grid(row=0, column=0)

# Création de frame pour logo sagemcom
frame0 = tk.Frame(root, bg="red")
frame0.grid(row=1, column=1, padx=50, pady=50, sticky="se")

# Creation de frame2
frame2 = tk.Frame(frame1, bg="white", width=200, height=100)
frame2.pack()
center_frame(frame1, frame2)

# ... (le reste de votre code)

#addObjective
label_welcome = Label(frame2,label_text="Add Objective",size=40, style="bold", color="#111858" )
label_welcome.grid(row=0, column=0, sticky="w")

#typeProd
input_typeProd = InputField(frame2, label_text="Production type", show="")
input_typeProd.grid(row=1, column=0, pady=(40,0))

#objProd
input_objProd = InputField(frame2, label_text="Production objective", show="")
input_objProd.grid(row=2, column=0, pady=(20,20))

#objdate
input_objdate = InputField(frame2, label_text="Date limite", show="")
input_objdate.grid(row=3, column=0, pady=(0,20))

frame3 = tk.Frame(frame2, bg="white",width=200, height=100)
frame3.grid(row=4, column=0, pady=(0,10), padx=(0,30), sticky="e")

#backButton
backButton = CustomButton(frame3, row=0, column=0, text="Back", bg_color="#FFFFFF", fg_color="#7B7B7B", borderwidth=1, padding=(20, 8), font=('roboto',10,'bold'), active_bg_color="#FFFFFF")
backButton.grid(pady=(0,5), padx=(10), sticky="snew")

#addButton
addButton = CustomButton(frame3, row=0, column=1, text="Add", bg_color="#0B59B2", fg_color="white", borderwidth=1, padding=(20, 8), font=('roboto',10,'bold'), active_bg_color="#0B59B2")
addButton.grid(pady=(0,5), sticky="snew")

# Création d'un Combobox
options = ["Option 1", "Option 2", "Option 3"]  # Remplacez par vos options
combo = ttk.Combobox(frame2, values=options)
combo.grid(row=5, column=0, pady=(20, 2), padx=(30), sticky="snew")

# Configuration pour redimensionner les frames
root.bind("<Configure>", update_frame_size)

root.mainloop()