import tkinter
from PIL import Image
import customtkinter

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
alcohol_image = customtkinter.CTkImage(light_image=Image.open("./img/icons8-alcohol-30.png"), dark_image=Image.open("./img/icons8-alcohol-30.png"))
remove_image = customtkinter.CTkImage(light_image=Image.open("./img/icons8-remove-48.png"), dark_image=Image.open("./img/icons8-remove-48.png"))
questionmark_image = customtkinter.CTkImage(light_image=Image.open("./img/icons8-question-mark-48.png"), dark_image=Image.open("./img/icons8-question-mark-48.png"))



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.list_of_items = []
        self.list_of_amounts = []
        self.lists_data = {}

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

        add_textbox = customtkinter.CTkTextbox(add_window, font=("Montserrat", 22))
        add_textbox.configure(height=8)
        add_textbox.pack(padx=10, pady=10)

        button_frame = customtkinter.CTkFrame(add_window)
        button_frame.pack(pady=5)

        confirm_button = customtkinter.CTkButton(button_frame, text="Confirm", command=lambda: self.add_list(add_textbox))
        confirm_button.pack(side="left", padx=5)

        cancel_button = customtkinter.CTkButton(button_frame, text="Cancel", command=add_window.destroy)
        cancel_button.pack(side="left", padx=5)


    def add_list(self, add_textbox):
        add_text = add_textbox.get("1.0", tkinter.END).strip()
        if add_text:
            switch_frame = customtkinter.CTkFrame(self.scrollable_frame)
            switch_frame.grid(row=len(self.scrollable_frame_switches), column=0, padx=10, pady=(0, 20))

            switch = customtkinter.CTkSwitch(master=switch_frame, text=add_text, font=("Montserrat", 20))
            switch.grid(row=0, column=0)

            button_frame = customtkinter.CTkFrame(switch_frame)
            button_frame.grid(row=1, column=0, padx=5, pady=(10, 0))

            open_button = customtkinter.CTkButton(button_frame, text="Open", command=lambda: self.open_list_window(add_text))
            open_button.pack(side="left")

            remove_button = customtkinter.CTkButton(button_frame, image=remove_image, text="", command=lambda: self.remove_list_item(switch_frame))
            remove_button.pack(side="left", padx=5)

            switch_frame.grid_columnconfigure(0, weight=1)
            self.scrollable_frame_switches.append(switch)
            self.lists_data[add_text] = []  # Initialize an empty list for the added list

        add_textbox.master.destroy()


    def remove_list_item(self, switch_frame):
        switch_frame.destroy()
        self.scrollable_frame_switches.remove(switch_frame.winfo_children()[0])


    def open_list_window(self, list_name):
        self.open_window = customtkinter.CTkToplevel(self)
        self.open_window.title(list_name)
        self.open_window.transient(self)
        self.open_window.geometry("375x600")

        # Retrieve the list's data from lists_data dictionary
        list_data = self.lists_data[list_name]

        for item, amount in list_data:
            item_frame = customtkinter.CTkFrame(self.open_window)
            item_frame.pack()

            checkbox_var = tkinter.IntVar(value=0)
            checkbox = customtkinter.CTkCheckBox(item_frame, text="", variable=checkbox_var)
            checkbox.grid(row=0, column=0, padx=5, sticky="w")

            description_label = customtkinter.CTkLabel(item_frame, text=item, font=("Montserrat", 14))
            description_label.grid(row=0, column=1, padx=(0, 10), sticky="w")

            if item in fruits_list:
                correct_image = fruits_image
            elif item in vegetables_list:
                correct_image = vegetables_image
            elif item in grains_list:
                correct_image = grains_image
            elif item in dairy_list:
                correct_image = dairy_image
            elif item in spices_list:
                correct_image = spices_image
            elif item in alcohol_list:
                correct_image = alcohol_image
            else:
                # Handle the case when description doesn't match any category
                correct_image = questionmark_image

            item_image = customtkinter.CTkLabel(item_frame, text="", image=correct_image)
            item_image.grid(row=0, column=2, padx=(0, 10))

            delete_button = customtkinter.CTkButton(item_frame, image=remove_image, text="", command=lambda: self.remove_item(item_frame, list_name, item))
            delete_button.grid(row=0, column=3, padx=5)


        # Add the "Add" button to the open window
        add_button = customtkinter.CTkButton(self.open_window, text="Add", command=self.add_item_window)
        add_button.pack(side="bottom", pady=10)



    def add_item_window(self):
        add_item_window = customtkinter.CTkToplevel(self)
        add_item_window.title("Add your items")
        add_item_window.transient(self)
        add_item_window.geometry("375x400")

        description_label = customtkinter.CTkLabel(add_item_window, text="Description:")
        description_label.grid(row=0, column=0, padx=10, pady=5)

        description_textbox = customtkinter.CTkTextbox(add_item_window, font=("Montserrat", 20))
        description_textbox.configure(height=8)
        description_textbox.grid(row=1, column=0, padx=10, pady=5)

        amount_label = customtkinter.CTkLabel(add_item_window, text="Amount/Unit:")
        amount_label.grid(row=2, column=0, padx=10, pady=5)

        amount_textbox = customtkinter.CTkTextbox(add_item_window, font=("Montserrat", 20))
        amount_textbox.configure(height=8)
        amount_textbox.grid(row=3, column=0, padx=10, pady=5)

        button_frame = customtkinter.CTkFrame(add_item_window)
        button_frame.grid(row=4, column=0, padx=10, pady=5)

        confirm_button = customtkinter.CTkButton(button_frame, text="Add", command=lambda: self.add_item(description_textbox, amount_textbox))
        confirm_button.grid(row=0, column=0, padx=5)

        cancel_button = customtkinter.CTkButton(button_frame, text="Cancel", command=add_item_window.destroy)
        cancel_button.grid(row=0, column=1, padx=5)

        add_item_window.grab_set()


    def add_item(self, description_textbox, amount_textbox):
        description = description_textbox.get("1.0", tkinter.END).strip()
        amount = amount_textbox.get("1.0", tkinter.END).strip()

        if description and amount:
            item_frame = customtkinter.CTkFrame(self.open_window)
            item_frame.pack()

            checkbox_var = tkinter.IntVar(value=0)
            checkbox = customtkinter.CTkCheckBox(item_frame, text="", variable=checkbox_var)
            checkbox.grid(row=0, column=0, padx=5, sticky="w")

            description_label = customtkinter.CTkLabel(item_frame, text=f"{description} - {amount}", font=("Montserrat", 14))
            description_label.grid(row=0, column=1, padx=(0, 10), sticky="w")

            if description in fruits_list:
                correct_image = fruits_image
            elif description in vegetables_list:
                correct_image = vegetables_image
            elif description in grains_list:
                correct_image = grains_image
            elif description in dairy_list:
                correct_image = dairy_image
            elif description in spices_list:
                correct_image = spices_image
            elif description in alcohol_list:
                correct_image = alcohol_image
            else:
                # Handle the case when description doesn't match any category
                correct_image = questionmark_image

            item_image = customtkinter.CTkLabel(item_frame, text="", image=correct_image)
            item_image.grid(row=0, column=2, padx=(0, 10))

            delete_button = customtkinter.CTkButton(item_frame, image=remove_image, text="", command=lambda: self.remove_item(item_frame, list_name, description))
            delete_button.grid(row=0, column=3, padx=5)

            # Update the corresponding list's data in the lists_data dictionary
            list_name = self.open_window.title()
            self.lists_data[list_name].append((description, amount))

            # Clear the content of the textboxes
            description_textbox.delete("1.0", tkinter.END)
            amount_textbox.delete("1.0", tkinter.END)


    def remove_item(self, item_frame, list_name, item):
        item_frame.destroy()
        self.lists_data[list_name] = [(desc, amount) for desc, amount in self.lists_data[list_name] if desc != item]



def function_1():
    return


def function_2():
    return


def function_n():
    return


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
