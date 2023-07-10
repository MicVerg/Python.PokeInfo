import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Grocery lists")
        self.geometry(f"{375}x{667}")

        # configure grid layout (4x4)


        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="My lists")
        self.scrollable_frame.grid(row=1, column=2, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        for i in range(100):
            switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)






    def add_list():
        print("Test")


if __name__ == "__main__":
    app = App()
    app.mainloop()