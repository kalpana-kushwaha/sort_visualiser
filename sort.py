import tkinter as tk
from tkinter import messagebox
import random
import os
from sorting_algorithms import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    heap_sort,
)

class SortingVisualizer:
    def __init__(self, root, num_boxes, sort_type):
        self.root = root
        self.root.title("Sorting Visualizer")

        self.num_boxes = num_boxes
        self.sort_type = sort_type
        self.boxes = []

        self.sort_method_label = tk.Label(root, text=f"Sorting Method: {sort_type}",
                                          font=("Arial", 10, "bold"))

        self.sort_method_label.pack()

        self.canvas = tk.Canvas(root, width=500, height=300, bg="black")
        self.canvas.pack()

        y_position = 80
        self.generate_boxes(y_position)

        frame = tk.Frame(root)
        frame.pack()

        self.sort_button = tk.Button(root, text="Sort", command=self.sort,bd=5,
                                     highlightbackground="black")
        self.sort_button.pack(pady=10)

        self.go_back_button = tk.Button(root, text="Go Back", command=self.go_back,bd=5,
                                     highlightbackground="black")
        self.go_back_button.pack(side=tk.LEFT, padx=10)

        self.exit_button = tk.Button(root, text="Exit", command=root.destroy,bd=5,
                                     highlightbackground="black")
        self.exit_button.pack(side=tk.LEFT, padx=5)

    def generate_boxes(self, y_position):
        for i in range(self.num_boxes):
            number = random.randint(1, 100)
            box = self.canvas.create_rectangle(i * 50, y_position, (i + 1) * 50, y_position + 50,
                                               fill="royalblue1")
            label = self.canvas.create_text((i * 50) + 25, y_position + 25, text=str(number),
                                            fill="white", font=("Arial", 12, "bold"))
            self.boxes.append((box, label, number))

    def sort(self):
        if self.sort_type == "Bubble Sort":
            bubble_sort(self.boxes, self.highlight_box, self.update_boxes_positions, self.root)
        elif self.sort_type == "Selection Sort":
            selection_sort(self.boxes, self.highlight_box, self.update_boxes_positions, self.root)
        elif self.sort_type == "Insertion Sort":
            insertion_sort(self.boxes, self.highlight_box, self.update_boxes_positions, self.root)
        elif self.sort_type == "Merge Sort":
            merge_sort(self.boxes, self.highlight_box, self.update_boxes_positions, self.root)
        elif self.sort_type == "Quick Sort":
            quick_sort(self.boxes, self.highlight_box, self.update_boxes_positions, self.root)
        elif self.sort_type == "Heap Sort":
            heap_sort(self.boxes, self.highlight_box, self.update_boxes_positions, self.root)

    def highlight_box(self, boxes, index, color):
        box, label, _ = boxes[index]
        self.canvas.itemconfig(box, fill=color)

    def update_boxes_positions(self, boxes, root):
        for i, (box, label, number) in enumerate(boxes):
            x1, y1, x2, y2 = self.canvas.coords(box)
            new_x1 = i * 50
            new_x2 = (i + 1) * 50
            self.canvas.coords(box, new_x1, y1, new_x2, y2)
            self.canvas.coords(label, (new_x1 + new_x2) / 2, (y1 + y2) / 2)

    def go_back(self):
        self.root.destroy()  # Close the sorting window
        os.system("python sort.py")


class InputWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Visualizer Input")
        self.root.geometry("300x200")
        self.root.eval('tk::PlaceWindow . center')
        self.num_boxes_label = tk.Label(root, text="Enter the number of boxes:")
        self.num_boxes_label.pack()

        self.num_boxes_entry = tk.Entry(root)
        self.num_boxes_entry.pack()

        self.sort_type_label = tk.Label(root, text="Select sorting algorithm:")
        self.sort_type_label.pack()

        self.sort_type_var = tk.StringVar()
        self.sort_type_var.set("Bubble Sort")

        algorithms = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Heap Sort"]
        self.sort_type_menu = tk.OptionMenu(root, self.sort_type_var, *algorithms)
        self.sort_type_menu.pack(pady=10)

        self.start_button = tk.Button(root, text="Start", command=self.start_visualizer,bd=5,
                                      highlightbackground="black")
        self.start_button.pack(pady=10)

        self.main_menu_button = tk.Button(root, text="Main Menu", command=self.go_to_main_menu,
                                          bd=5,highlightbackground="black")
        self.main_menu_button.pack(side=tk.LEFT, padx=5)

        self.exit_button = tk.Button(root, text="Exit", command=root.destroy,bd=5,
                                     highlightbackground="black")
        self.exit_button.pack(side=tk.LEFT, padx=5)

    def start_visualizer(self):
        try:
            num_boxes = int(self.num_boxes_entry.get())
            sort_type = self.sort_type_var.get()

            if num_boxes <= 0:
                raise ValueError("Number of boxes must be greater than 0.")

            root.withdraw()  # Hide the input window
            visualizer_root = tk.Tk()
            visualizer_root.geometry("600x400")
            visualizer = SortingVisualizer(visualizer_root, num_boxes, sort_type)
            visualizer_root.mainloop()

        except ValueError as e:
            messagebox.showerror("Error", str(e))
    def go_to_main_menu(self):
        self.root.destroy()  # Close the sorting window
        os.system("python main_menu.py")

if __name__ == "__main__":
    root = tk.Tk()
    input_window = InputWindow(root)
    root.mainloop()
