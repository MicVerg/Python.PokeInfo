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
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="My lists")
        self.scrollable_frame.grid(row=1, column=2, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        for i in range(100):
            switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)

        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")




    def add_list():
        print("Test")


    def remove_list():
        print("Test")


    def add_item():
        print("Test")


    def remove_item():
        print("Test")


    def check_item():
        print("Test")


    def uncheck_item():
        print("Test")


if __name__ == "__main__":
    app = App()
    app.mainloop()