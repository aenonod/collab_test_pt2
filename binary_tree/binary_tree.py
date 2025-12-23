import tkinter as tk
from tkinter import *

class TreeGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080")
        self.title("Structura")

        self.setup_background()
        self.setup_label()

    def setup_background(self):
        self.bg_image = PhotoImage(file="binary_tree/background.png")
        bg_label = Label(self, image=self.bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def setup_label(self):
        self.label_frame = Frame(self,
                                 bg = "#6e7bb2",
                                 width=850, height=92,
                                 bd = 8, relief = "solid")
        self.label_frame.place(relx=0.99, rely=0.02, anchor="ne")
        self.label_text = Label(self.label_frame,
                                text="Binary Tree",
                                font=("Press Start 2P", 20, "bold"),
                                fg = "white",
                                bg="#6e7bb2")
        self.label_text.pack(padx=30, pady=15)


if __name__ == "__main__":
    app = TreeGUI()
    app.mainloop()