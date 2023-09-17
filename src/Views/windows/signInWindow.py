import tkinter as tk
from PIL import Image, ImageTk
import sys
sys.path.append('C:\\Users\\Dell Pc\\Documents\\projects\\projetTkinter')
from src.Views.widgets.input import InputField
from src.Views.widgets.input import InputField
from src.Views.widgets.label import Label
from src.Views.widgets.boutton import CustomButton
from src.Controllers.authentificationController import AuthentificationController
from tkinter import messagebox

class SignInWindow:
    def __init__(self):
        def update_frame_size(event):
            frame_width = self.root.winfo_width() // 2
            frame_height = self.root.winfo_height()
            frame1.config(width=frame_width, height=frame_height)
            frame2.config(width=frame_width, height=frame_height)

        # Fonction pour centrer un frame dans un parent
        def center_frame(parent, child):
            child.grid(row=1, column=1)
            parent.grid_rowconfigure(0, weight=1)
            parent.grid_rowconfigure(2, weight=1)
            parent.grid_columnconfigure(0, weight=1)
            parent.grid_columnconfigure(2, weight=1)

        self.root = tk.Tk()
        self.root.title("Login")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.configure(bg="white")
        self.root.minsize(700, 500)

        # Création de deux frames
        frame1 = tk.Frame(self.root, bg="#F1F2F7")
        frame2 = tk.Frame(self.root, bg="white")

        # Placement initial des frames dans la grille
        frame1.grid(row=0, column=0)
        frame2.grid(row=0, column=1)

        #Creation de frame3
        frame3 = tk.Frame(frame2, bg="white",width=200, height=100)
        frame3.pack()

        center_frame(frame2, frame3)

        #Creation de frame4
        frame4 = tk.Frame(frame1, bg="white",width=10, height=10)
        frame4.pack()

        center_frame(frame1, frame4)

        # Chargez l'image à l'aide de PIL
        image_path = "C:\\Users\\Dell Pc\\Documents\\projects\\projetTkinter\\ressources\\signInImg.png"
        img = Image.open(image_path)

        # Convertissez l'image PIL en format Tkinter
        img_tk = ImageTk.PhotoImage(img)

        # Créez un widget Label pour afficher l'image
        label_image = tk.Label(frame4, image=img_tk, bg="#F1F2F7")
        label_image.grid(row=0, column=1) 

        #Welcome
        label_welcome = Label(frame3,label_text="Welcome Back",size=20, style="bold", color="#111858" )
        label_welcome.grid(row=0, column=0, sticky="w")

        #slogan
        label_welcome = Label(frame3,label_text="We make visualization effortless...",size=11, style="bold", color="#AAAAAA" )
        label_welcome.grid(row=1, column=0, sticky="w", pady=(0, 40))

        #email
        self.input_email = InputField(frame3, label_text="Email", show="")
        self.input_email.grid(row=2, column=0)

        #password
        self.input_password = InputField(frame3, label_text="Password", show="*")
        self.input_password.grid(row=3, column=0, pady=(20,2))

        #Forget password
        self.passwordButton = CustomButton(frame3, row=4, column=0, text="Forget password?", bg_color="white", fg_color="#969696", borderwidth=0, padding=(0, 0), font=('roboto',10,'normal'), active_bg_color="white")
        self.passwordButton.grid(sticky="e")

        #signInButton
        signInButton = CustomButton(frame3, row=5, column=0, text="Sign In", bg_color="#0B59B2", fg_color="white", borderwidth=1, padding=(0, 8), font=('roboto',10,'bold'), active_bg_color="#0B59B2", click_function=self.signIn)
        signInButton.grid(pady=(30,5), sticky="snew")

        #Creation de frame5
        frame5 = tk.Frame(frame3, bg="white",width=200, height=100)
        frame5.grid(row=7, column=0, pady=(0,0))

        #accountQuestion
        label_accountQuestion = Label(frame5,label_text="Don’t have an account yet?",size=10, style="normal", color="#969696" )
        label_accountQuestion.grid(row=0, column=0, pady=(0,0))

        #signUpButton
        signUpButton = CustomButton(frame5, row=0, column=1, text="Sign Up", bg_color="white", fg_color="#111858", borderwidth=0, padding=(0,0), font=('roboto',10,'bold'), active_bg_color="white", click_function = self.close_window)
        signUpButton.grid(pady=(0,0), padx=(0,0), sticky="w")

        # Création de frame pour logo sagemcom
        frame0 = tk.Frame(self.root, bg="red",width=100, height=100)
        frame0.grid(row=0, column=1, sticky="se")

        # Chargez l'image à l'aide de PIL
        imageLogo_path = "C:\\Users\\Dell Pc\\Documents\\projects\\projetTkinter\\ressources\\logoSagemcom.png"
        imgLogo = Image.open(imageLogo_path)

        # Redimensionnez l'image avec anti-crénelage
        imgLogo_redimensionnee = imgLogo.resize((100,110))

        # Convertissez l'image PIL en format Tkinter
        imgLogo_tk = ImageTk.PhotoImage(imgLogo_redimensionnee)

        # Créez un widget Label pour afficher l'image
        label_imageLogo = tk.Label(frame0, image=imgLogo_tk, bg="white")
        label_imageLogo.grid(row=0, column=1) 

        # Configuration pour redimensionner les frames
        self.root.bind("<Configure>", update_frame_size)

        self.root.mainloop()

    def signIn(self):
        input_email = self.input_email.get_value()
        input_password = self.input_password.get_value()
        try:
            user = AuthentificationController.signIn(input_email,input_password)
            from src.Views.windows.objectiveManagementWindow import ObjectiveManagementWindow
            self.root.destroy()
            objectiveManagementWindow = ObjectiveManagementWindow(user)  
        except ValueError as e:
            messagebox.showinfo("Alerte", str(e))
            print("Erreur lors de l'inscription :", str(e))
        
    def close_window(self): 
        from src.Views.windows.signUpWindow import SignUpWindow  
        self.root.destroy()
        signUpWindow = SignUpWindow()