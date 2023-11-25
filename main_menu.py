# main.py

import tkinter as tk
from tkinter import messagebox
import os

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Visualizer Main Menu")
        self.root.geometry("300x150")
        self.root.eval('tk::PlaceWindow . center')

        self.selected_algorithm = tk.StringVar()
        self.selected_algorithm.set("None")

        self.sort_button = tk.Button(root, text="Sort", command=self.start_sort, bd=5,
                                      highlightbackground="black")
        self.sort_button.pack(pady=10)

        self.comparison_button = tk.Button(root, text="Comparison", command=self.start_comparison, bd=5,
                                            highlightbackground="black")
        self.comparison_button.pack(pady=10)

        self.exit_button = tk.Button(root, text="Exit", command=root.destroy, bd=5,
                                     highlightbackground="black")
        self.exit_button.pack(pady=10)

        self.selected_algo_label = tk.Label(root, textvariable=self.selected_algorithm)
        self.selected_algo_label.pack()

    def start_sort(self):
        self.root.destroy()
        os.system("python sort.py")


    def start_comparison(self):
        self.root.destroy()
        os.system("python comparison.py")


if __name__ == "__main__":
    root = tk.Tk()
    main_menu = MainMenu(root)
    root.mainloop()
