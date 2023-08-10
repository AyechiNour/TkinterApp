import tkinter as tk
import sys
sys.path.append('C:\\Users\\Dell Pc\\Documents\\projects\\projetTkinter')
from src.Views.widgets.input import InputField
from src.Views.widgets.label import Label
from src.Views.widgets.boutton import CustomButton

def update_frame_size(event):
    frame_width = root.winfo_width() // 2
    frame_height = root.winfo_height()
    frame1.config(width=frame_width, height=frame_height)
    frame2.config(width=frame_width, height=frame_height)

# Fonction pour centrer un frame dans un parent
def center_frame(parent, child):
    child.grid(row=1, column=1)
    parent.grid_rowconfigure(0, weight=1)
    parent.grid_rowconfigure(2, weight=1)
    parent.grid_columnconfigure(0, weight=1)
    parent.grid_columnconfigure(2, weight=1)

root = tk.Tk()
root.title("Sign Up")
root.geometry("1200x600")
root.configure(bg="white")
root.minsize(700, 500)

# Création de deux frames
frame1 = tk.Frame(root, bg="#F1F2F7")
frame2 = tk.Frame(root, bg="white")

# Placement initial des frames dans la grille
frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)

#Creation de frame3
frame3 = tk.Frame(frame2, bg="white",width=200, height=100)
frame3.pack()

center_frame(frame2, frame3)

#Creation de frame4
frame4 = tk.Frame(frame1, bg="white",width=200, height=100)
frame4.pack()

center_frame(frame1, frame4)

#Image
# img = tk.PhotoImage(file="projettkinter\ressources\SignInImg.jpg")
# tk.Label(frame4,image=img,bg="white").pack()

#Welcome
label_welcome = Label(frame3,label_text="Welcome",size=20, style="bold", color="#111858" )
label_welcome.grid(row=0, column=0, sticky="w")

#slogan
label_welcome = Label(frame3,label_text="Register your account",size=11, style="bold", color="#AAAAAA" )
label_welcome.grid(row=1, column=0, sticky="w", pady=(0, 40))

#fullName
input_email = InputField(frame3, label_text="Full Name", show="")
input_email.grid(row=2, column=0)

#email
input_email = InputField(frame3, label_text="Email", show="")
input_email.grid(row=3, column=0 ,pady=(20,2))

#password
input_password = InputField(frame3, label_text="Password", show="*")
input_password.grid(row=4, column=0, pady=(20,0))

#confirm password
input_password = InputField(frame3, label_text="Confirm Password", show="*")
input_password.grid(row=5, column=0, pady=(20,0))

#signUpButton
signInButton = CustomButton(frame3, row=6, column=0, text="Sign Up", bg_color="#0B59B2", fg_color="white", borderwidth=1, padding=(0, 8), font=('roboto',10,'bold'), active_bg_color="#0B59B2")
signInButton.grid(pady=(30,5), sticky="snew")

#Creation de frame5
frame5 = tk.Frame(frame3, bg="red",width=200, height=100)
frame5.grid(row=7, column=0, pady=(0,0))

#accountQuestion
label_accountQuestion = Label(frame5,label_text="Already have an account?",size=10, style="normal", color="#969696" )
label_accountQuestion.grid(row=0, column=0, pady=(0,0))

#signInButton
signUpButton = CustomButton(frame5, row=0, column=1, text="Sign In", bg_color="white", fg_color="#111858", borderwidth=0, padding=(0,0), font=('roboto',10,'bold'), active_bg_color="white")
signUpButton.grid(pady=(0,0), padx=(0,0), sticky="w")

# Création de frame pour logo sagemcom
frame0 = tk.Frame(root, bg="red",width=100, height=100)
frame0.grid(row=0, column=1, sticky="se")

# Configuration pour redimensionner les frames
root.bind("<Configure>", update_frame_size)

root.mainloop()