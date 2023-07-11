import tkinter
import customtkinter
from functools import partial

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Grocery lists")
        self.geometry(f"{375}x{667}")

        # configure grid layout (4x4)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="My lists", label_font=("Montserrat", 22))
        self.scrollable_frame.grid(row=0, column=0, columnspan=3, padx=(0, 0), pady=(0, 20), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        for i in range(10):
            switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)

        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=0, columnspan=3, padx=(20, 0), pady=(0, 20), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)

        # add list button
        self.button_1 = customtkinter.CTkButton(self.slider_progressbar_frame, text="Add a list", command=lambda: self.add_list_window())
        self.button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # remove list button
        self.button_2 = customtkinter.CTkButton(self.slider_progressbar_frame, text="Remove a list", command=remove_list)
        self.button_2.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")


    def add_list_window(self):
        add_window = customtkinter.CTkToplevel(self)
        add_window.title("Add a list")
        add_window.transient(self)
        add_window.geometry("300x300")

        add_textbox = customtkinter.CTkTextbox(add_window, font=("Montserrat", 22))
        add_textbox.pack(padx=10, pady=10)

        button_frame = customtkinter.CTkFrame(add_window)
        button_frame.pack(pady=5)

        confirm_button = customtkinter.CTkButton(button_frame, text="Confirm", command=lambda: self.add_list(add_textbox))
        confirm_button.pack(side="left", padx=5)

        cancel_button = customtkinter.CTkButton(button_frame, text="Cancel", command=add_window.destroy)
        cancel_button.pack(side="left", padx=5)


    def add_list(self, add_textbox):
        add_text = add_textbox.get("1.0", tkinter.END)
        print("Add:", add_text)


def remove_list():
    print("Remove")


def add_item():
    print("Add item")


def remove_item():
    print("Remove item")


def check_item():
    print("Check item")


def uncheck_item():
    print("UNcheck item")


if __name__ == "__main__":
    app = App()
    app.mainloop()
