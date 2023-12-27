from tkinter import *

# Conversion factor from miles to kilometers
MILE = 1.609344


# Function to convert miles to kilometers
def mile_to_km(miles):
    return miles * MILE


# Function triggered when the "Calculate" button is clicked
def button_clicked():
    # Get the miles value from the input, convert it to float
    miles = float(miles_input.get())
    # Calculate kilometers and update the result label
    km_format = mile_to_km(miles)
    kilometer_result_label.config(text=f"{km_format:.2f}")


# Create the main Tkinter window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Calculate button
calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(row=3, column=3)

# Miles label
miles_label = Label(text="Miles")
miles_label.grid(row=1, column=4)

# "is equal to" label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=2, column=1)

# Kilometer result label
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(row=2, column=3)

# Kilometer label
kilometer_label = Label(text="Km")
kilometer_label.grid(row=2, column=4)

# Miles input field
miles_input = Entry(width=10)
miles_input.grid(row=1, column=3)

# Start the Tkinter event loop
window.mainloop()
