import time

def bubble_sort(boxes, highlight_box, update_boxes_positions, canvas):
    num_boxes = len(boxes)
    for i in range(num_boxes - 1):
        for j in range(num_boxes - i - 1):
            if boxes[j][2] > boxes[j + 1][2]:
                highlight_box(boxes, j, "red", canvas)
                boxes[j], boxes[j + 1] = boxes[j + 1], boxes[j]
                update_boxes_positions(boxes, canvas)
                time.sleep(0.6)
                canvas.update()
                highlight_box(boxes, j, "royalblue1", canvas)


def selection_sort(boxes, highlight_box, update_boxes_positions, canvas):
    num_boxes = len(boxes)
    for i in range(num_boxes):
        min_index = i
        for j in range(i + 1, num_boxes):
            if boxes[j][2] < boxes[min_index][2]:
                min_index = j
        highlight_box(boxes, i, "red", canvas)
        highlight_box(boxes, min_index, "green", canvas)
        boxes[i], boxes[min_index] = boxes[min_index], boxes[i]
        update_boxes_positions(boxes, canvas)
        time.sleep(0.6)
        canvas.update()
        highlight_box(boxes, i, "royalblue1",canvas)



def insertion_sort(boxes, highlight_box, update_boxes_positions, canvas):
    num_boxes = len(boxes)
    for i in range(1, num_boxes):
        key = boxes[i]
        j = i - 1
        while j >= 0 and key[2] < boxes[j][2]:
            highlight_box(boxes, j, "red", canvas)
            boxes[j + 1] = boxes[j]
            j -= 1
            update_boxes_positions(boxes, canvas)
            time.sleep(0.6)
            canvas.update()
            highlight_box(boxes, j, "royalblue1", canvas)
        boxes[j + 1] = key
        update_boxes_positions(boxes, canvas)
        time.sleep(0.6)
        canvas.update()


def merge_sort(boxes, highlight_box, update_boxes_positions, canvas):
    def merge_sort_recursive(low, high):
        if low < high:
            mid = (low + high) // 2
            merge_sort_recursive(low, mid)
            merge_sort_recursive(mid + 1, high)
            merge(low, mid, high)

    def merge(low, mid, high):
        left = boxes[low:mid + 1]
        right = boxes[mid + 1:high + 1]

        i = j = 0
        k = low

        while i < len(left) and j < len(right):
            if left[i][2] < right[j][2]:
                highlight_box(boxes, low + i, "red", canvas)
                boxes[k] = left[i]
                i += 1
            else:
                highlight_box(boxes, mid + 1 + j, "red", canvas)
                boxes[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            highlight_box(boxes, low + i, "red", canvas)
            boxes[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            highlight_box(boxes, mid + 1 + j, "red", canvas)
            boxes[k] = right[j]
            j += 1
            k += 1

        update_boxes_positions(boxes, canvas)
        time.sleep(0.6)
        canvas.update()
        highlight_box(boxes, low, "royalblue1", canvas)

    merge_sort_recursive(0, len(boxes) - 1)


def quick_sort(boxes, highlight_box, update_boxes_positions, canvas):
    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    def partition(low, high):
        pivot = boxes[high]
        i = low - 1

        # Highlight the pivot element with a different color
        highlight_box(boxes, high, "orange", canvas)
        update_boxes_positions(boxes, canvas)
        time.sleep(0.6)
        canvas.update()
        highlight_box(boxes, high, "royalblue1", canvas)  # Reset the color after highlighting

        for j in range(low, high):
            if boxes[j][2] < pivot[2]:
                i += 1
                boxes[i], boxes[j] = boxes[j], boxes[i]
                highlight_box(boxes, i, "red", canvas)
                update_boxes_positions(boxes, canvas)
                time.sleep(0.6)
                canvas.update()
                highlight_box(boxes, i, "royalblue1", canvas)

        boxes[i + 1], boxes[high] = boxes[high], boxes[i + 1]
        highlight_box(boxes, i + 1, "red", canvas)
        update_boxes_positions(boxes, canvas)
        time.sleep(0.6)
        canvas.update()
        highlight_box(boxes, i + 1, "royalblue1", canvas)

        return i + 1

    quick_sort_recursive(0, len(boxes) - 1)


def heap_sort(boxes, highlight_box, update_boxes_positions, canvas):
    def heapify(n, i):
        largest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and boxes[left_child][2] > boxes[largest][2]:
            largest = left_child

        if right_child < n and boxes[right_child][2] > boxes[largest][2]:
            largest = right_child

        if largest != i:
            highlight_box(boxes, i, "red", canvas)
            boxes[i], boxes[largest] = boxes[largest], boxes[i]
            update_boxes_positions(boxes, canvas)
            time.sleep(0.6)
            canvas.update()
            highlight_box(boxes, i, "royalblue1", canvas)
            heapify(n, largest)

    n = len(boxes)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for i in range(n - 1, 0, -1):
        highlight_box(boxes, i, "red", canvas)
        boxes[i], boxes[0] = boxes[0], boxes[i]
        update_boxes_positions(boxes, canvas)
        time.sleep(0.6)
        canvas.update()
        highlight_box(boxes, i, "royalblue1", canvas)
        heapify(i, 0)
