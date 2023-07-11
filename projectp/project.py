import tkinter
from PIL import Image
import customtkinter
from functools import partial

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

fruits_list = ["apple", "banana", "orange", "grape", "kiwi", "pineapple", "mango", "strawberry", "watermelon", "pear", "peach", "blueberry", "raspberry", "lemon", "lime", "cherry", "plum", "pomegranate", "apricot", "avocado", "blackberry", "coconut", "fig", "grapefruit"]
vegetables_list = ["carrot", "broccoli", "spinach", "tomato", "potato", "cucumber", "lettuce", "bell pepper", "onion", "garlic", "zucchini", "celery", "corn", "mushroom", "green bean", "peas", "cabbage", "cauliflower", "asparagus", "radish", "eggplant", "beetroot", "sweet potato", "brussels sprouts"]
grains_list = ["baguette", "sourdough", "ciabatta", "naan", "croissant", "muffin", "toast", "crust", "rye", "whole wheat", "focaccia", "panini", "pita", "scone", "brioche", "tortilla", "rice", "basmati", "jasmine", "wild", "brown", "fried", "risotto", "sushi", "paella", "noodles", "spaghetti", "linguine", "fettuccine", "lasagna", "macaroni", "ravioli", "gnocchi", "penne", "orzo"]
dairy_list = ["milk", "cheese", "yogurt", "butter", "cream", "sour cream", "cottage cheese", "whipped cream", "cheddar", "mozzarella", "parmesan", "swiss", "gouda", "brie", "feta", "cream cheese", "ricotta", "blue cheese", "goat cheese", "mascarpone", "provolone", "ghee", "buttermilk", "evaporated milk", "condensed milk"]
spices_list = ["cinnamon", "turmeric", "ginger", "cumin", "paprika", "coriander", "nutmeg", "cloves", "cardamom", "garlic powder", "onion powder", "chili powder", "oregano", "thyme", "rosemary", "bay leaf", "cayenne pepper", "black pepper", "white pepper", "red pepper flakes", "saffron", "mustard seeds", "fenugreek", "allspice", "star anise", "fennel seeds", "vanilla", "celery salt", "dill", "tarragon", "marjoram", "clove", "caraway seeds", "curry powder", "garam masala", "pumpkin pie spice"]
alcohol_list = ["beer", "wine", "whiskey", "vodka", "rum", "tequila", "gin", "brandy", "champagne", "cocktail", "martini", "margarita", "mojito", "sake", "scotch", "bourbon", "cognac", "liqueur", "absinthe", "vermouth", "cider", "sherry", "port", "amaretto", "baileys", "schnapps", "prosecco", "pinot noir", "merlot", "chardonnay", "sauvignon blanc", "pinot grigio", "rosé", "red wine", "white wine"]
fruits_image = customtkinter.CTkImage(light_image=Image.open("./img/icons8-fruit-48.png"), dark_image=Image.open("./img/icons8-fruit-48.png"))
vegetables_image = customtkinter.CTkImage(light_image=Image.open("./img/icons8-vegetables-48.png"), dark_image=Image.open("./img/icons8-vegetables-48.png"))
grains_image = customtkinter.CTkImage(light_image=Image.open("./img/icons8-grains-64.png"), dark_image=Image.open("./img/icons8-grains-64.png"))
dairy_image = customtkinter.CTkImage(light_image=Image.open("./img/icons8-cheese-48.png"), dark_image=Image.open("./img/icons8-cheese-48.png"))
spices_image = customtkinter.CTkImage(light_image=Image.open("./img/icons8-spices-48.png"), dark_image=Image.open("./img/icons8-spices-48.png"))
remove_image = customtkinter.CTkImage(light_image=Image.open("./img/icons8-alcohol-30.png"), dark_image=Image.open("./img/icons8-alcohol-30.png"))



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

        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=0, columnspan=3, padx=(20, 0), pady=(0, 20), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)

        # add list button
        self.button_1 = customtkinter.CTkButton(self.slider_progressbar_frame, text="Add a list", command=lambda: self.add_list_window())
        self.button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")


    def add_list_window(self):
        add_window = customtkinter.CTkToplevel(self)
        add_window.title("Add a list")
        add_window.transient(self)
        add_window.geometry("300x300")

        add_textbox = customtkinter.CTkTextbox(add_window, font=("Montserrat", 22), border_color="light_color")
        add_textbox.pack(padx=10, pady=10)

        button_frame = customtkinter.CTkFrame(add_window)
        button_frame.pack(pady=5)

        confirm_button = customtkinter.CTkButton(button_frame, text="Confirm", command=lambda: self.add_list(add_textbox))
        confirm_button.pack(side="left", padx=5)

        cancel_button = customtkinter.CTkButton(button_frame, text="Cancel", command=add_window.destroy)
        cancel_button.pack(side="left", padx=5)


    def add_list(self, add_textbox):
        add_text = add_textbox.get("1.0", tkinter.END).strip()  # Strip any leading/trailing whitespace
        if add_text:
            switch_frame = customtkinter.CTkFrame(self.scrollable_frame)
            switch_frame.grid(row=len(self.scrollable_frame_switches), column=0, padx=10, pady=(0, 20))

            switch = customtkinter.CTkSwitch(master=switch_frame, text=add_text, font=("Montserrat", 20))
            switch.grid(row=0, column=0)

            button_frame = customtkinter.CTkFrame(switch_frame)
            button_frame.grid(row=1, column=0, padx=5, pady=(10, 0))

            open_button = customtkinter.CTkButton(button_frame, text="Open", command=lambda: self.open_list_window(add_text))
            open_button.pack(side="left")

            # remove button
            remove_image = customtkinter.CTkImage(light_image=Image.open("./img/icons8-remove-48.png"), dark_image=Image.open("./img/icons8-remove-48.png"))
            remove_button = customtkinter.CTkButton(button_frame, image=remove_image, text="", command=lambda: self.remove_list_item(switch_frame))
            remove_button.pack(side="left", padx=5)

            switch_frame.grid_columnconfigure(0, weight=1)
            self.scrollable_frame_switches.append(switch)

        add_textbox.master.destroy()  # Close the popup window after adding the item


    def remove_list_item(self, switch_frame):
        switch_frame.destroy()
        self.scrollable_frame_switches.remove(switch_frame.winfo_children()[0])


    def open_list_window(self, list_name):
        open_window = customtkinter.CTkToplevel(self)
        open_window.title(list_name)
        open_window.transient(self)
        open_window.geometry("375x667")

        # Create a frame for the three columns
        columns_frame = customtkinter.CTkFrame(open_window)
        columns_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Column 1: Image
        image_frame = customtkinter.CTkFrame(columns_frame)
        image_frame.pack(side="left", padx=10)

        # Add your image widget or label here

        # Column 2: Description
        description_frame = customtkinter.CTkFrame(columns_frame)
        description_frame.pack(side="left", padx=10)

        # Add your description widget or label here

        # Column 3: Checkbox
        checkbox_frame = customtkinter.CTkFrame(columns_frame)
        checkbox_frame.pack(side="left", padx=10)

        checkbox = customtkinter.CTkCheckBox(checkbox_frame, text="Select")
        checkbox.pack(side="left")


    def add_item_window(self):
        add_item_window = customtkinter.CTkToplevel(self)
        add_item_window.title("Add your items")
        add_item_window.transient(self)
        add_item_window.geometry("375x667")

        add_item_textbox = customtkinter.CTkTextbox(add_item_window, font=("Montserrat", 22))
        add_item_textbox.pack(padx=10, pady=10)

        button_item_frame = customtkinter.CTkFrame(add_item_window)
        button_item_frame.pack(pady=5)

        confirm_item_button = customtkinter.CTkButton(button_item_frame, text="Confirm", command=lambda: self.add_item(add_item_textbox))
        confirm_item_button.pack(side="left", padx=5)

        cancel_item_button = customtkinter.CTkButton(button_item_frame, text="Cancel", command=add_item_window.destroy)
        cancel_item_button.pack(side="left", padx=5)


    def add_item(self, add_item_textbox):
        add_item_text = add_item_textbox.get("1.0", tkinter.END).strip()  # Strip any leading/trailing whitespace
        if add_item_text:
            switch_item_frame = customtkinter.CTkFrame(self.scrollable_frame)
            switch_item_frame.grid(row=len(self.scrollable_frame_switches), column=0, padx=10, pady=(0, 20))

            item_checkbox = customtkinter.CTkCheckBox(master=switch_frame, text=add_item_text, font=("Montserrat", 20))
            item_checkbox.grid(row=0, column=0)

            button_frame = customtkinter.CTkFrame(switch_frame)
            button_frame.grid(row=1, column=0, padx=5, pady=(10, 0))

            open_button = customtkinter.CTkButton(button_frame, text="Open", command=lambda: self.open_list_window(add_text))
            open_button.pack(side="left")

            # remove button
            remove_image = customtkinter.CTkImage(light_image=Image.open("./img/icons8-remove-48.png"), dark_image=Image.open("./img/icons8-remove-48.png"))
            remove_button = customtkinter.CTkButton(button_frame, image=remove_image, text="", command=lambda: self.remove_list_item(switch_frame))
            remove_button.pack(side="left", padx=5)

            switch_item_frame.grid_columnconfigure(0, weight=1)
            self.scrollable_frame_switches.append(item_checkbox)

        add_item_textbox.master.destroy()


def remove_item():
    print("Remove item")


def check_item():
    print("Check item")


def uncheck_item():
    print("UNcheck item")


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
