from tkinter import *

# Create window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=10, height=10)
window.config(padx=10,pady=10)
window.frame()

# Create calculate button function
def button_clicked():
    result_km = float(input_text_box.get()) * 1.609344
    print(result_km)
    result_display = Label(text=result_km, font=("Arial", 16))
    result_display.grid(row=1, column=2)

button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=2)

# Create query entry box
input_text_box = Entry(width=10)
input_text_box.grid(row=0, column=2)

# Label Miles
miles_label = Label(text="Miles", font=("Arial", 20))
miles_label.grid(row=0, column=3)

# Label Kilometers
miles_label = Label(text="Km", font=("Arial", 20))
miles_label.grid(row=1, column=3)

# result label
result_label = Label(text="is equal to", font=("Arial", 20))
result_label.grid(row=1, column=0)


window.mainloop()
