from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Sorting")
window.config(bg="#0159D3")

# variables
numbers = [42, 12, 13, 89, 63, 11]

# functions


def selection_sort():
    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    display_ordered_list.config(text=numbers)


# widgets
unordered_list_label = Label(window, text="Unordered list", )
display_unordered_list = Label(window, text="42, 12, 13, 89, 63, 11")
ordered_list_label = Label(window, text="Ordered list",)
display_ordered_list = Label(window, text="")
sort_button = Button(window, text="Sort", command=selection_sort)

# placing
unordered_list_label.place(x=100, y=50)
display_unordered_list.place(x=200, y=50)
ordered_list_label.place(x=100, y=100)
display_ordered_list.place(x=200, y=100)
sort_button.place(x=300, y=150)

window.mainloop()
