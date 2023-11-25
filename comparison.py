import tkinter as tk
from tkinter import messagebox
import random
import time
import os
import threading
from sorting_algorithms2 import ( bubble_sort, selection_sort, insertion_sort,  merge_sort,
    quick_sort, heap_sort,)

class SortingComparisonVisualizer:
    def __init__(self, root, num_boxes, algo1, algo2):
        self.root = root
        self.root.title("Sorting Algorithm Comparison")

        self.num_boxes = num_boxes
        self.algo1 = algo1
        self.algo2 = algo2

        self.random_numbers = [random.randint(1, 100) for _ in range(num_boxes)]

        self.boxes1 = []
        self.boxes2 = []

        self.canvas1 = tk.Canvas(root, width=500, height=300, bg="black")
        self.canvas1.pack(side=tk.LEFT, padx=10)

        self.canvas2 = tk.Canvas(root, width=500, height=300, bg="black")
        self.canvas2.pack(side=tk.RIGHT, padx=10)

        y_position = 80
        self.generate_boxes(self.boxes1, y_position, self.canvas1)
        self.generate_boxes(self.boxes2, y_position, self.canvas2)

        frame = tk.Frame(root)
        frame.pack()

        self.sort_button = tk.Button(root, text="Sort", command=self.sort,bd=5,
                                     highlightbackground="black")
        self.sort_button.pack(pady=10)

        self.go_back_button = tk.Button(root, text="Go Back", command=self.go_back,bd=5,
                                     highlightbackground="black")
        self.go_back_button.pack(pady=10)

        self.exit_button = tk.Button(root, text="Exit", command=root.destroy, bd=5,
                                     highlightbackground="black")
        self.exit_button.pack(side=tk.LEFT, padx=5)

        self.time_label_algo1 = tk.Label(root, text=f"{algo1} Time: 0.000000 seconds",bd=5,
                                     highlightbackground="black")
        self.time_label_algo1.pack()
        self.time_label_algo1.place(relx=0.0, rely=1.0, anchor='sw')

        self.time_label_algo2 = tk.Label(root, text=f"{algo2} Time: 0.000000 seconds")
        self.time_label_algo2.pack()
        self.time_label_algo2.place(relx=1.0, rely=1.0, anchor='se')

    def generate_boxes(self, boxes, y_position, canvas):
        for i in range(self.num_boxes):
            number = self.random_numbers[i]
            box = canvas.create_rectangle(i * 50, y_position, (i + 1) * 50, y_position + 50, fill="royalblue1")
            label = canvas.create_text((i * 50) + 25, y_position + 25, text=str(number), fill="white", font=("Arial", 12, "bold"))
            boxes.append((box, label, number))

    def sort(self):
        self.thread1 = threading.Thread(target=self.run_algorithm, args=(
        self.algo1, self.boxes1, self.canvas1, self.time_label_algo1))
        self.thread2 = threading.Thread(target=self.run_algorithm, args=(
        self.algo2, self.boxes2, self.canvas2, self.time_label_algo2))

        self.thread1.start()
        self.thread2.start()

        self.root.after(100, self.check_threads)

    def check_threads(self):
        if self.thread1.is_alive() or self.thread2.is_alive():
            self.root.after(100, self.check_threads)
        else:
            # Both threads have completed
            self.thread1.join()
            self.thread2.join()

    def run_algorithm(self, algorithm, boxes, canvas, time_label):
        start_time = time.time()
        self.execute_algorithm(algorithm, boxes, canvas)
        end_time = time.time()
        time_complexity = end_time - start_time
        time_label.config(text=f"{algorithm} Time: {time_complexity:.6f} seconds")


    def execute_algorithm(self, algorithm, boxes, canvas):
        if algorithm == "Bubble Sort":
            bubble_sort(boxes, self.highlight_box, self.update_boxes_positions, canvas)
        elif algorithm == "Selection Sort":
            selection_sort(boxes, self.highlight_box, self.update_boxes_positions, canvas)
        elif algorithm == "Insertion Sort":
            insertion_sort(boxes, self.highlight_box, self.update_boxes_positions, canvas)
        elif algorithm == "Merge Sort":
            merge_sort(boxes, self.highlight_box, self.update_boxes_positions, canvas)
        elif algorithm == "Quick Sort":
            quick_sort(boxes, self.highlight_box, self.update_boxes_positions, canvas)
        elif algorithm == "Heap Sort":
            heap_sort(boxes, self.highlight_box, self.update_boxes_positions, canvas)

    def highlight_box(self, boxes, index, color, canvas):
        box, label, _ = boxes[index]
        canvas.itemconfig(box, fill=color)

    def update_boxes_positions(self, boxes, canvas):
        for i, (box, label, number) in enumerate(boxes):
            x1, y1, x2, y2 = canvas.coords(box)
            new_x1 = i * 50
            new_x2 = (i + 1) * 50
            canvas.coords(box, new_x1, y1, new_x2, y2)
            canvas.coords(label, (new_x1 + new_x2) / 2, (y1 + y2) / 2)

    def go_back(self):
        self.root.destroy()  # Close the sorting window
        os.system("python comparison.py")

class InputWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Comparison Visualizer Input")
        self.root.geometry("300x250")
        self.root.eval('tk::PlaceWindow . center')
        self.num_boxes_label = tk.Label(root, text="Enter the number of boxes:")
        self.num_boxes_label.pack()

        self.num_boxes_entry = tk.Entry(root)
        self.num_boxes_entry.pack()

        self.algo1_label = tk.Label(root, text="Select first sorting algorithm:")
        self.algo1_label.pack()

        self.algo1_var = tk.StringVar()
        self.algo1_var.set("Bubble Sort")

        algorithms = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Heap Sort"]
        self.algo1_menu = tk.OptionMenu(root, self.algo1_var, *algorithms)
        self.algo1_menu.pack()

        self.algo2_label = tk.Label(root, text="Select second sorting algorithm:")
        self.algo2_label.pack()

        self.algo2_var = tk.StringVar()
        self.algo2_var.set("Selection Sort")

        self.algo2_menu = tk.OptionMenu(root, self.algo2_var, *algorithms)
        self.algo2_menu.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_comparison_visualizer,bd=5,
                                     highlightbackground="black")
        self.start_button.pack()

        self.main_menu_button = tk.Button(root, text="Main Menu", command=self.go_to_main_menu,
                                         bd=5, highlightbackground="black")
        self.main_menu_button.pack(side=tk.LEFT, padx=5,pady=10)

        self.exit_button = tk.Button(root, text="Exit", command=root.destroy, bd=5,
                                     highlightbackground="black")

        self.exit_button.pack(side=tk.LEFT, padx=5,pady=10)

    def start_comparison_visualizer(self):
        try:
            num_boxes = int(self.num_boxes_entry.get())
            algo1 = self.algo1_var.get()
            algo2 = self.algo2_var.get()

            if num_boxes <= 0:
                raise ValueError("Number of boxes must be greater than 0.")

            self.root.withdraw()  # Hide the input window
            comparison_visualizer_root = tk.Tk()
            comparison_visualizer_root.geometry("1100x400")
            comparison_visualizer = SortingComparisonVisualizer(comparison_visualizer_root, num_boxes, algo1, algo2)
            comparison_visualizer_root.mainloop()

        except ValueError as e:
            messagebox.showerror("Error", str(e))
    def go_to_main_menu(self):
        self.root.destroy()  # Close the sorting window
        os.system("python main_menu.py")
if __name__ == "__main__":
    root = tk.Tk()
    input_window = InputWindow(root)
    root.mainloop()
