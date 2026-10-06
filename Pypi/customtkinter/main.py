import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("Meu primeiro programa")
app.geometry("400x300")

label = ctk.CTkLabel(app, text="Olá! CustomTkinter funcionando!")
label.pack(pady=50)

app.mainloop()
