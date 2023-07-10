import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.Ctk()
root.geometry("500x350")



def_login():
    print("Test")


frame = customtkinter.CtkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CtkLabel(master=frame, text="Login system", text_font=("Arial, 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CtkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry1 = customtkinter.CtkEntry(master=frame, placeholder_text="Password", show="*")
entry1.pack(pady=12, padx=10)

button = customtkinter.CtkButton(master=frame, text="Login", command=login)
button.pack(pady)